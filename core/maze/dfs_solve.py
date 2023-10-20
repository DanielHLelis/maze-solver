from typing import Callable, Tuple, Optional

from .maze import Maze, MazeSolution
from .heuristics import (
    euclidean_heuristic,
    manhattan_heuristic,
    vertical_heuristic,
    horizontal_heuristic,
)


def maze_dfs_solve(
    maze: Maze, heuristic: Optional[Callable[[Maze, Tuple[int, int]], float]] = None
) -> MazeSolution:
    """
    Solve a maze using depth-first search.
    """

    visited = [[False] * maze.width for _ in range(maze.height)]

    path = []
    steps = []
    parents = [[None] * maze.width for _ in range(maze.height)]

    stack = [maze.start]

    while stack:
        position = stack.pop()

        visited[position[0]][position[1]] = True
        steps.append(position)

        if position == maze.end:
            break

        candidates = maze.candidate_moves(position)

        if heuristic is not None:
            candidates = sorted(candidates, key=lambda x: heuristic(maze, x))

        for candidate in candidates:
            if visited[candidate[0]][candidate[1]]:
                continue

            parents[candidate[0]][candidate[1]] = position
            stack.append(candidate)

    cur = maze.end
    if parents[cur[0]][cur[1]] is not None:
        while cur is not None:
            path.append(cur)
            cur = parents[cur[0]][cur[1]]

    path.reverse()

    return MazeSolution(maze, steps, path)


maze_dfs_solve_euclidean = lambda maze: maze_dfs_solve(maze, euclidean_heuristic)
maze_dfs_solve_manhattan = lambda maze: maze_dfs_solve(maze, manhattan_heuristic)
maze_dfs_solve_vertical = lambda maze: maze_dfs_solve(maze, vertical_heuristic)
maze_dfs_solve_horizontal = lambda maze: maze_dfs_solve(maze, horizontal_heuristic)


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
