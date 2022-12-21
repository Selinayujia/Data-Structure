import LinkedBinaryTree

l_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
r_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(3)
l_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(+, l_ch1, r_ch1)
r_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(2)
root = LinkedBinaryTree.LinkedBinaryTree.Node(*, l_ch2, r_ch2)

tree = LinkedBinaryTree.LinkedBinaryTree(root)

def eval_exp_tree(tree):
    pass