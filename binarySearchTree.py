class Node():
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild =  None
        self.parent = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            return self._insert(self.root,data)

    def _insert(self,curr_node,data):
        if data < curr_node.data and curr_node.leftChild != None:
            return self._insert(curr_node.leftChild, data)
        elif data > curr_node.data and curr_node.rightChild != None:
            return self._insert(curr_node.rightChild,data)
        elif data < curr_node.data:
            curr_node.leftChild = Node(data)
            curr_node.leftChild.parent = curr_node
        elif data > curr_node.data:
            curr_node.rightChild = Node(data)
            curr_node.rightChild.parent = curr_node
        else:
            print ("value already exists")

    # SEARCH
    def search(self,data):
        if self.root == None:
            return print("tree is empty")
        else:
            return self._search(self.root,data)

    def _search(self,curr_node,data):
        if data < curr_node.data and curr_node.leftChild != None:
            return self._search(curr_node.leftChild, data)
        elif data > curr_node.data and curr_node.rightChild != None:
            return self._search(curr_node.rightChild,data)
        elif data == curr_node.data:
            return print(data,'is present')
        else:
            print ("value does not exists")

    # HEIGHT
    def height(self):
        height = 0
        if self.root != None:
            return self._height(self.root,height)
        else:
            return "there is no root node, no height"

    def _height(self,curr_node,curr_height):
        if curr_node == None:
            return curr_height
        leftHeight  = self._height(curr_node.leftChild,curr_height+1)
        rightHeight = self._height(curr_node.rightChild,curr_height+1)
        return max(leftHeight,rightHeight)

    # Find
    # SEARCH
    def find(self,data):
        if self.root == None:
            return print("tree is empty")
        else:
            return self._find(self.root,data)

    def _find(self,curr_node,data):
        if data < curr_node.data and curr_node.leftChild != None:
            return self._find(curr_node.leftChild, data)
        elif data > curr_node.data and curr_node.rightChild != None:
            return self._find(curr_node.rightChild,data)



    # DISPLAY
    def display(self):
        if self.root == None:
            print("Tree has no values yet")
        else:
            return self._display(self.root)

    def _display(self,curr_node):
        if curr_node != None:
            self._display(curr_node.leftChild)
            print(curr_node.data)
            self._display(curr_node.rightChild)



t1 = BinarySearchTree()

t1.insert(1)
t1.insert(2)
t1.insert(0)
t1.insert(-1)
t1.insert(-5)
t1.insert(3)
t1.insert(5)
t1.insert(6)
t1.insert(7)

t1.display()

print("##########################")
t1.search(18)
print("##########################")
print(t1.height())
