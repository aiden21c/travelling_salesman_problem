import itertools

def hka(G, n):
    # Initialize the memoization table g with a dictionary
    g = {}

    # Initialize the path table to store the optimal path
    path = {}

    # Initialize g for subsets of size 2
    for k in range(1, n):
        g[(frozenset([k]), k)] = G[0][k]
        path[(frozenset([k]), k)] = [0, k]

    # Dynamic loop
    for s in range(2, n):
        for subset in itertools.combinations(range(1, n), s):
            S = frozenset(subset)
            for k in S:
                min_dist = float('inf')
                min_m = None
                for m in S:
                    if m != k:
                        # Calculate the minimum distance
                        dist = g[(S - frozenset([k]), m)] + G[m][k]
                        if dist < min_dist:
                            min_dist = dist
                            min_m = m
                g[(S, k)] = min_dist
                path[(S, k)] = path[(S - frozenset([k]), min_m)] + [k]

    # Calculate the final optimal tour distance
    opt = float('inf')
    final_k = None
    for k in range(1, n):
        dist = g[(frozenset(range(1, n)), k)] + G[k][0]
        if dist < opt:
            opt = dist
            final_k = k

    # Retrieve the optimal tour path
    optimal_path = path[(frozenset(range(1, n)), final_k)] + [0]

    return opt, optimal_path

