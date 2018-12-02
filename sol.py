import numpy as np
import math
import re


def get_file_input_graph_adjucency_list():
    with open('input.txt', 'r', encoding='utf-8') as f:
        arr_len = int(f.readline())
        data = f.read()
        adjucency_arr = [int(i) for i in re.findall(r"[\d]+", data)[0:arr_len]]
        nodes_count = adjucency_arr[0] - 1
        graph_edges = np.array([[math.inf for _ in range(nodes_count - 1)] for _ in range(nodes_count - 1)])
        for i in range(nodes_count - 1):
            ratio = 0
            for node in range(int((adjucency_arr[i + 1] - adjucency_arr[i]) / 2)):
                graph_edges[i][adjucency_arr[adjucency_arr[i] - 1 + ratio] - 1] = \
                    adjucency_arr[adjucency_arr[i] + ratio]
                graph_edges[adjucency_arr[adjucency_arr[i] - 1 + ratio] - 1][i] = \
                    adjucency_arr[adjucency_arr[i] + ratio]
                ratio += 2
        return graph_edges


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[math.inf for _ in range(vertices)]
                      for _ in range(vertices)]

    def printMST(self, parent):
        with open("output.txt", "w", encoding="utf-8") as f:
            summary = 0
            for i in range(1, self.V):
                res = str(i + 1) + " " + str(parent[i] + 1)
                f.write(res + "\n")
                summary += self.graph[i][parent[i]]
            f.write(str(int(summary)))


    # Функция для нахождения вершины с наименьшим весом к ней
    # из тех, которые еще не были выбраны
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minWeight(self, weight, already_set_in_MST):
        min = math.inf

        for v in range(self.V):
            if weight[v] < min and already_set_in_MST[v] == False:
                min = weight[v]
                min_node_index = v

        return min_node_index

    # Функция построения и отрисовки остова для графа
    # Используются матрицы смежности
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        # значения веса, используемые для выбора минимального веса
        # weight values used to pick minimum weight edge
        weight = [math.inf] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make weigth 0 so that this vertex is picked as first vertex
        weight[0] = 0
        already_set_in_MST = [False] * self.V

        parent[0] = -1  # First node is always the root of MST

        for node in range(self.V):
            # Берем наименьший вес от вершины к оставшемуся множеству вершин,
            # которые еще не обработаны
            # u всегда равна источнику на первой итерации
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minWeight(weight, already_set_in_MST)

            # Кладем это минимальный вес (как бы ребро) в остов
            # Put the minimum distance vertex in
            # the shortest path tree
            already_set_in_MST[u] = True

            # Обновляем значения веса смежных вершин
            # выбранной вершины только если текущий вес
            # больше чем новый вес и вершины еще нет в остове
            #
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] имеет ребро если его вес < inf
                # already_set_in_MST[v] false для невключенных в остов вершин
                # Обновляем weight только если graph[u][v] меньше чем key[v]
                # Как раз здесь идет проверка на цикл
                #
                # graph[u][v] is non zero only for adjacent vertices of m
                # already_set_in_MST[v] is false for vertices not yet included in MST
                # Update the weight only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] < math.inf and already_set_in_MST[v] == False and weight[v] > self.graph[u][v]:
                    weight[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)


graph_edges = get_file_input_graph_adjucency_list()
g = Graph(len(graph_edges))
g.graph = graph_edges

g.primMST()
