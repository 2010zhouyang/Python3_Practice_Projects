import collections


class TreeNode(object):
    def __init__(self, val):
        """

        :param val: an integer for this node's value
        """
        self.val = val
        self.left = None
        self.right = None


def print_root_to_leaf_path(root):
    Q = collections.deque([(root, [str(root.val)])])
    while Q:
        node, path = Q.popleft()
        if not node.left and not node.right:
            print(' -> '.join(path))
        if node.left:
            Q.append((node.left, path + [str(node.left.val)]))
        if node.right:
            Q.append((node.right, path + [str(node.right.val)]))


n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n0.left, n0.right = n1, n2
n1.left = n3
n2.left = n4
print_root_to_leaf_path(n0)
