def bfs_connected_component(graph,start):
    queue = [start]
    explored = []
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            for neighbour in graph[node]:
                queue.append(neighbour)
    return(explored)