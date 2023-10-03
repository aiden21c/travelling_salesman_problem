def minimum_spanning_tree(G):
    visited = set()
    node = next(iter(G))
    mst_edges = []

    def visit(node):
        visited.add(node)
        edges = sorted((G[node][v], node, v) for v in G[node] if v not in visited)
        for weight, u, v in edges:
            mst_edges.append((u, v, weight))
            visit(v)

    visit(node)

    return mst_edges

def eulerian_circuit(mst_edges):
    H = {}
    for u, v, _ in mst_edges:
        if u not in H:
            H[u] = []
        if v not in H:
            H[v] = []
        H[u].append(v)
        H[v].append(u)

    # Find an Eulerian circuit in H
    circuit = []
    stack = [next(iter(H))]
    while stack:
        node = stack[-1]
        if H[node]:
            stack.append(H[node].pop())
        else:
            circuit.append(stack.pop())

    # Shortcutting: remove repeated nodes in the Eulerian circuit, keeping only the first occurrence
    visited = set()
    shortcut_circuit = [node for node in circuit if not (node in visited or visited.add(node))]

    return shortcut_circuit

def double_tree(cities, distances):
    G = {cities[i]: {cities[j]: distances[i][j] for j in range(len(cities))} for i in range(len(cities))}
    T = minimum_spanning_tree(G)
    mst_edges = T + T
    euler_circuit = eulerian_circuit(mst_edges)

    # Add the starting city to the end of the circuit to complete the return trip
    euler_circuit.append(euler_circuit[0])

    # Calculate the total cost of the circuit
    total_cost = sum(G[u][v] for u, v in zip(euler_circuit[:-1], euler_circuit[1:]))

    return total_cost, euler_circuit