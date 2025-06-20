import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def show_graph (graph):
    pos = nx.spring_layout(graph, seed=14)
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
