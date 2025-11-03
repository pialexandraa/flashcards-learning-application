#complete node class implementation w. pointers for sequential structures & hierarchical structures:
class Node:
    def __init__(self, data=None, next_node=None, previous_node=None, children_node=None, parent_node=None):
        self.data = data
        self.next = next_node #pointer to the next node in a linked list
        self.previous = previous_node
        self.children = children_node if children_node is not None else []
        self.parent = parent_node #pointer needed for a tree/graph structure

    #getter methods:
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def get_previous(self):
        return self.previous
        
    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    #setter methods:
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next_node):
        self.next = new_next_node

    def set_previous(self, new_previous_node):
        self.previous = new_previous_node

    def set_children(self, new_children_node):
        self.children = new_children_node

    def set_parent(self, new_parent_node):
        self.parent = new_parent_node

    #methods for printing lists and debugging:
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"<Node data={repr(self.data)}, next={self.next is not None}, previous={self.previous is not None}, children={len(self.children)}>"