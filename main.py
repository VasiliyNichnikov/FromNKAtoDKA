from algorithmtransfer import AlgorithmTransfer
from graph import Graph
from vertex import Vertex


def create_graph_nka_1() -> Graph:
    point_entry = Vertex("1", (True, ["a"]))
    point_2 = Vertex("2", (True, ["a"]))
    point_3 = Vertex("3", (True, ["a", "b"]), end_vertex=True)

    g_nka = Graph(point_entry)
    g_nka.add_vertex((point_entry, ["a"]), (point_2, ["b"]))
    g_nka.add_vertex((point_entry, ["b"]), (point_3, None))
    g_nka.add_vertex((point_2, ["b"]), (point_3, None))
    return g_nka


def create_graph_nka_2() -> Graph:
    point_entry = Vertex("1", (True, ["a", "b"]))
    point_2 = Vertex("2")
    point_3 = Vertex("3")
    point_4 = Vertex("4", end_vertex=True)

    g_nka = Graph(point_entry)
    g_nka.add_vertex((point_entry, ["a"]), (point_2, None))
    g_nka.add_vertex((point_2, ["a", "b"]), (point_3, None))
    g_nka.add_vertex((point_3, ["a", "b"]), (point_4, None))
    return g_nka


def main() -> None:
    g_nka = create_graph_nka_1()
    al_transfer = AlgorithmTransfer(g_nka)
    g_dka = al_transfer.transfer_from_NKA_to_DKA()

    g_nka.output()
    print()
    g_dka.output()


if __name__ == '__main__':
    main()
