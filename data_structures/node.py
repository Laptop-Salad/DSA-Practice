class Node:
    """
    Node

    Represents a node data structure.

    Properties:
    - value (any type) => A value for the current node
    - next_node (Node/None) => A pointer to the next node
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
