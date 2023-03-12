import unittest
import sys

sys.path.append("../")

from node import Node
from linked_list import LinkedList

def setup_linked_list():
    stations = LinkedList(Node("Village"))
    stations.insert_end(Node("City"))
    stations.insert_end(Node("Beach"))
    
    return stations

class TestLinkedList(unittest.TestCase):
    def test_stringify(self):
        self.assertEqual(setup_linked_list().stringify(), "Village -> City -> Beach")
    
    def test_insert_front(self):
       stations = setup_linked_list()
       stations.insert_front(Node("Airport"))
       
       self.assertEqual(stations.stringify(), "Airport -> Village -> City -> Beach")
    
    def test_insert_end(self):
        stations = setup_linked_list()
        stations.insert_end(Node("Airport"))
        
        self.assertEqual(stations.stringify(), "Village -> City -> Beach -> Airport")
    
    def test_insert_after(self):
        stations = setup_linked_list()
        village = stations.head
        stations.insert_after(Node("Airport"), village)
        
        self.assertEqual(stations.stringify(), "Village -> Airport -> City -> Beach")
    
    def test_insert_before(self):
        stations = setup_linked_list()
        village = stations.head
        stations.insert_before(Node("Airport"), village)
        
        self.assertEqual(stations.stringify(), "Airport -> Village -> City -> Beach")
    
    def test_delete_node(self):
        stations = setup_linked_list()
        village = stations.head
        stations.delete_node(village)
        
        self.assertEqual(stations.stringify(), "City -> Beach")
    
    def test_find_value(self):
        stations = setup_linked_list()
        city = stations.head.next_node
        
        self.assertEqual(stations.find_value("City"), city)
    
    def test_find_nth(self):
        stations = setup_linked_list()
        city = stations.head.next_node
        
        self.assertEqual(stations.find_nth(1), city)
    
    def test_length(self):
        stations = setup_linked_list()
        
        self.assertEqual(stations.length(), 3)
