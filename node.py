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


apple = Node("apple")
banana = Node("banana")
orange = Node("orange")

apple.next_node = banana
banana.next_node = orange

# Print out all nodes
current_node = apple

while current_node is not None:
    print(current_node.value)
    current_node = current_node.next_node

