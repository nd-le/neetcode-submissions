class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != parent[cur]:
            parent[cur] = parent[parent[cur]]
            cur = parent[cur]
        return cur

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        
        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [-1] * n

        def find(node):
            cur = node
            while parent[cur] >= 0:
                cur = parent[cur]

            return cur 

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0
            size1, size2 = parent[p1] * -1, parent[p2] * -1
            if size1 > size2:
                parent[p2] = p1
                parent[p1] -= 1
            elif size2 > size1:
                parent[p1] = p2
                parent[p2] -= 1
            else:
                parent[p2] = p1
                parent[p1] -= 1
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res