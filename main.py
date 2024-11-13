import networkx as nx
import matplotlib.pyplot as plt

def read_friends_file():
    friends_list = []
    with open("friends.txt", "r") as file:
        for line in file:
            line_parts = line.strip().split(" follows ")
            friends_list.append((line_parts[0], line_parts[1]))
    return friends_list

def create_graph(data):
    graph = nx.Graph(data)
    return graph

def plot_graph(graph):
    nx.draw(graph, with_labels=graph)
    plt.show()


def main():
    friends_list = read_friends_file()
    graph = create_graph(friends_list)
    plot_graph(graph)

main()