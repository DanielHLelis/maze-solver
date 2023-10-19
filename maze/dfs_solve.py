from typing import Tuple

from .maze import Maze, MazeSolution


def maze_dfs_solve(maze: Maze) -> MazeSolution:
    """
    Solve a maze using depth-first search.
    """

    visited = [[False] * maze.width for _ in range(maze.height)]

    stack = []
    steps = []
    parent = {}
    
    def dfs_solve(maze: Maze, position: Tuple[int, int]):
        stack.append(position)
        parent[position] = None

        while stack:
            position = stack.pop()    
            steps.append(position)
            visited[position[0]][position[1]] = True

            candidates = [ _p for _p in reversed(maze.candidate_moves(position))
                    if maze[_p[0],_p[1]] and not visited[_p[0]][_p[1]]]

            for candidate in candidates:
                parent[candidate] = position
            stack.extend(candidates)

            if position == maze.end: 
                return position
    
    dfs_solve(maze, maze.start)
    
    def get_path():
        path = []
        position = maze.end
        while position != None: 
            path.append(position)
            position = parent[position]
        path.reverse()
        return path     

    return MazeSolution(maze, steps, get_path())


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
