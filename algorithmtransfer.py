from typing import List, Dict

from errors import ErrorWhenCreatingDKA
from graph import Graph
from vertex import Vertex


class AlgorithmTransfer:
    def __init__(self, graph_nka: Graph) -> None:
        self.__graph_nka = graph_nka

    def transfer_from_NKA_to_DKA(self) -> Graph:
        data: List[Dict] = []
        queue: List[str] = [self.__graph_nka.root.name]
        passed: List[str] = []

        while len(queue) > 0:
            name_a: str = queue.pop(0)
            passed.append(name_a)
            transitions = self.__vertex_filter(name_a)
            for key in transitions.keys():
                name_b, end_vertex_b = transitions[key]
                data.append(
                    {"name_a": name_a,
                     "name_b": name_b,
                     "symbols": key,
                     "end_vertex_b": end_vertex_b}
                )
                if name_b not in passed:
                    queue.append(name_b)
        return self.__create_dka(data)

    def __create_dka(self, data: List[Dict]) -> Graph:
        root_name = self.__graph_nka.root.name
        root = Vertex(root_name)
        graph_dka = Graph(root)

        for info in data:
            name_a = info["name_a"]
            name_b = info["name_b"]
            symbols = info["symbols"]
            end_vertex_b = info["end_vertex_b"]

            vertex_a = graph_dka.get_vertex_by_name(name_a)
            vertex_b = graph_dka.get_vertex_by_name(name_b)

            if name_a != name_b:
                if vertex_b is None:
                    vertex_b = Vertex(name_b, end_vertex=end_vertex_b)

                if vertex_a is not None:
                    vertex_a.add_vertex(vertex_b, symbols)
            else:
                selected_vertex = vertex_a
                if vertex_a is None:
                    selected_vertex = vertex_b
                elif vertex_a is None and vertex_b is None:
                    raise ErrorWhenCreatingDKA("Ошибка, нет опорного элемента")
                selected_vertex.change_transition_yourself(True, symbols)
        return graph_dka

    def __vertex_filter(self, elements: str) -> Dict:
        transitions: Dict = {}
        for element in elements:
            found_vertex: Vertex = self.__graph_nka.get_vertex_by_name(element)
            connected_vertexes = found_vertex.connected_vertexes
            for vertex in connected_vertexes:
                value: Vertex = vertex["vertex"]
                symbols: List[str] = vertex["symbols"]
                for symbol in symbols:
                    if symbol not in transitions:
                        transitions[symbol] = [value.name, value.end_vertex]
                    elif symbol in transitions and value.name not in transitions[symbol][0]:
                        transitions[symbol][0] += value.name
        return transitions
