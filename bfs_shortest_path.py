def bfs_shortest_path(graph, start, goal):
    queue = [[start]]
    explored = []
    if start ==goal:
        return start
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            explored.append(node)
            for neighbor in graph[node]:
                newpath = list(path)
                newpath.append(neighbor)
                if neighbor == goal:
                    return newpath
                queue.append(newpath)
    return ("No Path Found")