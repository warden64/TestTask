import graph as gr
from graph import GraphType


class UserType:
    user_field = ''

    def __init__(self, u_field):
        self.user_field = u_field

    def tostring(self):
        return self.user_field


def path_to_str(path):
    result = []
    if len(path) > 0:
        for i in path:
            result.append(i.tostring())
    else:
        result = "Path doesn't exist"
    return str(result)


def main():
    a = UserType('aa')
    b = UserType('bb')
    c = UserType('cc')
    d = UserType('dd')
    e = UserType('ee')
    f = UserType('ff')
    g = UserType('gg')

    """
     a -> b -> e -> f
          V
     c -> d    g
    """

    graph_type = GraphType.NOT_ORIENTED

    graph = gr.Graph(graph_type)
    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_vertex(d)
    graph.add_vertex(e)
    graph.add_vertex(f)
    graph.add_vertex(g)
    graph.add_edge((a, b))
    graph.add_edge((c, d))
    graph.add_edge((b, d))
    graph.add_edge((b, e))
    graph.add_edge((e, f))
    print('a -> a: ' + path_to_str(graph.find_path(a, a)))
    print('a -> e: ' + path_to_str(graph.find_path(a, e)))
    print('a -> d: ' + path_to_str(graph.find_path(a, d)))
    print('a -> c: ' + path_to_str(graph.find_path(a, c)))
    print('a -> f: ' + path_to_str(graph.find_path(a, f)))
    print('f -> c: ' + path_to_str(graph.find_path(f, c)))
    print('f -> g: ' + path_to_str(graph.find_path(f, g)))


if __name__ == "__main__":
    main()
