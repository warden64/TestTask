import threading
import collections
import GraphType


class Graph:
    type = GraphType.NOT_ORIENTED
    graph = {}
    lock = threading.Lock()

    def __init__(self, graph_type=GraphType.NOT_ORIENTED):
        self.type = graph_type

    def add_vertex(self, vertex):
        """
        Adds vertex to the graph.
        @type  vertex: vertex
        @param vertex: User defined type
        """
        self.lock.acquire()
        self.graph[vertex] = set()
        self.lock.release()

    def add_edge(self, edge):
        """
        Adds edge to the graph.
        @type  edge: tuple
        @param edge: Edge
        """
        vertex1, vertex2 = edge
        self.lock.acquire()
        self.graph[vertex1].add(vertex2)
        if self.type == GraphType.NOT_ORIENTED:
            self.graph[vertex2].add(vertex1)
        self.lock.release()

    def find_path(self, vertex1, vertex2):
        """
        Finds path between two vertexes.
        @type  vertex1: user object
        @param vertex1: First vertex

        @type  vertex2: user object
        @param vertex2: Second vertex

        @rtype:  boolean
        @return: Truth-value for node existence.
        """
        result = []
        self.lock.acquire()
        try:
            queue = collections.deque([(vertex1, [vertex1])])
            while queue:
                (vertex, path) = queue.popleft()
                for node in self.graph[vertex] - set(path):
                    if node == vertex2:
                        result = path + [node]
                    else:
                        queue.append((node, path + [node]))
        finally:
            self.lock.release()
        return result
