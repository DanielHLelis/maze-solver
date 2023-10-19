from typing import Tuple

from .maze import Maze, MazeSolution


def maze_bhfs_solve(maze: Maze, heuristic) -> MazeSolution:
    """
    Solve a maze using breadth-first search.
    """

    path = []
    steps = []

    parents = [[None] * maze.width for _ in range(maze.height)]
    visited = [[False] * maze.width for _ in range(maze.height)]

    queue = []
    queue.append(maze.start)

    def bhfs_heuristic(candidate: Tuple[int, int]):   #adapta a função heurística para funcionar no sort
        return heuristic(maze.end, candidate)

    def bhfs_solve(maze: Maze,queue: [], cur: Tuple[int, int]):

        if not maze[cur]:
            return False

        if visited[cur[0]][cur[1]]:
            return False

        visited[cur[0]][cur[1]] = True
        steps.append(cur)

        if cur == maze.end:
            return True
        
        next_positions = maze.candidate_moves(cur)
        next_positions = sorted(next_positions, key=bhfs_heuristic)  #ordena as novas posições possíveis pela heurística

        next_best = bhfs_heuristic(next_positions[0])

        if(len(queue)>0):
            while(bhfs_heuristic(queue[0])<next_best):
                cur1 = queue.pop(0)
                if bhfs_solve(maze,queue, cur1):
                    path.append(cur)
                    return True
        
        for nl, nc in next_positions:
            if not visited[nl][nc]:
                parents[nl][nc] = cur
                queue.append((nl, nc))

        queue = sorted(queue, key=bhfs_heuristic)  #ordena as novas posições possíveis pela heurística

        while(len(queue)>0):
            cur1 = queue.pop(0)
            if bhfs_solve(maze,queue, cur1):
                path.append(cur)
                return True

        return False
    
    bhfs_solve(maze,queue, maze.start)
    path.reverse()
    return MazeSolution(maze, steps, path)


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
