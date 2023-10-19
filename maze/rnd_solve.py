from typing import Tuple, Optional, Any
from .maze import Maze, MazeSolution
from random import Random


def maze_rnd_solve(
    maze: Maze, seed: Optional[Any] = "insider_trading_do_bernardo"
) -> MazeSolution:
    """
    Solve a maze using a random search.
    """
    rng = Random(seed)

    visited = [[False] * maze.width for _ in range(maze.height)]

    heads = []
    steps = []
    path = []
    parents = [[None] * maze.width for _ in range(maze.height)]

    heads.append(maze.start)

    parents[maze.start[0]][maze.start[1]] = None
    visited[maze.start[0]][maze.start[1]] = True

    while heads:
        position = heads.pop(rng.randint(0, len(heads) - 1))
        steps.append(position)

        if position == maze.end:
            break

        candidates = maze.candidate_moves(position)

        for candidate in candidates:
            if visited[candidate[0]][candidate[1]]:
                continue

            visited[candidate[0]][candidate[1]] = True
            parents[candidate[0]][candidate[1]] = position
            heads.append(candidate)

    cur = maze.end
    if parents[cur[0]][cur[1]] is not None:
        while cur is not None:
            path.append(cur)
            cur = parents[cur[0]][cur[1]]

    path.reverse()

    return MazeSolution(maze, steps, path)


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
