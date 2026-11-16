from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start, goal):
    q = deque([[start]])
    visited = set()

    while q:
        path = q.popleft()
        node = path[-1]

        if node == goal:
            print("Path:", path)
            return

        if node not in visited:
            visited.add(node)

            for i in graph[node]:
                q.append(path + [i])

    print("No path")


bfs('A', 'F')