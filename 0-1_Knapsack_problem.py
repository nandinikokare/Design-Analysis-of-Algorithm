def knapsack(weights, values, capacity):
    n = len(values)
    # Create a 2D DP table to store the maximum value for each capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in a bottom-up manner
    for i in range(1, n + 1):  # Loop through each item
        for w in range(1, capacity + 1):  # Loop through each capacity
            if weights[i - 1] <= w:
                # Include item i-1 and check if it results in higher value
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude item i-1
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # Maximum value for the full capacity

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = knapsack(weights, values, capacity)
print(f"Maximum value in the knapsack: {max_value}")


"""
In the 0-1 Knapsack Problem, we have a set of items, each with a weight and a value, and a knapsack with a weight capacity. The goal is to maximize the total value of items placed in the knapsack without exceeding the weight capacity. Unlike the fractional knapsack, here we can't take fractions of items—each item can either be included entirely or excluded (0-1).


Dynamic Programming : Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems, solving each subproblem only once, and storing their solutions for future use.
