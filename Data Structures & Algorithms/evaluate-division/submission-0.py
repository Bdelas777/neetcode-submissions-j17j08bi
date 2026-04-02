from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # 1️⃣ Construir el grafo
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        # 2️⃣ DFS para encontrar el resultado
        def dfs(src, dst, visited):
            if src == dst:
                return 1.0
            
            visited.add(src)

            for neighbor in graph[src]:
                if neighbor in visited:
                    continue
                res = dfs(neighbor, dst, visited)
                if res != -1:
                    return res * graph[src][neighbor]
            
            return -1

        # 3️⃣ Resolver queries
        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(a, b, set()))
        
        return results