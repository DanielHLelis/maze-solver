import heapq
from typing import Callable, Tuple

from .maze import Maze, MazeSolution
from .heuristics import dijkstra_heuristic, euclidean_heuristic, manhattan_heuristic


def maze_bfirst_solve(
    maze: Maze,
    heuristic: Callable[[Maze, Tuple[int, int]], float] = manhattan_heuristic,
) -> MazeSolution:
    visited = [[False] * maze.width for _ in range(maze.height)]

    path = []
    steps = []
    parents = [[None] * maze.width for _ in range(maze.height)]

    pqueue = [(0, maze.start, None)]

    while pqueue:
        _, cur, par = heapq.heappop(pqueue)  # cost is g(x, y)

        if visited[cur[0]][cur[1]]:
            continue

        visited[cur[0]][cur[1]] = True
        parents[cur[0]][cur[1]] = par
        steps.append(cur)

        if cur == maze.end:
            break

        candidates = maze.candidate_moves(cur)

        for candidate in candidates:
            if visited[candidate[0]][candidate[1]]:
                continue
            f = heuristic(maze, candidate)
            heapq.heappush(pqueue, (f, candidate, cur))

    cur = maze.end
    if parents[cur[0]][cur[1]] is not None:
        while cur is not None:
            path.append(cur)
            cur = parents[cur[0]][cur[1]]

    path.reverse()

    return MazeSolution(maze, steps, path)


# Aliases
maze_bfirst_solve_euclidean = lambda maze: maze_bfirst_solve(maze, euclidean_heuristic)
maze_bfirst_solve_manhattan = lambda maze: maze_bfirst_solve(maze, manhattan_heuristic)
maze_bfirst_solve_dijkstra = lambda maze: maze_bfirst_solve(maze, dijkstra_heuristic)
maze_dijkstra_solve = maze_bfirst_solve_dijkstra
