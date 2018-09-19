from collections import defaultdict
from sys import maxsize as maxint
from copy import deepcopy


def get_file_input_graph_adjucency_list():
    adjucency_list = defaultdict(list)
    print(adjucency_list[0])
    with open('input.txt', 'r', encoding='utf-8') as f:
        n = int(f.readline())
        for i in range(1, n + 1):
            list_for_node = f.readline().split()
            list_for_node.remove('0')
            list_for_node = [int(x) for x in list_for_node]
            k = 0
            ready_edges_set_for_node = set()
            while k != len(list_for_node):
                ready_edges_set_for_node.add((list_for_node[k], list_for_node[k + 1]))
                k += 2
            adjucency_list[i] = sorted(ready_edges_set_for_node, key=lambda x: x[1])
    return adjucency_list


def get_input_graph_adjucency_list():
    adjucency_list = defaultdict(list)
    n = int(input())
    for i in range(1, n + 1):
        list_for_node = input().split()
        list_for_node.remove('0')
        list_for_node = [int(x) for x in list_for_node]
        k = 0
        ready_edges_set_for_node = set()
        while k != len(list_for_node):
            ready_edges_set_for_node.add((list_for_node[k], list_for_node[k + 1]))
            k += 2
        adjucency_list[i] = sorted(ready_edges_set_for_node, key=lambda x: x[1])
    return adjucency_list


def find_cycle(graph):
    colors = {node: "WHITE" for node in graph.keys()}
    start = list(graph.keys())[0]
    colors[start] = "GRAY"
    stack = [(None, start)]  # store edge, but at this point we have not visited one
    while stack:
        (prev, node) = stack.pop()  # get stored edge
        for neighbor in graph[node]:
            if neighbor[0] == prev:
                pass  # don't travel back along the same edge we came from
            elif colors[neighbor[0]] == "GRAY":
                return True
            else:  # can't be anything else than WHITE...
                colors[neighbor[0]] = "GRAY"
                stack.append((node, neighbor[0])) # push edge on stack
    return False


def get_min_span(adjucency_list):
    span = defaultdict(list)
    while len(span) < len(adjucency_list):
        span_copy = deepcopy(span)
        min_edge = get_edge_with_min_weight(adjucency_list)
        span_copy = _add_edge_to_span(span_copy, min_edge, False)
        if find_cycle(span_copy) is False:
            span = deepcopy(span_copy)
        adjucency_list = _delete_edge_from_graph(adjucency_list, min_edge)
    return span


def _add_edge_to_span(span, edge, second_time_here):
    if edge[0] not in span:
        span[edge[0]] = [(edge[1], edge[2])]
    else:
        span[edge[0]].append((edge[1], edge[2]))
    if not second_time_here:
        second_time_here = True
        sim_edge = (edge[1], edge[0], edge[2])
        span = _add_edge_to_span(span, sim_edge, second_time_here)
    return span


def _delete_edge_from_graph(span, edge):
    span[edge[0]].remove((edge[1], edge[2]))
    span[edge[1]].remove((edge[0], edge[2]))
    return span


def get_edge_with_min_weight(adjucency_list):
    min_edge = (0, 0, maxint)
    for node in adjucency_list:
        edges = adjucency_list[node]
        if len(edges) > 0:
            minimum = min(edges, key=lambda x: x[1])
            if minimum[1] <= min_edge[2]:
                min_edge = (node, minimum[0], minimum[1])
            else:
                continue
    return min_edge


def print_span(span):
    res_span = []
    sum_weight = 0
    for node in span:
        while len(span[node]) != 0:
            elem = span[node][0]
            sum_weight += elem[1]
            res_span.append(str(node) + " " + str(elem[0]))
            span = _delete_edge_from_graph(span, (node, elem[0], elem[1]))
    print(sum_weight)
    for elem in res_span:
        print(elem)


adj_graph_list = get_file_input_graph_adjucency_list()
adj_span_list = get_min_span(adj_graph_list)
#print_span(adj_span_list)
