class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Total value of the knapsack
    for item in items:
        if capacity >= item.weight:
            # If item can be fully added
            capacity -= item.weight
            total_value += item.value
            print(f"Taking full item with weight {item.weight} and value {item.value}")
        else:
            # Take only fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            print(f"Taking {fraction*100}% of item with weight {item.weight} and value {item.value}")
            break  # Knapsack is full after this item fraction

    return total_value

# Example usage
items = [
    Item(60, 10),  # Value = 60, Weight = 10
    Item(100, 20), # Value = 100, Weight = 20
    Item(120, 30)  # Value = 120, Weight = 30
]
capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in the knapsack: {max_value}")





"""Knapsack Problem : In the Fractional Knapsack Problem, the goal is to maximize the total value of items in a knapsack with a fixed weight capacity, where fractions of items can be included.
A greedy algorithm works well here by choosing items based on the highest value-to-weight ratio.


The greedy approach is an algorithmic strategy that makes a series of choices, each of which seems the best at the moment (locally optimal), with the hope that this will lead to a globally optimal solution.
Greedy algorithms are often used for optimization problems where the goal is to maximize or minimize a certain value."""
