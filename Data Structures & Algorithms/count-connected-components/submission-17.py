class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
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
        uf = UnionFind(n)

        res = n
        for n1, n2 in edges:
            res -= uf.union(n1, n2)

        return res