class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        # self.child_node = None

    def add_child(self, child):
        self.children.append(child)

    # def add_child_node(self,child_node):
    #     self.child_node = child_node

class Tree:
    def __init__(self):
        self.root = None

    def add_root(self, root_node):
        self.root = root_node

    def traverse_tree(self, node):
        #print(node.data)
        for child in node.children:
            self.traverse_tree(child)
    
    def find(self, node, to_find):
        if node.data == to_find:
            return node.children
        else:
            for child in node.children:
                result = self.find(child, to_find)
                if result:
                    return result
        return None
    def find_node(self, node, to_find):
        if node.data == to_find:
            return node
        else:
            for child in node.children:
                result = self.find(child, to_find)
                if result:
                    return result
        return None