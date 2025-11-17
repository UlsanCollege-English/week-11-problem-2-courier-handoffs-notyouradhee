"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque

def bfs_path(graph, start, target):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.

    TODO (8 Steps):
    1) Read & Understand: what is "fewest handoffs" here?
    2) Re-phrase: say the goal in simple words.
    3) Identify I/O: inputs graph, s, t; output list or None.
    4) Break down: queue, visited, parent; loop until found.
    5) Pseudocode: write steps as comments above your code.
    6) Write code with deque.
    7) Debug with prints (locally).
    8) Optimize: state O(V+E) in README.
    """
    # FIX: Check for missing nodes FIRST.
    if start not in graph or target not in graph:
        return None
        
    # NOW, check if start == target.
    if start == target:
        return [start]

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        u = queue.popleft()
        if u == target:
            path = []
            while u is not None:
                path.append(u)
                u = parent[u]
            return path[::-1]
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    return None