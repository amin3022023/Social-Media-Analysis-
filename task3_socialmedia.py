import networkx as nx
import gzip

# Task 1: Download the social network dataset (email-Eu-core.txt.gz) manually and place it in your working directory

# Task 2: Load the network using NetworkX library and print the highest and lowest node degrees
def load_and_print_network(email_Eu_core):
    # Load the network from the file
    with gzip.open(email_Eu_core, 'rt') as f:
        G = nx.read_edgelist(f)

    # Print the highest and lowest node degrees
    degrees = dict(G.degree())
    max_degree_node = max(degrees, key=degrees.get)
    min_degree_node = min(degrees, key=degrees.get)
    print("Highest node degree:", max_degree_node, degrees[max_degree_node])
    print("Lowest node degree:", min_degree_node, degrees[min_degree_node])

    return G

# Task 3: Perform Depth-First-Search (DFS) traversal starting from user:0
def dfs_traversal(graph, start_node):
    traversal_order = list(nx.dfs_edges(graph, source=start_node))
    return traversal_order

if __name__ == "__main__":
    # Define the filename of the dataset
    filename = "email_Eu_core.txt.gz"

    # Task 2: Load the network and print highest and lowest node degrees
    network = load_and_print_network(filename)

    # Task 3: Perform Depth-First-Search (DFS) traversal starting from user:0
    start_node = '0'
    traversal_order = dfs_traversal(network, start_node)
    print("DFS traversal order starting from node", start_node, ":", traversal_order)
