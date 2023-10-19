from .maze import Maze, MazeSolution


def maze_bfs_solve(maze: Maze) -> MazeSolution:
    """
    Solve a maze using breadth-first search.
    """

    path = []
    steps = []

    parents = [[None] * maze.width for _ in range(maze.height)]
    visited = [[False] * maze.width for _ in range(maze.height)]

    queue = []
    queue.append(maze.start)

    while queue:
        cur = queue.pop(0)

        if not maze[cur]:
            continue

        if visited[cur[0]][cur[1]]:
            continue

        visited[cur[0]][cur[1]] = True
        steps.append(cur)

        if cur == maze.end:
            break

        next_positions = maze.candidate_moves(cur)

        for nl, nc in next_positions:
            if not visited[nl][nc]:
                parents[nl][nc] = cur
                queue.append((nl, nc))

    cur = maze.end
    if parents[cur[0]][cur[1]] is not None:
        while cur is not None:
            path.append(cur)
            cur = parents[cur[0]][cur[1]]

    path.reverse()

    return MazeSolution(maze, steps, path)


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
