from .maze import Maze, MazeSolution


def maze_dfs_solve(maze: Maze) -> MazeSolution:
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


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
