from node import Node

class LinkedList(Node):
    """
    LinkedList(Node)
    
    The description of a linked list.
    
    Attributes
    ----------
    head: Node
        The first node in a linked list.
    """
    def __init__(self, head: Node):
        if type(head) is Node:
            self.head = head
        else:
            self.head = None
       
    def stringify(self) -> str:
        """
        stringify()
        
        Stringifies all the elements in a linked list.
        
        Returns
        -------
        str
            The stringified linked list.
        """
        current_node = self.head
        string_list = ""
        
        while current_node is not None:
            string_list += current_node.value
            string_list += " -> "
            current_node = current_node.next_node
        
        string_list = string_list[:-4]
        return string_list
    
    def insert_front(self, new_node: Node) -> Node | None:
        """
        insert_front(new_node)
        
        Inserts a given node at the start of a linked list.
        
        Parameters
        ----------
        new_node: Node
            The new node to insert.
        
        Returns
        -------
        Node
            If node has been inserted.
        None
            If there was an error and node has not been inserted.
        """
        if type(new_node) is not Node:
            print("Element to insert must be a Node")
            return None
            
        new_node.next_node = self.head
        self.head = new_node
        
        return new_node
    
    def insert_end(self, new_node: Node) -> Node | None:
        """
        insert_end(new_node)
        
        Inserts a given node at the end of a linked list.

        Parameters
        ----------
        new_node: Node
            The new node to insert.
        
        Returns
        -------
        Node
            If node has been inserted.
        None
            If there was an error and node has not been inserted.
        """
        if type(new_node) is not Node:
            print("Element to insert must be a Node")
            return None
            
        current_node = self.head
        
        while current_node.next_node is not None:
            current_node = current_node.next_node
        
        tail = current_node
        tail.next_node = new_node
        
        return new_node
    
    def insert_after(self, new_node: Node, node: Node) -> Node | None:
        """
        insert_after(new_node, node)
        
        Inserts a given node after another node.

        Parameters
        ----------
        new_node: Node
            The new node to insert.
        node: Node
            The node to insert the new node after.
        
        Returns
        -------
        Node
            If node has been inserted.
        None
            If there was an error and node has not been inserted.
        """
        if type(new_node) is not Node or type(node) is not Node:
            print("Element to insert must be a Node")
            return None
            
        current_node = self.head
        
        # Check if node exists in linked list
        while current_node is not None:
            if current_node == node:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return new_node
            
            current_node = current_node.next_node
        
        print("Node not found")
        return None
            
    def insert_before(self, new_node: Node, node: Node) -> Node | None:
        """
        insert_before(new_node, node)
        
        Inserts a given node before another node.

        Parameters
        ----------
        new_node: Node
            The new node to insert.
        node: Node
            The node to insert the new node before.
        
        Returns
        -------
        Node
            If node has been inserted.
        None
            If there was an error and node has not been inserted.
        """
        if type(new_node) is not Node or type(node) is not Node:
            print("Element to insert must be a Node")
            return None
            
        current_node = self.head
        prev_node = None
        
        # Check if node exists in linked list
        while current_node is not None:
            if current_node == node:
                new_node.next_node = current_node
                
                if prev_node is None:                
                    self.head = new_node
                else:
                    prev_node.next_node = new_node
                    
                return new_node
 
            prev_node = current_node
            current_node = current_node.next_node
        
        print("Node not found")
        return None
    
    def delete_node(self, node: Node) -> Node | None:
        """
        delete_node(node)
        
        Deletes a given node from a linked list.
        
        Parameters
        ----------
        node: Node
            The node to delete.
        
        Returns
        -------
        Node
            If node has been deleted.
        None
            If there was an error and node has not been deleted.
        """
        if type(node) is not Node:
            print("Element to insert must be a Node")
            return None
            
        current_node = self.head
        prev_node = None
        
        # Check if node exists in linked list
        while current_node is not None:
            if current_node == node:
                if prev_node is None:
                    self.head = current_node.next_node
                    return node

                prev_node.next_node = current_node.next_node
                return node
            
            prev_node = current_node
            current_node = current_node.next_node
        
        print("Node not found")
        return None
    
    def find_value(self, to_find) -> Node | None:
        """
        find_value(to_find)
        
        Returns the node with the given value.  
        
        Parameters
        ----------
        to_find
            The value to find.
        
        Returns
        -------
        Node
            The Node with the given value.
        None
            If there was an error and a node with the given value was not found.
        """
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == to_find:
                return current_node
            
            current_node = current_node.next_node
        
        print("Value {} not found in linked list".format(to_find))
        return None
    
    def find_nth(self, n: int) -> Node | None:
        """
        find_nth(n)
        
        Returns the node in the given position.
        
        Parameters
        ----------
        n: int
            nth value to find.
        
        Returns
        -------
        Node
            The Node in the given position.
        None
            If there was an error and a node with the given position was not found.
        """
        if type(n) is not int:
            print("Nth position specified must be of type int")
            return None
        
        if n < 0 or n >= self.length():
            print("Nth position must be within boundaries > 0 and < length of linked list")
            return None
        
        count = -1
        current_node = self.head
        
        while current_node is not None:
            count += 1
            
            if count == n:
                return current_node
            
            current_node = current_node.next_node
        
    
    def length(self) -> int:
        """
        length()
        
        Returns the length of the linked list.
        
        Returns
        -------
        int
            The length of the linked list.
        """
        length = 0
        current_node = self.head
        
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        
        return length                
