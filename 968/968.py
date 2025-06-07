from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 0: El nodo no está cubierto.
    # 1: El nodo tiene una cámara.
    # 2: El nodo está cubierto.
    def postorder_aux(self, node , num_cameras):
        if not node:
            return
        self.postorder_aux(node.left,num_cameras)
        self.postorder_aux(node.right,num_cameras)
        if not node.left and not node.right: # Caso en que el nodo es una hoja
            node.val = 0
            return
        elif not node.left and node.right: # Caso en que solo hay un hijo derecho
            if node.right.val == 1:
                node.val = 2
            elif node.right.val == 0:
                node.val = 1
                num_cameras.append(1)
            else:
                node.val = 0
            return
        elif not node.right and node.left: # Caso donde solo hay un hijo izquierdo
            if node.left.val == 1:
                node.val = 2
            elif node.left.val == 0:
                node.val = 1
                num_cameras.append(1)
            else:
                node.val = 0
            return
        else: # Caso donde hay dos hijos
            if node.left.val == 0 or node.right.val == 0:
                node.val = 1
                num_cameras.append(1)
            elif node.left.val == 1 or node.right.val == 1:
                node.val = 2
            else:
                node.val = 0


    def postorder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None
        """
        num_cameras = []
        self.postorder_aux(root , num_cameras)
        if root.val == 0:
            num_cameras.append(1)
        return len(num_cameras)
            
    def print_tree_by_levels(self, root):
            """
            Imprime el árbol por niveles (compatible con Python 2.x)
            """
            if not root:
                print("Árbol vacío")
                return

            queue = deque()
            queue.append(root)
            level = 0

            while queue:
                level_size = len(queue)
                print("Nivel {}: ".format(level)),
                for _ in range(level_size):
                    node = queue.popleft()
                    if node:
                        print(node.val),
                        queue.append(node.left)
                        queue.append(node.right)
                    else:
                        print("None"),
                print("")
                level += 1
                
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        resultado = self.postorder(root)
        self.print_tree_by_levels(root)
        return resultado

        