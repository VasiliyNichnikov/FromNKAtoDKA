class VertexException(Exception):
    pass


class GraphException(Exception):
    pass


class AlgorithmException(Exception):
    pass


class VertexNotPassed(VertexException):
    pass


class NameRepeats(GraphException):
    pass


class NotFoundVertex(GraphException):
    pass


class NotCorrectlyElements(GraphException):
    pass


class ErrorWhenCreatingDKA(AlgorithmException):
    pass
