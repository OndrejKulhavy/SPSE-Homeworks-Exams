import matplotlib.pyplot as plt
import time


def create_line_graph(input_sizes_list, execution_times_list, graph_titles):
    for input_sizes, execution_times, title in zip(input_sizes_list, execution_times_list, graph_titles):
        plt.plot(input_sizes, execution_times, marker='o', linestyle='-', label=title)

    plt.title('Time Complexity Analysis')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()
