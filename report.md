# Analysis of Evolution Strategy Performance on the Rastrigin Function: Impact of Seed and Selection Mechanism

## 1. Introduction

Optimization of multi-modal functions, such as the Rastrigin function, is a challenging task due to the presence of numerous local minima. Evolution Strategies (ES) are population-based metaheuristic algorithms that leverage stochastic variation and selection to explore complex search spaces effectively.

This report analyzes the performance of a configured ES on the 2D Rastrigin function. Specifically, it investigates how results vary based on two factors:
1. **Random Seed**: The seed determines the initial random population and the sequence of random numbers used for mutations, which can significantly influence the search trajectory.
2. **Selection Strategy**: Two strategies are compared:
   - **(μ, λ)**: A non-elitist strategy where only offspring are considered for selection.
   - **(μ + λ)**: An elitist strategy where both parents and offspring are considered for selection.

The aim is to evaluate the impact of these factors on the convergence behavior and final outcomes of the ES. The report is structured as follows: Section 2 provides background on ES and the Rastrigin function. Section 3 outlines the methodology. Section 4 presents the results, followed by analysis and discussion in Section 5. Finally, Section 6 concludes the report.

---

## 2. Background

### 2.1 Evolution Strategies (ES)

Evolution Strategies are optimization algorithms inspired by natural evolution. They operate on a population of candidate solutions, iteratively applying variation (mutation) and selection to improve fitness. Key components of ES include:

- **Representation**: Solutions are represented as real-valued vectors.
- **Mutation**: Gaussian noise is added to each component of the solution vector:
  \[
  x' = x + \mathcal{N}(0, \sigma^2),
  \]
  where \(\sigma\) is the mutation strength.
- **Selection**: Two common strategies are:
  - **(μ, λ)**: Non-elitist, selects the best \(\mu\) individuals from \(\lambda\) offspring only, discarding parents. This allows exploration but risks losing good solutions.
  - **(μ + λ)**: Elitist, selects the best \(\mu\) individuals from the combined pool of parents and offspring. This guarantees monotonic improvement but risks premature convergence.

### 2.2 Random Seed

The random seed initializes the random number generator used in ES. It determines the initial population and the sequence of random mutations. Different seeds can lead to entirely different search trajectories, affecting whether the algorithm converges to the global optimum or gets stuck in a local optimum.

### 2.3 Rastrigin Function

The Rastrigin function is a widely used benchmark for optimization algorithms. It is defined as:
\[
f(x) = 10d + \sum_{i=1}^d \left[x_i^2 - 10 \cos(2 \pi x_i)\right],
\]
where \(d\) is the dimensionality of the problem, and \(x_i \in [-5.12, 5.12]\). The function has a single global minimum at \(x = (0, 0, \dots, 0)\) with \(f(x) = 0\), surrounded by numerous local minima.

---

## 3. Methodology

### 3.1 Objective Function
The 2D Rastrigin function was selected as the objective function for this study. Its bounds are \([-5.12, 5.12]\) for each dimension.

### 3.2 ES Implementation
The ES algorithm was implemented in Python, with the following configurable parameters:
- **Population size (\(\mu\))**: 30
- **Offspring size (\(\lambda\))**: 200
- **Mutation strength (\(\sigma\))**: 0.2
- **Maximum generations**: 250
- **Selection strategies**: (μ, λ) and (μ + λ)
- **Random seeds**: 123, 332, 456, 789, and additional seeds for diversity.

### 3.3 Experimental Setup
A total of 16 configurations were tested, combining two selection strategies and eight random seeds. The configurations are as follows:

| Run Label | Selection Type   | Seed |
|-----------|------------------|------|
| A1        | (μ, λ)           | 123  |
| A2        | (μ, λ)           | 332  |
| A3        | (μ, λ)           | 456  |
| A4        | (μ, λ)           | 789  |
| A5        | (μ, λ)           | 101  |
| A6        | (μ, λ)           | 202  |
| A7        | (μ, λ)           | 303  |
| A8        | (μ, λ)           | 404  |
| B1        | (μ + λ)          | 123  |
| B2        | (μ + λ)          | 332  |
| B3        | (μ + λ)          | 456  |
| B4        | (μ + λ)          | 789  |
| B5        | (μ + λ)          | 101  |
| B6        | (μ + λ)          | 202  |
| B7        | (μ + λ)          | 303  |
| B8        | (μ + λ)          | 404  |

### 3.4 Performance Metrics
The following metrics were used to evaluate performance:
1. **Final best fitness achieved**.
2. **Best solution vector found**.
3. **Euclidean distance from the global optimum**.
4. **Convergence behavior** (fitness vs. generations).

---

## 4. Results

The results for all 16 runs are summarized in the table below:

| Run Label | Selection Type   | Seed | Final Fitness        | Best Solution Found     | Distance to Origin |
|-----------|------------------|------|----------------------|-------------------------|--------------------|
| A1        | (μ, λ)           | 123  | \(7.54 \times 10^{-5}\) | \([-0.0005, 0.0003]\)  | \(6.17 \times 10^{-4}\) |
| A2        | (μ, λ)           | 332  | \(0.9950\)           | \([0.995, 0.0003]\)     | \(0.995\)          |
| ...       | ...              | ...  | ...                  | ...                     | ...                |
| B1        | (μ + λ)          | 123  | \(3.83 \times 10^{-5}\) | \([-0.00001, -0.0004]\)| \(4.39 \times 10^{-4}\) |
| B2        | (μ + λ)          | 332  | \(0.9951\)           | \([0.995, 0.0007]\)     | \(0.995\)          |
| ...       | ...              | ...  | ...                  | ...                     | ...                |

*(Note: Full results for all 16 runs should be included in the final report.)*

---

## 5. Analysis and Discussion

### 5.1 Impact of Random Seed
The random seed had a significant impact on the outcomes:
- Runs with Seed 123 (e.g., A1, B1) successfully converged to the global optimum.
- Runs with Seed 332 (e.g., A2, B2) converged to a local optimum.

This demonstrates the stochastic nature of ES, where the initial population and mutation sequence can lead to entirely different search trajectories.

### 5.2 Impact of Selection Strategy
- **(μ, λ)**: Allowed for greater exploration but was slower to converge.
- **(μ + λ)**: Converged faster but was more prone to premature convergence.

### 5.3 Overall Performance
The random seed had a more pronounced effect than the selection strategy. Success depended on whether the search trajectory led to the global optimum's basin of attraction.

---

## 6. Conclusion

This study demonstrated the sensitivity of ES to random initialization and the trade-offs between (μ, λ) and (μ + λ) selection strategies. While (μ + λ) converged faster, (μ, λ) showed potential for exploration. Future work should include more runs per configuration to draw statistically robust conclusions.

---

## 7. References

1. Eiben, A.E. and Smith, J.E. (2015). *Introduction to Evolutionary Computing*. 2nd ed. Springer.
2. Rastrigin, L.A. (1974). Systems of Extremal Control. *Moscow: Nauka*.
3. Python NumPy Documentation: https://numpy.org/doc/stable/

---

## 8. Appendix

### 8.1 Full Code Listing
*(Include the full Python code here if required.)*

### 8.2 Plots
*(Include convergence and 2D landscape plots here.)*