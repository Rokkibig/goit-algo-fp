import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neigh, w in graph[node].items():
            new_dist = dist + w
            if new_dist < distances[neigh]:
                distances[neigh] = new_dist
                heapq.heappush(pq, (new_dist, neigh))
    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(dijkstra(graph, 'A'))
