# es_optimiser/evolution_strategy.py
import numpy as np
from typing import Tuple, List, Callable, Optional # Optional is useful
# Re-import objective function if needed directly, though usually passed in
from .objective_functions import rastrigin # Example relative import

class Individual:
    """
    Represents a single candidate solution within the ES population.

    Encapsulates the solution vector (genotype) and its corresponding
    fitness value. Allows for easy comparison based on fitness.

    Attributes:
        genotype (np.ndarray): The vector representing the candidate solution's
                               parameters in the search space.
        fitness (float): The objective function value for this genotype.
                         Initialized to positive infinity until evaluated.
    """
    def __init__(self, genotype: np.ndarray, fitness: float = np.inf):
        """
        Initializes an Individual instance.

        Args:
            genotype (np.ndarray): The initial parameter vector.
            fitness (float, optional): The pre-calculated fitness value.
                                       Defaults to np.inf, indicating unevaluated.
        """
        self.genotype = genotype
        self.fitness = fitness

    def __lt__(self, other: 'Individual') -> bool:
        """
        Compares this individual to another based on fitness (for minimization).

        Allows sorting lists of Individuals directly using sort() or min().

        Args:
            other (Individual): The other individual to compare against.

        Returns:
            bool: True if this individual has a strictly smaller fitness value
                  than the other, False otherwise.
        """
        return self.fitness < other.fitness

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the individual.

        Returns:
            str: String showing fitness and genotype.
        """
        return f"Individual(fitness={self.fitness:.4e}, genotype={np.round(self.genotype, 3)})"


class EvolutionStrategy:
    """
    Implements a configurable Evolution Strategy (ES) for optimization.

    This class provides a framework for (μ, λ) or (μ + λ) selection strategies,
    using Gaussian mutation as the primary variation operator.

    Attributes:
        objective_function (Callable[[np.ndarray], float]): The function to minimize.
        dimensions (int): The number of variables in the solution vector.
        bounds (Tuple[float, float]): Lower and upper bounds for each variable.
        mu (int): The number of parents selected for the next generation.
        lambda_ (int): The number of offspring generated each generation.
        max_generations (int): The stopping criterion based on generations.
        sigma (float): The standard deviation (mutation strength) for Gaussian mutation.
        selection_type (str): Specifies survival selection: '(mu, lambda)' or '(mu + lambda)'.
        rng (np.random.Generator): NumPy random number generator for reproducibility.

        population (List[Individual]): The current population of parent individuals.
        best_individual_overall (Optional[Individual]): Best solution found across all generations.
        history (List[Tuple[int, float]]): Records the best fitness per generation.
    """
    def __init__(
        self,
        objective_function: Callable[[np.ndarray], float],
        dimensions: int,
        bounds: Tuple[float, float],
        mu: int,
        lambda_: int,
        max_generations: int = 100,
        sigma: float = 0.1,
        selection_type: str = '(mu, lambda)', # Default to comma selection
        seed: Optional[int] = None
    ):
        """
        Initializes the Evolution Strategy algorithm configuration.

        Args:
            objective_function: The target function to minimize.
            dimensions: Dimensionality of the search space.
            bounds: Tuple (min_val, max_val) applied to all dimensions.
            mu: Number of parent individuals.
            lambda_: Number of offspring to generate (must be >= mu for comma selection).
            max_generations: Maximum number of iterations. Defaults to 100.
            sigma: Mutation strength (standard deviation). Defaults to 0.1.
            selection_type: Survival strategy, '(mu, lambda)' or '(mu + lambda)'.
                            Defaults to '(mu, lambda)'.
            seed: Optional seed for the random number generator. Defaults to None.

        Raises:
            ValueError: If lambda_ < mu for '(mu, lambda)' selection.
            ValueError: If selection_type is not recognized.
        """
        self.objective_function = objective_function
        self.dimensions = dimensions
        self.bounds = bounds
        self.mu = mu
        self.lambda_ = lambda_
        self.max_generations = max_generations
        self.sigma = sigma

        if selection_type not in ['(mu, lambda)', '(mu + lambda)']:
            raise ValueError(f"Unknown selection_type: {selection_type}. Use '(mu, lambda)' or '(mu + lambda)'.")
        if selection_type == '(mu, lambda)' and self.lambda_ < self.mu:
             raise ValueError("For '(mu, lambda)' selection, lambda_ must be >= mu.")
        self.selection_type = selection_type

        self.rng = np.random.default_rng(seed) # Modern NumPy RNG

        self.population: List[Individual] = []
        self.best_individual_overall: Optional[Individual] = None
        self.history: List[Tuple[int, float]] = []

        print("--- ES Configuration ---")
        print(f" Objective Function: {self.objective_function.__name__}")
        print(f" Dimensions: {self.dimensions}")
        print(f" Bounds: {self.bounds}")
        print(f" Mu: {self.mu}, Lambda: {self.lambda_}")
        print(f" Selection Type: {self.selection_type}")
        print(f" Sigma (Mutation): {self.sigma}")
        print(f" Max Generations: {self.max_generations}")
        print(f" Seed: {seed}")
        print("------------------------")


    def _initialize_population(self):
        """Creates and evaluates the initial population of mu individuals."""
        self.population = []
        for _ in range(self.mu):
            genotype = self.rng.uniform(self.bounds[0], self.bounds[1], self.dimensions)
            fitness = self.objective_function(genotype)
            individual = Individual(genotype, fitness)
            self.population.append(individual)

        # Sort initial population and find initial best
        self.population.sort() # Uses Individual.__lt__
        self.best_individual_overall = self.population[0]
        self.history.append((0, self.best_individual_overall.fitness))
        print(f"Generation 0: Initial Best Fitness = {self.best_individual_overall.fitness:.4e}")

    def _generate_offspring(self) -> List[Individual]:
        """
        Generates lambda_ offspring from the current parent population via mutation.
        Parents for breeding are selected uniformly at random.
        """
        offspring_population = []
        for _ in range(self.lambda_):
            # 1. Select parent randomly (uniform choice from current parents)
            parent = self.rng.choice(self.population)

            # 2. Mutate parent's genotype
            # Add Gaussian noise N(0, sigma^2) to all components
            mutation = self.rng.normal(loc=0.0, scale=self.sigma, size=self.dimensions)
            mutated_genotype = parent.genotype + mutation

            # 3. Boundary Handling (Clipping)
            # Ensure the mutated genotype stays within the defined bounds
            mutated_genotype = np.clip(mutated_genotype, self.bounds[0], self.bounds[1])

            # 4. Evaluate fitness of the new genotype
            offspring_fitness = self.objective_function(mutated_genotype)

            # 5. Create new offspring individual
            offspring_individual = Individual(mutated_genotype, offspring_fitness)
            offspring_population.append(offspring_individual)

        return offspring_population

    def _select_survivors(self, offspring: List[Individual]):
        """
        Selects the next generation's parents based on the specified strategy.

        - '(mu, lambda)': Selects the best mu individuals *only* from the offspring.
        - '(mu + lambda)': Selects the best mu individuals from the *combined*
                           pool of parents and offspring.

        Args:
            offspring (List[Individual]): The list of generated offspring.
        """
        if self.selection_type == '(mu, lambda)':
            # Sort offspring by fitness and select the top mu
            offspring.sort()
            self.population = offspring[:self.mu]

        elif self.selection_type == '(mu + lambda)':
            # Combine parents and offspring
            combined_population = self.population + offspring
            # Sort the combined pool and select the top mu
            combined_population.sort()
            self.population = combined_population[:self.mu]
        # No else needed due to check in __init__

    def run(self) -> 'EvolutionStrategy':
        """
        Executes the main loop of the Evolution Strategy.

        Initializes the population, then iterates through generations, performing
        offspring generation and survivor selection. Tracks the best fitness found.

        Returns:
            EvolutionStrategy: Returns self to allow method chaining or
                                        easy access to results after running.
        """
        self._initialize_population()

        print("Starting Evolution...")
        for generation in range(1, self.max_generations + 1):
            # 1. Generate lambda offspring using mutation
            offspring = self._generate_offspring()

            # 2. Select mu survivors for the next generation's population
            self._select_survivors(offspring)

            # 3. Update best overall individual found so far
            current_best_in_pop = self.population[0] # Population is sorted after selection
            if current_best_in_pop < self.best_individual_overall:
                self.best_individual_overall = current_best_in_pop

            # 4. Record history
            self.history.append((generation, self.best_individual_overall.fitness))

            # --- Optional: Print progress periodically ---
            if generation % 20 == 0 or generation == self.max_generations:
                 print(f"Generation {generation}: "
                       f"Current Best Fitness = {current_best_in_pop.fitness:.4e}, "
                       f"Overall Best Fitness = {self.best_individual_overall.fitness:.4e}")

        print("Evolution finished.")
        print(f"Final Best Fitness: {self.best_individual_overall.fitness:.6e}")
        print(f"Best Solution Found: {np.round(self.best_individual_overall.genotype, 5)}")
        return self # Return self for convenience

    def get_best_solution(self) -> Optional[Individual]:
        """
        Returns the best individual found during the run.

        Returns:
            Optional[Individual]: The best Individual object, or None if run() hasn't completed.
        """
        return self.best_individual_overall

    def get_history(self) -> List[Tuple[int, float]]:
        """
        Returns the convergence history.

        Returns:
            List[Tuple[int, float]]: List of (generation, best_fitness) tuples.
        """
        return self.history


