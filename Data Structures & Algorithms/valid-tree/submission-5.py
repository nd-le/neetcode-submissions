class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        print(adj)

        visit = set()

        def dfs(node, prevNode):
            if node in visit:
                return False

            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == prevNode:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visit) == n