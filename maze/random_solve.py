from typing import Tuple
from .maze import Maze, MazeSolution
from random import shuffle

def maze_rnd_solve(maze: Maze) -> MazeSolution:
    """
    Solve a maze using a random search.
    """

    visited = [[False] * maze.width for _ in range(maze.height)]

    head_list = []
    steps = []
    parent = {}
    
    def rnd_solve(maze: Maze, position: Tuple[int, int]):
        head_list.append(position)
        parent[position] = None
        visited[position[0]][position[1]] = True
        
        while head_list:
            shuffle(head_list)
            position = head_list.pop(0)
            steps.append(position)

            candidates = [ _p for _p in reversed(maze.candidate_moves(position))
                if maze[_p[0],_p[1]] and not visited[_p[0]][_p[1]]]

            for candidate in candidates:
                parent[candidate] = position
                visited[candidate[0]][candidate[1]] = True
            head_list.extend(candidates)

            if position == maze.end: 
                return position
    
    rnd_solve(maze, maze.start)
    
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
