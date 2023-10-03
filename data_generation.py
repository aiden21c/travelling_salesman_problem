import csv
import random

# Number of cities
n = int(input("Enter the number of cities: "))
max = int(input("Enter the maximum distance between cities: "))

# Create a list of cities
cities = [f"City {i}" for i in range(n)]

# Create a distance matrix
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        distances[i][j] = distances[j][i] = random.randint(1, max)

# Write the distance matrix to a CSV file
with open("csv/distances.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([""] + cities)
    for i, row in enumerate(distances):
        writer.writerow([cities[i]] + row)
