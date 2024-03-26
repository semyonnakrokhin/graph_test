class Vertex:
    ID = 1

    def __init__(self):
        self._id = self.ID
        Vertex.ID += 1

        self.marked = False
        self._links = []

    @property
    def links(self):
        return self._links

    def add_link(self, link: "Link") -> None:
        if link not in self._links:
            self._links.append(link)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self._id}>"


class Link:
    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1, self._v2 = v1, v2

        self._v1.add_link(link=self)
        self._v2.add_link(link=self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self._v1} - {self._v2}>"


class Graph:
    def __init__(self):
        self._links: list[Link] = []
        self._vertices: list[Vertex] = []

    def __add_vertex(self, vertex: Vertex) -> None:
        if vertex not in self._vertices:
            self._vertices.append(vertex)

    def add_link(self, link: Link) -> None:
        check_link_in_graph = tuple(
            filter(
                lambda x: (
                    (x.v1 == link.v1 and x.v2 == link.v2)
                    or (x.v1 == link.v2 and x.v2 == link.v1)
                ),
                self._links,
            )
        )

        if not check_link_in_graph:
            self._links.append(link)
            self.__add_vertex(vertex=link.v1)
            self.__add_vertex(vertex=link.v2)

    def output_graph_to_screen(self):
        for v in self._vertices:
            output = f"{v} ({'+' if v.marked else '-'}): {v.links}"
            print(output)


def create_graph() -> tuple[Graph, Vertex]:
    """
    Function where you inputl all vertices and links
    :return:
    first object: Graph
    second_object: Top Vertex
    """

    # vert1 = Vertex()
    # vert2 = Vertex()
    # vert3 = Vertex()
    # vert4 = Vertex()
    # vert5 = Vertex()
    #
    # link1 = Link(v1=vert1, v2=vert2)
    # link2 = Link(v1=vert1, v2=vert3)
    # link3 = Link(v1=vert2, v2=vert3)
    # link4 = Link(v1=vert2, v2=vert4)
    # link5 = Link(v1=vert2, v2=vert5)
    # link6 = Link(v1=vert3, v2=vert5)
    #
    # graph = Graph()
    #
    # graph.add_link(link=link1)
    # graph.add_link(link=link2)
    # graph.add_link(link=link3)
    # graph.add_link(link=link4)
    # graph.add_link(link=link5)
    # graph.add_link(link=link6)
    #
    # return graph, vert1

    graph = Graph()
    vertices = [Vertex() for _ in range(20)]

    links = [
        Link(vertices[0], vertices[1]),
        Link(vertices[0], vertices[2]),
        Link(vertices[1], vertices[3]),
        Link(vertices[1], vertices[4]),
        Link(vertices[2], vertices[5]),
        Link(vertices[2], vertices[6]),
        Link(vertices[3], vertices[7]),
        Link(vertices[3], vertices[8]),
        Link(vertices[4], vertices[9]),
        Link(vertices[4], vertices[10]),
        Link(vertices[5], vertices[11]),
        Link(vertices[5], vertices[12]),
        Link(vertices[6], vertices[13]),
        Link(vertices[6], vertices[14]),
        Link(vertices[7], vertices[15]),
        Link(vertices[7], vertices[16]),
        Link(vertices[8], vertices[17]),
        Link(vertices[8], vertices[18]),
        Link(vertices[9], vertices[19]),
        Link(vertices[10], vertices[19]),
    ]

    for link in links:
        graph.add_link(link)

    return graph, vertices[0]
