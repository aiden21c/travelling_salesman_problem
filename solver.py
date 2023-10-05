import csv
import time
import held_karp_algorithm
import christofides_algorithm
import double_tree_algorithm

def read_distances(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        cities = next(reader)[1:]
        distances = []
        for row in reader:
            distances.append([int(x) for x in row[1:]])
        return cities, distances

cities, distances = read_distances("csv/distances.csv")

algorithm = int(input("Which algorithm do you want to use?\n\t1: Held-Karp Algorithm\n\t2: Christofides Algorithm\n\t3. Double Tree Algorithm\n"))

start_time = time.time()
if algorithm == 1:
    result, path = held_karp_algorithm.hka(distances, len(cities))
elif algorithm == 2:
    path, result = christofides_algorithm.christofides_tsp(list(range(len(cities))), distances)
elif algorithm == 3:
    result, path = double_tree_algorithm.double_tree(list(range(len(cities))), distances)
execution_time = time.time() - start_time 

print("Minimum TSP cost:", result)
print("Optimal tour path:", path)
print(f"Execution Time: {execution_time} seconds.")

