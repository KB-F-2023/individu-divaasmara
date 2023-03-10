import heapq


def astar(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    parent = {}

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_node == end:
            path = []
            curr = end
            while curr != start:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return (curr_dist, list(reversed(path)))

        if curr_dist > dist[curr_node]:
            continue

        for neighbor, distance in graph[curr_node].items():
            tentative_dist = curr_dist + distance
            heuristic = abs(ord(neighbor) - ord(end))
            if tentative_dist + heuristic < dist[neighbor]:
                dist[neighbor] = tentative_dist + heuristic
                heapq.heappush(pq, (dist[neighbor], neighbor))
                parent[neighbor] = curr_node

    return float('inf')


graph = {
    'S': {'A': 6, 'B': 5, 'C': 10},
    'A': {'E': 6},
    'B': {'E': 6, 'D': 7},
    'C': {'D': 6},
    'D': {'F': 6},
    'E': {'F': 4},
    'F': {'G': 3},
    'G': {0}
}

shortest_route, path = astar(graph, 'C', 'G')
print(path)
print(shortest_route)

# reference : Dijkstra’s Shortest Path Algorithm
# A* algorithm is a variant of Dijkstra's algorithm that uses a heuristic function
# to guide the search towards the goal node, potentially resulting in a more efficient search.
