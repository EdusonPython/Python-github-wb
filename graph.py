import collections
# Тестируем структуру данных "графы"

# Поиск графа в глубину DFS
graph_1 = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['D', 'E'], 'D': [], 'E': []
}

# Использование рекурсии

visited = set()


def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)

        for child in graph[root]:
            dfs(visited, graph, child)

    return visited


# Поиск графа в ширину BFS

def bfs(graph, root):
    visit = set()
    deque = collections.deque([root])

    while deque:
        node = deque.popleft()
        visit.add(node)

        for item in graph[node]:
            if item not in visit:
                deque.append(item)

    return visit
