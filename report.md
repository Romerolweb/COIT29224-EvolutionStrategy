# **COIT29224 Evolution Strategy Optimizer**

## **Overview**

This repository provides a modular Python implementation of an **Evolution Strategy (ES)** algorithm for optimizing complex, multi-modal objective functions. The project is designed for **Assignment 2** of the COIT29224 Evolutionary Computation course at CQUniversity, and demonstrates key ES concepts including:

* Population-based stochastic search  
* Variation through Gaussian mutation  
* Configurable survival selection: **(μ, λ)** and **(μ \+ λ)**

The codebase emphasizes clarity, extensibility, and robust documentation.

## **Key Features**

* **Modular OOP Design:** Core logic is encapsulated in EvolutionStrategy and Individual classes.  
* **Selection Strategies:** Supports both **(μ, λ)** (comma) and **(μ \+ λ)** (plus) survivor selection.  
* **Gaussian Mutation:** Configurable mutation strength (sigma) for exploration.  
* **Boundary Handling:** Solutions are clipped to remain within user-specified bounds.  
* **Benchmark Functions:** Includes the Rastrigin function; easily extensible for others.  
* **Visualization:** Generates convergence plots and, for 2D problems, a landscape plot showing the best solution.  
* **Logging:** Each run is logged with a unique batch ID, and plots are saved in batch-specific folders.  
* **Reproducibility:** Supports random seeds for repeatable experiments.  
* **Extensible:** Add new objective functions by editing a single file.

## **Project Structure**
```bash
.  
├── LICENSE                         \# Project license (GPL)  
├── README.md                       \# This documentation file  
├── es\_optimiser/                   \# Main Python package for ES logic  
│   ├── \_\_init\_\_.py                 \# Package initializer  
│   ├── \_\_pycache\_\_/                \# Python bytecode cache  
│   ├── evolution\_strategy.py       \# ES algorithm implementation  
│   ├── objective\_functions.py      \# Fitness/objective functions (e.g., Rastrigin)  
│   └── plot.py                     \# Plotting utilities  
├── logs/                           \# Output logs directory  
├── main.py                         \# Main script to run the optimizer  
├── plan-to-develop.md              \# Future development notes  
├── requirements.txt                \# Python package dependencies  
├── plots/                          \# Output plots directory  
│   ├── batch_id/                 \# Run-specific plots  
│   └── plots.md                    \# Plot documentation/notes  
└── report.md                       \# Project report
```
## **Installation**

**Requirements:**

* Python 3.8 or newer  
* NumPy  
* Matplotlib

**Setup:**

1. Clone the repository:  
   git clone https://github.com/Romerolweb/COIT29224-EvolutionStrategy.git  
   cd COIT29224-EvolutionStrategy

2. (Recommended) Create and activate a virtual environment:  
   python \-m venv venv  
   * source venv/bin/activate    
   * .\\venv\\Scripts\\activate \# On Windows:

3. Install dependencies:  
   pip install \-r requirements.txt

## **How to Run**

Run the main script from the project root:

python main.py

**What happens:**

* The script prints the ES configuration and progress.  
* Upon completion, it prints the best solution found.  
* Convergence and (if 2D) landscape plots are saved in a batch-specific folder under plots/.  
* All run details are logged in the logs/ directory.

## **Configuration**

Edit the parameters in main.py (inside the run\_es\_optimization function or the main block):

* PROBLEM\_DIMENSIONS: Number of variables (int)  
* SEARCH\_BOUNDS: Tuple of (min, max) for each variable  
* POPULATION\_MU: Number of parents (μ)  
* OFFSPRING\_LAMBDA: Number of offspring (λ)  
* GENERATIONS: Number of generations  
* MUTATION\_SIGMA: Mutation strength (σ)  
* SELECTION\_STRATEGY: '(mu, lambda)' or '(mu \+ lambda)'  
* RANDOM\_SEED: Integer or None  
* objective\_function: Function to optimize (e.g., rastrigin)

## **Adding Objective Functions**

1. Define the function in es\_optimiser/objective\_functions.py:  
   def my\_function(x: np.ndarray) \-\> float:  
       \# Implementation of the objective function  
       return value

2. Update main.py to use the new function:  
   from es\_optimiser.objective\_functions import my\_function  
   \# ...  
   es\_optimizer \= EvolutionStrategy(  
       objective\_function=my\_function,  
       \# ...  
   )

## **Output**

* **Logs:** Each run creates a log file in logs/ with a unique batch ID.  
* **Plots:** Convergence and landscape plots are saved in plots/\<batch\_id\>/.  
* **Console:** Progress and summary statistics are printed.

# **Analysis of Evolution Strategy Performance on the Rastrigin Function: Impact of Seed and Selection Mechanism**

## **1\. Introduction**

Optimization of multi-modal functions, such as the Rastrigin function, presents a significant challenge due to the presence of numerous local minima. Evolution Strategies (ES) are population-based metaheuristic algorithms that utilize stochastic variation and selection to effectively explore complex search spaces.

This report analyzes the performance of a configured ES on the 2D Rastrigin function. The analysis investigates how the results vary based on two primary factors:

1. **Random Seed**: The seed initializes the random number generator, influencing the initial population and the sequence of random numbers used for mutations. This can significantly affect the search trajectory.  
2. **Selection Strategy**: Two strategies are compared:  
   * **(μ, λ)**: A non-elitist strategy where only offspring are considered for selection.  
   * **(μ \+ λ)**: An elitist strategy where both parents and offspring are considered for selection.

The aim is to evaluate the impact of these factors on the convergence behavior and final outcomes of the ES. The report is structured as follows: Section 2 provides background on ES and the Rastrigin function. Section 3 outlines the methodology employed in this study. Section 4 presents the results, followed by analysis and discussion in Section 5\. Finally, Section 6 concludes the report.

## **2\. Background**

### **2.1 Evolution Strategies (ES)**

Evolution Strategies are optimization algorithms inspired by natural evolution. They operate on a population of candidate solutions, iteratively applying variation (mutation) and selection to improve the fitness of individuals within the population. Key components of ES include:

* **Representation**: Solutions are represented as real-valued vectors.  
* **Mutation**: Gaussian noise is added to each component of the solution vector, introducing variation:  
  x′=x+N(0,σ2),  
  where ( \\sigma ) represents the mutation strength.  
* **Selection**: This process determines which individuals survive and reproduce. Two common strategies are:  
  * **(μ, λ)**: A non-elitist strategy that selects the best ( \\mu ) individuals from ( \\lambda ) offspring, discarding the parents. This strategy promotes exploration but may risk losing potentially valuable solutions.  
  * **(μ \+ λ)**: An elitist strategy that selects the best ( \\mu ) individuals from the combined pool of parents and offspring. This strategy guarantees monotonic improvement in fitness but can increase the risk of premature convergence to a sub-optimal solution.

### **2.2 Random Seed**

The random seed initializes the random number generator used by the ES algorithm. This initialization determines the initial population and the subsequent sequence of random mutations applied during the search process. Consequently, different seeds can lead to significantly different search trajectories. These variations can influence whether the algorithm converges to the global optimum or becomes trapped in a local optimum.

### **2.3 Rastrigin Function**

The Rastrigin function is a widely used benchmark function for evaluating the performance of optimization algorithms. It is defined as:

f(x)=10d+∑i=1d​\[xi2​−10cos(2πxi​)\],

where ( d ) is the dimensionality of the problem, and ( x\_i \\in \[-5.12, 5.12\] ). The function is characterized by a single global minimum at ( x \= (0, 0, \\dots, 0\) ) with a function value of ( f(x) \= 0 ), surrounded by numerous local minima. This complex landscape makes it a challenging testbed for optimization algorithms.

## **3\. Methodology**

### **3.1 Objective Function**

The 2D Rastrigin function was selected as the objective function for this study. The search bounds for each dimension are ( \[-5.12, 5.12\] ).

### **3.2 ES Implementation**

The ES algorithm was implemented in Python, with the following configurable parameters:

* **Population size (( \\mu ))**: 30  
* **Offspring size (( \\lambda ))**: 200  
* **Mutation strength (( \\sigma ))**: 0.2  
* **Maximum generations**: 250  
* **Selection strategies**: (μ, λ) and (μ \+ λ)  
* **Random seeds**: 123, 332, 456, 789, 101, 202, 303, 404\.

### **3.3 Experimental Setup**

A total of 16 configurations were tested. These configurations combined two selection strategies and eight different random seeds, as outlined in the following table:

| Run Label | Selection Type | Seed |
| :---- | :---- | :---- |
| A1 | (μ, λ) | 123 |
| A2 | (μ, λ) | 332 |
| A3 | (μ, λ) | 456 |
| A4 | (μ, λ) | 789 |
| A5 | (μ, λ) | 101 |
| A6 | (μ, λ) | 202 |
| A7 | (μ, λ) | 303 |
| A8 | (μ, λ) | 404 |
| B1 | (μ \+ λ) | 123 |
| B2 | (μ \+ λ) | 332 |
| B3 | (μ \+ λ) | 456 |
| B4 | (μ \+ λ) | 789 |
| B5 | (μ \+ λ) | 101 |
| B6 | (μ \+ λ) | 202 |
| B7 | (μ \+ λ) | 303 |
| B8 | (μ \+ λ) | 404 |

### **3.4 Performance Metrics**

The following metrics were used to evaluate the performance of the ES algorithm:

1. **Final best fitness achieved**: The fitness value of the best solution found at the end of the optimization process.  
2. **Best solution vector found**: The vector representing the solution (set of parameters) that yielded the best fitness.  
3. **Euclidean distance from the global optimum**: A measure of how close the best-found solution is to the known global optimum of the Rastrigin function.  
4. **Convergence behavior (fitness vs. generations)**: How the fitness of the best solution evolves over the generations, indicating the rate and stability of convergence.

## **4\. Results**

The results for all 16 runs are summarized in the following table:

| Batch ID | Run ID | Selection Strategy | Random Seed | Best Fitness | Best Genotype | Distance from Origin | Elapsed Time (seconds) | Convergence Plot Saved | Landscape Plot Saved |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 6e93dd33-88cb-4382-a962-b907568a327a | A1 | (mu, lambda) | 123 | 7.5433e-05 | \[-0.001 0\. \] | 6.1662e-04 | 2.18 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A2 | (mu, lambda) | 332 | 9.9502e-01 | \[0.995 0\. \] | 9.9537e-01 | 2.02 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A3 | (mu, lambda) | 456 | 7.5162e-05 | \[ 0.001 \-0. \] | 6.1551e-04 | 1.98 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A4 | (mu, lambda) | 789 | 6.0822e-05 | \[-0. 0.\] | 5.5369e-04 | 1.80 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A5 | (mu, lambda) | 101 | 8.7467e-01 | \[0.033 0.058\] | 6.6708e-02 | 1.81 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A6 | (mu, lambda) | 202 | 9.3981e-06 | \[0. 0.\] | 2.1765e-04 | 1.86 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A7 | (mu, lambda) | 303 | 9.9688e-01 | \[0.996 0.003\] | 9.9609e-01 | 1.89 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | A8 | (mu, lambda) | 404 | 1.9902e+00 | \[-0.995 \-0.994\] | 1.4066e+00 | 1.87 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B1 | (mu \+ lambda) | 123 | 3.8255e-05 | \[-0. \-0.\] | 4.3912e-04 | 2.09 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B2 | (mu \+ lambda) | 332 | 9.9507e-01 | \[0.995 0.001\] | 9.9522e-01 | 1.87 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B3 | (mu \+ lambda) | 456 | 6.5871e-05 | \[-0. \-0.\] | 5.7622e-04 | 1.89 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B4 | (mu \+ lambda) | 789 | 7.1229e-04 | \[0.002 0\. \] | 1.8948e-03 | 1.79 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B5 | (mu \+ lambda) | 101 | 9.9502e-01 | \[-0.995 \-0. \] | 9.9516e-01 | 1.86 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B6 | (mu \+ lambda) | 202 | 4.0219e-05 | \[0. 0.\] | 4.5025e-04 | 1.98 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B7 | (mu \+ lambda) | 303 | 1.9901e+00 | \[0.994 0.995\] | 1.4064e+00 | 1.89 | Yes | Yes |
| 6e93dd33-88cb-4382-a962-b907568a327a | B8 | (mu \+ lambda) | 404 | 1.9903e+00 | \[-0.995 \-0.996\] | 1.4082e+00 | 2.35 | Yes | Yes |

## **5\. Analysis and Discussion**

### **5.1 Impact of Random Seed**

The random seed had a significant impact on the optimization outcomes:

* Runs with Seed 123 (e.g., A1, B1) converged to the global optimum with high accuracy.  
* Runs with Seed 332 (e.g., A2, B2) converged to a local optimum, demonstrating the algorithm's sensitivity to initial conditions.

This highlights the stochastic nature of ES algorithms, where the initial population and the sequence of random mutations can substantially alter the search trajectory and the final result.

### **5.2 Impact of Selection Strategy**

* **(μ, λ)**: This strategy exhibited a tendency for greater exploration of the search space but demonstrated slower convergence.  
* **(μ \+ λ)**: This strategy showed faster convergence but exhibited a higher susceptibility to premature convergence, becoming trapped in local optima.

### **5.3 Overall Performance**

The random seed had a more pronounced effect on the final results than the selection strategy. The success of the optimization process was highly dependent on whether the initial search trajectory led the algorithm into the basin of attraction of the global optimum.

**Comparison Graph**

Include a comparison graph here.  
convergence\_A1.png, convergence\_A8.png, convergence\_B1.png, convergence\_B8.png

### **5.4 Visualization of Convergence and Landscape**

The following figures illustrate the convergence behavior and final solution for representative runs of each selection strategy.

**Strategy A: (μ, λ)**

The first row shows results for the (μ, λ) strategy.

The second row shows results for a different run of the (μ, λ) strategy.

**Strategy B: (μ \+ λ)**

The first row shows results for the (μ \+ λ) strategy.

The second row shows results for a different run of the (μ \+ λ) strategy.

## **6\. Conclusion**

This study demonstrated the sensitivity of the Evolution Strategy to random initialization and the trade-offs between the (μ, λ) and (μ \+ λ) selection strategies when applied to the Rastrigin function. While the (μ \+ λ) strategy exhibited faster convergence, the (μ, λ) strategy showed a greater capacity for exploration. The random seed, however, was the dominant factor influencing the success of the optimization.

Future work should include a greater number of independent runs for each configuration to enable more robust statistical analysis and to draw more definitive conclusions regarding the relative performance of the selection strategies. Additionally, investigating the impact of varying the mutation strength (( \\sigma )) could provide further insights into the algorithm's behavior.

## **7\. References**

1. Eiben, A.E. and Smith, J.E. (2015). *Introduction to Evolutionary Computing*. 2nd ed. Springer.  
2. Rastrigin, L.A. (1974). Systems of Extremal Control. *Moscow: Nauka*.  
3. Python NumPy Documentation: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
4. Python Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
5. Python Logging Documentation: [https://docs.python.org/3/library/logging.html](https://docs.python.org/3/library/logging.html)
6. Python Virtual Environments: [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)

## 8. Appendix

### 8.1 Full Logs
Below are the logs from all runs:

[Log file](es_optimization_A1.log)
(Note, the logs are too long to include in full here, but they can be found in the provided file. Numerous executions were performed, though, they are not included here, as the report should be readable for a general audience. Additional executions are indentified by UUIDs, and their generated plots are included in the plots folder. Furthermore, the logs will be located in a diferent folder named plots, and UUIDs will serve as a way to math the generated plots with the respective log.)

## Author

- **Sebastian Romero Laguna**
- COIT29224 Evolutionary Computation, CQUniversity
- Assignment 2, Term 1, 2025

