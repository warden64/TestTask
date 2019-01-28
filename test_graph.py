import graph
from graph import GraphType


class UserType:
    a = ''

    def __init__(self, a):
        self.a = a


graph_not_oriented = graph.Graph(GraphType.NOT_ORIENTED)
graph_oriented = graph.Graph(GraphType.ORIENTED)


test_data = ['a', 'b', 'c', 'd', 'e', 'g']


def test_add_vertexes():
    for item in test_data:
        graph_oriented.add_vertex(item)
        graph_not_oriented.add_vertex(item)


def test_add_edges_oriented():
    """
     a -> b -> c <-> e <- d
     g
    """
    graph_oriented.add_edge(('a', 'b'))
    graph_oriented.add_edge(('b', 'c'))
    graph_oriented.add_edge(('c', 'e'))
    graph_oriented.add_edge(('d', 'e'))


def test_get_path_oriented():
    assert graph_oriented.find_path('a', 'e') == ['a', 'b', 'c', 'e']
    assert graph_oriented.find_path('a', 'd') == []
    assert graph_oriented.find_path('d', 'e') == ['d', 'e']


def test_add_edges_not_oriented():
    """
     a <-> b     g
     c <-> e <-> d
    """
    graph_not_oriented.add_edge(('a', 'b'))
    graph_not_oriented.add_edge(('c', 'e'))
    graph_not_oriented.add_edge(('d', 'e'))


def test_get_path_not_oriented():
    assert graph_not_oriented.find_path('a', 'g') == []
    assert graph_not_oriented.find_path('c', 'd') == ['c', 'e', 'd']
    assert graph_not_oriented.find_path('d', 'a') == []
