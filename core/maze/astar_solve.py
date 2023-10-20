import heapq
from typing import Callable, Tuple

from .maze import Maze, MazeSolution


def dijkstra_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return 0


def euclidian_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return ((maze.end[0] - current[0]) ** 2 + (maze.end[1] - current[1]) ** 2) ** (0.5)


def manhattan_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return abs(maze.end[0] - current[0]) + abs(maze.end[1] - current[1])


def maze_astar_solve(
    maze: Maze,
    heuristic: Callable[[Maze, Tuple[int, int]], float] = manhattan_heuristic,
) -> MazeSolution:
    visited = [[False] * maze.width for _ in range(maze.height)]

    path = []
    steps = []
    parents = [[None] * maze.width for _ in range(maze.height)]

    pqueue = [(0, maze.start, None)]

    while pqueue:
        cost, cur, par = heapq.heappop(pqueue)  # cost is g(x, y)

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
            # f = g + h
            new_cost = cost + 1 + heuristic(maze, candidate)
            heapq.heappush(pqueue, (new_cost, candidate, cur))

    cur = maze.end
    if parents[cur[0]][cur[1]] is not None:
        while cur is not None:
            path.append(cur)
            cur = parents[cur[0]][cur[1]]

    path.reverse()

    return MazeSolution(maze, steps, path)


# Aliases
maze_astar_solve_euclidian = lambda maze: maze_astar_solve(maze, euclidian_heuristic)
maze_astar_solve_manhattan = lambda maze: maze_astar_solve(maze, manhattan_heuristic)
maze_astar_solve_dijkstra = lambda maze: maze_astar_solve(maze, dijkstra_heuristic)
maze_dijkstra_solve = maze_astar_solve_dijkstra
