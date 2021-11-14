from typing import List, Tuple, Dict

from errors import VertexNotPassed


class Vertex(object):
    def __init__(self, name: str,
                 transition_into_yourself: Tuple[bool, List[str] | None] = (False, None),
                 end_vertex: bool = False) -> None:
        self.__name = name
        self.__connected_vertexes: List[Dict] = []
        self.__end_vertex = end_vertex

        self.__is_transition_yourself = transition_into_yourself[0]
        if self.__is_transition_yourself \
                and transition_into_yourself[1] is not None \
                and len(transition_into_yourself[1]) > 0:
            self.add_vertex(self, transition_into_yourself[1])

    @property
    def name(self) -> str:
        return self.__name

    @property
    def connected_vertexes(self) -> List[Dict]:
        return self.__connected_vertexes

    @property
    def end_vertex(self) -> bool:
        return self.__end_vertex

    @property
    def is_transition_yourself(self) -> bool:
        return self.__is_transition_yourself

    def change_transition_yourself(self, is_transition: bool, symbols: List[str]) -> None:
        self.__is_transition_yourself = is_transition
        if self.__is_transition_yourself and symbols is not None and len(symbols) > 0:
            self.add_vertex(self, symbols)

    def add_vertex(self, vertex, symbols: List[str]) -> None:
        if not isinstance(vertex, Vertex):
            raise VertexNotPassed(f"Данная вершина не является объектом типа {type(Vertex)}")

        new_vertex: Dict[str] = {"symbols": symbols,
                                 "vertex": vertex}
        for connected_vertex in self.__connected_vertexes:
            if connected_vertex == new_vertex:
                return
        self.__connected_vertexes.append(new_vertex)
