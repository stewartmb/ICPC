class BST:
        
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def is_valid_bst(self):
        def _validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return _validate(node.left, low, node.val) and _validate(node.right, node.val, high)
        return _validate(self.root)
    
    
def build_tree_from_list(tree, node_map=None):
    if not tree:
        return None
    bst = BST()
    bst.root = tree
    root = bst.root
    if node_map is not None:
        if root.left:
            node_map[root.left.val] = root
        if root.right:
            node_map[root.right.val] = root
    return bst

class Solution(object):
    def canMerge(self, trees):
        global global_node_map
        global_node_map = {}  # IMPORTANT: reset global map if reused
        global global_root_map
        global_root_map = {}
        
        list_bst = []
        for tree in trees:
            bst = build_tree_from_list(tree, global_node_map)
            global_root_map[bst.root.val] = bst.root
            list_bst.append(bst)
        n_not_merged = 0
        n = len(list_bst)
        while len(list_bst)>1:
            bst = list_bst.pop()
            if bst.root.val in global_node_map:
                node = global_node_map[bst.root.val]
                del global_node_map[bst.root.val]
                if not bst.is_valid_bst():
                    return None
                if node.left and node.left.val == bst.root.val:
                    node.left = bst.root

                if node.right and node.right.val == bst.root.val:
                    node.right = bst.root             
            else:
                list_bst.insert(0, bst)
                n_not_merged = n_not_merged + 1
                if n_not_merged > 1:
                    return None

        if len(list_bst) > 1:
            return None
        final_bst = list_bst[0]
        if not final_bst.is_valid_bst():
            return None
        return final_bst.root
    
    
