from typing import List, Tuple, Dict

from errors import NameRepeats, NotCorrectlyElements
from vertex import Vertex


class Graph:
    def __init__(self, root: Vertex | None = None) -> None:
        self.__root = root
        if self.__root is None:
            self.__root = Vertex("A")

    @property
    def root(self) -> Vertex:
        return self.__root

    # root list - список элементов для перехода из root в new
    # new list - список элементов для перехода из new в root
    @staticmethod
    def add_vertex(root: Tuple[Vertex, List[str] | None], new: Tuple[Vertex, List[str] | None]) -> None:
        root_vertex, root_transition_to = root
        next_vertex, new_transition_to = new
        if root_vertex == next_vertex:
            raise NameRepeats("Вершины одинаковы")

        if root_vertex is None or next_vertex is None:
            raise NotCorrectlyElements("Не верно передан элемент(ы)")

        if root_transition_to is not None:
            root_vertex.add_vertex(next_vertex, root_transition_to)

        if new_transition_to is not None:
            next_vertex.add_vertex(root_vertex, new_transition_to)

    def output(self) -> None:
        self.__output(self.__root, [])

    def __output(self, root: Vertex, traversed_vertexes: List[Vertex]) -> None:
        if root in traversed_vertexes:
            return
        else:
            traversed_vertexes.append(root)

        for connected_vertex in root.connected_vertexes:
            vertex = connected_vertex["vertex"]
            symbols = connected_vertex["symbols"]
            if isinstance(symbols, list):
                print(f"{root.name} -> ", end='')
                for symbol in symbols:
                    print(symbol, end=' ')
                print(f"-> {vertex.name}")
            else:
                print(f"{root.name} -> {symbols} -> {vertex.name}")
        for connected_vertex in root.connected_vertexes:
            vertex = connected_vertex["vertex"]
            self.__output(vertex, traversed_vertexes)

    def get_vertex_by_name(self, name: str) -> Vertex | None:
        return self.__search_vertex(name, self.__root, [])

    def __search_vertex(self, name: str, root: Vertex, traversed_vertexes: List[Vertex]) -> Vertex:
        if self.__root.name == name:
            return self.__root

        for element in root.connected_vertexes:
            vertex = element["vertex"]
            if vertex in traversed_vertexes:
                continue
            else:
                traversed_vertexes.append(vertex)

            if vertex.name == name:
                return vertex
            found_vertical = self.__search_vertex(name, vertex, traversed_vertexes)
            if found_vertical is not None:
                return found_vertical
