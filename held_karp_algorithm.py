import csv
import itertools

def read_distances(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        cities = next(reader)[1:]
        distances = []
        for row in reader:
            distances.append([int(x) for x in row[1:]])
        return cities, distances

def held_karp(graph):
    n = len(graph)
    memo = {}  # Memoization dictionary to store computed subproblem results

    # Initialize memoization for base case: {({1}, 1): weight}
    for k in range(1, n):
        memo[(frozenset([k]), k)] = graph[k][0]

    for subset_size in range(2, n+1):
        subsets = itertools.combinations(range(1, n), subset_size)
        for subset in subsets:
            subset = frozenset(subset)
            for k in subset:
                if k == 0:
                    continue
                # Compute the minimum cost for the current subset and ending at city k
                memo[(subset, k)] = min(
                    graph[i][k] + memo[(subset - {k}, i)] for i in subset if i != k
                )

    # Calculate the final result by considering all cities in the subset and returning to the starting city
    full_set = frozenset(range(1, n))
    min_tour_cost = min(
        graph[k][0] + memo[(full_set - {k}, k)] for k in range(1, n)
    )

    return min_tour_cost


# Example usage
cities, distances = read_distances("csv/distances.csv")
result = held_karp(distances)
print("Minimum TSP cost:", result)
