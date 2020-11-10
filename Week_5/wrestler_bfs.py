
import sys
# Bryan Rodriguez-Andrade
# CS 325 F2020
# Homework 5, Problem 5
# base code below referenced from:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# https://www.youtube.com/watch?v=-uR7BSfNJko


class Vertex:
    """Vertex class to be used as nodes for the Graph class
    """

    def __init__(self, wrestler):

        self.name = wrestler
        self.neighbors = list()
        self.distance = 9999
        self.color = 'black'
        self.type = ''

    def add_neighbor(self, v):

        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    """The graph class that the BFS will run on
    """
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    def bfs(self, vertex):
        """Runs the breadth first search algorithm on the passed vertex

        Args:
            vertex : the vertext to be explored
        """

        q = list()
        vert_distance = 0

        for v in vertex.neighbors:
            self.vertices[v].distance = vert_distance + 1
            self.vertices[v].type = 'Heel'
            q.append(v)

        while len(q) > 0:

            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'
            for v in node_u.neighbors:
                node_v = self.vertices[v]

                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

                    if node_v.distance % 2 == 0:
                        node_v.type = 'Babyface'
                    else:
                        node_v.type = 'Heel'

                    if node_v.type == node_u.type:
                        print("Impossible")
                        quit()

        for v in self.vertices:
            if self.vertices[v].color == 'black':
                self.bfs(self.vertices[v])

    def printResult(self):
        """iterates through the graph and appends temporary array to be used for file printing
        """
        print("Yes Possible")
        babyfaces = 'Babyfaces: '
        heels = 'Heels: '
        temp_array1 = []
        temp_array2 = []

        for v in self.vertices:
            if self.vertices[v].type == "Babyface":
                temp_array1.append(self.vertices[v].name)
        temp_array1.sort()
        for wrestler in temp_array1:
            babyfaces += wrestler + ' '

        for v in self.vertices:
            if self.vertices[v].type == "Heel":
                temp_array2.append(self.vertices[v].name)
        temp_array2.sort()
        for heel in temp_array2:
            heels += heel + ' '

        print(babyfaces)
        print(heels)

# file handling
sample_input = input("Filename: ")
with open(sample_input, 'r') as infile:

    inputs = infile.read().splitlines()
    number_of_wrestlers = int(inputs[0])
    number_of_rivalries = int(inputs[number_of_wrestlers + 1])
    rivalry_graph = Graph()

    for i in range(1, number_of_wrestlers + 1):
        rivalry_graph.add_vertex(Vertex(inputs[i]))

    for j in range(number_of_wrestlers + 2, number_of_wrestlers + number_of_rivalries + 2):
        wrestler_pairs = inputs[j].split()
        rivalry_graph.add_edge(wrestler_pairs[0], wrestler_pairs[1])

    rivalry_graph.bfs(rivalry_graph.vertices[inputs[1]])
    rivalry_graph.printResult()
