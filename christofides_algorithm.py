import networkx as nx
from networkx.algorithms import matching

def christofides_tsp(cities, distances):
    # Create an empty graph and add cities as nodes
    G = nx.Graph()
    G.add_nodes_from(cities)
    
    # Add edges with distances as edge weights
    for i, city in enumerate(cities):
        for j, distance in enumerate(distances[i]):
            G.add_edge(city, cities[j], weight=distance)

    # Find a minimum spanning tree T of G
    T = nx.minimum_spanning_tree(G, weight='weight')

    # Let O be the set of vertices with odd degree in T
    O = [v for v, d in T.degree() if d % 2 == 1]

    # Find a minimum weight perfect matching M in the induced subgraph given by the vertices from O
    M = matching.min_weight_matching(G.subgraph(O))

    # Combine the edges of M and T to form a connected multigraph H in which each vertex has even degree
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    # Form an Eulerian circuit in H
    circuit = list(nx.eulerian_circuit(H))

    # Make the circuit into a Hamiltonian circuit by skipping repeated nodes (shortcutting)
    path = []
    visited = set()
    for u, v in circuit:
        if not u in visited:
            path.append(u)
            visited.add(u)
        if not v in visited:
            path.append(v)
            visited.add(v)

    # Add the starting city to the end of the path to form a complete circuit
    path.append(path[0])

    # Calculate the total cost of the path
    cost = sum(G[path[i-1]][path[i]]['weight'] for i in range(1, len(path)))

    return path, cost