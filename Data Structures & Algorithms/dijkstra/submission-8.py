class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}

        for u, v, w in edges:
            adj[u].append((w, v))

        print(adj)
        shortest = {}
        minHeap = [(0, src)]

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = cost

            for dist, neighbor in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(minHeap, (cost + dist, neighbor))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest