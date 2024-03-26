import networkx as nx
import matplotlib.pyplot as plt
def load_and_print_network(facebook_combined):
    # Load the network from the file
    Dataset = nx.read_edgelist(facebook_combined)

    # Print the number of nodes and edges
    num_nodes = Dataset.number_of_nodes()
    num_edges = Dataset.number_of_edges()
    print("Number of nodes:", num_nodes)
    print("Number of edges:", num_edges)

    # Return the loaded graph
    return Dataset

# T3: he label of the node with the highest degree in the network
def find_node_with_highest_degree(graph):
    degrees = dict(graph.degree())
    max_degree_node = max(degrees, key=degrees.get)
    return max_degree_node, degrees[max_degree_node]

# T4: Compute the average degree of all the nodes in the network
def compute_average_degree(graph):
    degrees = [degree for node, degree in graph.degree()]
    average_degree = sum(degrees) / len(degrees)
    return average_degree

# T5: Visualize the network
def visualize_network(graph):
    nx.draw(graph, with_labels=True, node_size=50, node_color='skyblue', edge_color='gray')
    plt.title("Facebook Social Network")
    plt.show()

if __name__ == "__main__":

    filename = "facebook_combined.txt"

    # Load and print the network
    network = load_and_print_network(filename)

    # Task 3: Find the label of the node with the highest degree in the network
    max_degree_node, max_degree = find_node_with_highest_degree(network)
    print("Node with the highest degree:", max_degree_node)
    print("Degree:", max_degree)

    # T4: Compute the average degree of all the nodes in the network
    average_degree = compute_average_degree(network)
    print("Average degree of all nodes:", average_degree)

    # T5: Visualize the network
    visualize_network(network)
