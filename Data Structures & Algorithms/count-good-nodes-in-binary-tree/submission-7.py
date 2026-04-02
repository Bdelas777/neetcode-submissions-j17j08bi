class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxVal: int) -> int:
            if not node:  # Caso base: si el nodo es nulo, no hay nodos buenos en esta rama.
                return 0

            # Un nodo es bueno si su valor es mayor o igual al máximo valor encontrado hasta ahora.
            res = 1 if node.val >= maxVal else 0

            # Actualizamos el máximo valor para las ramas izquierda y derecha.
            maxVal = max(maxVal, node.val)

            # Llamadas recursivas a las ramas izquierda y derecha.
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            # Devolvemos el conteo total de nodos buenos en esta rama.
            return res

        # Llamada inicial al DFS, comenzando desde la raíz y con el valor de la raíz como el máximo inicial.
        return dfs(root, root.val)
