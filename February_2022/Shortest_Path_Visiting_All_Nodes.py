class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n = len(graph)
        endingMask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        visited = set(queue)
        level = 0
        while queue:
            nextQueue = []
            for node, mask in queue:
                for neighbor in graph[node]:
                    nextMask = mask | (1 << neighbor)
                    if nextMask == endingMask:
                        return level + 1
                    if (neighbor, nextMask) not in visited:
                        visited.add((neighbor, nextMask))
                        nextQueue.append((neighbor, nextMask))
            level += 1
            queue = nextQueue