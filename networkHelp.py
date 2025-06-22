import networkx as nx
import matplotlib.pyplot as plt
import random
import time

#def show_graph (graph):
#    is_planar, embedding = nx.check_planarity(graph)
#    if not is_planar:
#        pos = nx.spring_layout(graph, seed=17)
#        # pos = nx.spring_layout(graph)
#        nx.draw(graph, pos, with_labels=True)
#    else:
#        nx.planar_layout(graph)
#        nx.draw(graph, embedding, with_labels=True)
#    plt.show()

#def show_graph(graph):
#    is_planar, embedding = nx.check_planarity(graph)
#    if not is_planar:
#        raise ValueError("The graph is not planar and cannot be drawn without edge crossings.")
#
#    # Use a layout that guarantees planarity
#    pos = nx.planar_layout(graph)
#    nx.draw(graph, pos, with_labels=True)
#    plt.show()

#def show_graph (graph):
#    is_planar, embedding = nx.check_planarity(graph)
#    pos = nx.spring_layout(graph, seed=17)
#    # pos = nx.spring_layout(graph)
#    nx.draw(graph, pos, with_labels=True)
#    plt.show()



def show_graph(graph):
    is_planar, embedding = nx.check_planarity(graph)
    if not is_planar:
        raise ValueError("Graph is not planar")

    # Start with a planar layout
    pos_planar = nx.planar_layout(graph)

    # Use the planar layout as the initial position for spring_layout
    pos = nx.spring_layout(graph, pos=pos_planar, seed=17, iterations=50)

    nx.draw(graph, pos, with_labels=True)
    plt.show()


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        delta_time = t2 - t1
        if type(result) == tuple:
            result = (*result, delta_time)
        else:
            result = (result, delta_time)
        #with open("Time.csv", "a") as time_register:
        #    time_register.write(f"node_num,edge_num,{t2 - t1:.6f}\n")
        #print(f"Execution time: {t2 - t1:.6f} seconds")
        return result
    return wrapper
