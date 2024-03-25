import matplotlib.pyplot as plt
from algorithms.basic import boat_brute_force
from algorithms.heuristic import boat_heuristic
import time
from algorithms.monte_carlo import boat_monte_carlo
from algorithms.ship import Ship
from algorithms.utils import create_line_graph


def monte_carlo():
    start_time = time.time_ns()
    s = Ship([73, 85, 81, 8, 65, 85, 85, 69, 76, 24])
    boat_monte_carlo(s)
    end_time = time.time_ns()
    result = end_time - start_time
    print(result)


def brute_force():
    start_time = time.time()
    boat_brute_force(73, 85, 81, 54, 48, 44, 99, 34, 75, 23)
    end_time = time.time()
    result = end_time - start_time
    print(result)


def heuristic():
    start_time = time.time_ns()
    boat_heuristic(73, 85, 81, 43, 53, 89, 89, 89, 87, 65)
    end_time = time.time_ns()
    result = end_time - start_time
    print(result)


def generate_graph():
    input_sizes_list = [
        [5, 6, 7, 8, 9, 10],
        [5, 6, 7, 8, 9, 10],
        [5, 6, 7, 8, 9, 10]
    ]

    execution_times_list = [
        [0.001005411148071289, 0.00200653076171875, 0.021004438400268555, 0.14102745056152344, 1.8999998569488525,
         17.73934245109558],
        [0.0099995, 0.0070011, 0.0029984, 0.0009987, 0.23499774932861328, 0.0169986],
        [0, 0.0010006, 0.0009999, 0.0009993, 0.0009996, 0.0010007]
    ]

    graph_titles = ['Brute Force', 'Heuristic', 'Monte Carlo']

    create_line_graph(input_sizes_list, execution_times_list, graph_titles)


def main():
    # brute_force()
    # heuristic()
    # monte_carlo()
    generate_graph()


if __name__ == "__main__":
    main()
