import networkx as nx
import numpy as np
import itertools
from scipy.optimize import linear_sum_assignment

def create_graph(cities, distances):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            G.add_edge(i, j, weight=distances[i][j])
    return G

def minimum_weight_matching(G, maxcardinality=False):
    r"""Minimum weight matching of a graph.
    This is the solution to the Assignment Problem with the algorithm of Kuhn-Munkres.
    """
    import numpy as np
    from scipy.optimize import linear_sum_assignment

    edges = nx.edges(G)
    nodes = list(nx.nodes(G))
    
    # Create a mapping of nodes to integers
    node_to_int = {node: i for i, node in enumerate(nodes)}
    
    weights = nx.get_edge_attributes(G, 'weight')
    weight_matrix = np.zeros((len(nodes), len(nodes)))
    
    for edge in edges:
        # Use the mapping to index the weight_matrix
        weight_matrix[node_to_int[edge[0]], node_to_int[edge[1]]] = weights[edge]
        weight_matrix[node_to_int[edge[1]], node_to_int[edge[0]]] = weights[edge]
        
    row_ind, col_ind = linear_sum_assignment(weight_matrix)
    
    # Convert integers back to nodes
    return [(nodes[i], nodes[j]) for i, j in zip(row_ind, col_ind)]

def eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def christofides(cities, distances):
    # Create a graph from the distances
    G = create_graph(cities, distances)

    # Create a minimum spanning tree T of G
    T = nx.minimum_spanning_tree(G)

    # Let O be the set of vertices with odd degree in T
    O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

    # Create a subgraph induced by vertices from O
    subgraph_O = G.subgraph(O)

    # Find a minimum-weight perfect matching M in the induced subgraph given by the vertices from O
    M = minimum_weight_matching(subgraph_O)

    # Combine the edges of M and T to form a connected multigraph H in which each vertex has even degree
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    # Check if all vertices of H have even degree
    for v in H.nodes():
        if H.degree(v) % 2 != 0:
            print(f"Vertex {v} has odd degree")

    # Form an Eulerian circuit in H
    circuit = eulerian_circuit(H)

    # Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices (shortcutting)
    hamiltonian_circuit = []
    visited = set()
    
    for u,v in circuit:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
        if v not in visited:
            hamiltonian_circuit.append(v)
            visited.add(v)
            
    return hamiltonian_circuit

