import LinkedBinaryTree

l_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
r_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(3)
l_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(2, l_ch1, r_ch1)
l_ch3 = LinkedBinaryTree.LinkedBinaryTree.Node(5)
r_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(6, l_ch3)
root = LinkedBinaryTree.LinkedBinaryTree.Node(4, l_ch2, r_ch2)

tree = LinkedBinaryTree.LinkedBinaryTree(root)

x = tree.height()
print(x)

def seq1():
    yield 1
    yield 2
    yield from seq2()
def seq2():
    yield 3
    yield 4
    
for elem in tree:
    print(elem)

for node in tree.breadth_first():
    print(node.data)    