import networkx as nx
import matplotlib.pyplot as plt

# T1: Load the network and heuristics
def load_network(users_edgelist.txt)):
    G = nx.Graph()
    with open(users_edgelist.txt), 'r') as file:
        for line in file:
            user1, user2, cost = line.strip().split()
            G.add_edge(user1, user2, cost=float(cost))
    return G

def load_heuristics(users_edgelist.txt):
    heuristics = {}
    with open(users_edgelist.txt, 'r') as file:
        for line in file:
            user, cost = line.strip().split()
            heuristics[user] = float(cost)
    return heuristics

# T2: Complete the Greedy Search algorithm implementation
def greedy_search(graph, heuristics, start, goal):
    path = [start]
    total_cost = 0

    current_node = start
    while current_node != goal:
        neighbors = graph[current_node]
        min_cost = float('inf')
        next_node = None

        for neighbor in neighbors:
            if neighbor not in path:
                cost_to_go = heuristics[neighbor]
                if cost_to_go < min_cost:
                    min_cost = cost_to_go
                    next_node = neighbor

        if next_node is None:
            print("No path found.")
            return None

        path.append(next_node)
        total_cost += min_cost
        current_node = next_node

    print("Greedy path found:", path)
    print("Total cost:", total_cost)
    return path

# Task 3: Visualize the network and highlight the greedy path
def visualize_network(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)

    # Highlight the greedy path
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)

    plt.title('Social Media Network')
    plt.show()


