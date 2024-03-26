from graph_utills import Vertex, create_graph


def mark_vertices(start_vertex: Vertex):
    start_vertex.marked = True
    for link in start_vertex.links:
        neighbor_vertex: Vertex = link.v2 if link.v1 is start_vertex else link.v1
        if not neighbor_vertex.marked:
            mark_vertices(start_vertex=neighbor_vertex)


if __name__ == "__main__":
    g, vert1 = create_graph()

    g.output_graph_to_screen()

    mark_vertices(start_vertex=vert1)

    print()
    g.output_graph_to_screen()
