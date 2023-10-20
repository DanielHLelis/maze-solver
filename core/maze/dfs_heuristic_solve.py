from typing import Tuple

from .maze import Maze, MazeSolution


def maze_dfs_heuristic_solve(maze: Maze, heuristic) -> MazeSolution:
    """
    Solve a maze using depth-first search with heuristic.
    """

    path = []
    steps = []
    visited = [[False] * maze.width for _ in range(maze.height)]

    def dfs_heuristic(candidate: Tuple[int, int]):   #adapta a função heurística para funcionar no sort
        return heuristic(maze.end, candidate)


    def dfs_heuristic_solve(maze: Maze, position: Tuple[int, int]):
        if not maze[position]:  #retorna false se bate num muro
            return False

        if visited[position[0]][position[1]]: #retorna false se já posição já visitada
            return False

        visited[position[0]][position[1]] = True #marca posição como já visitada
        steps.append(position)

        if position == maze.end: #indica o final do labirinto e retorna a posição final
            path.append(position)
            return True

        next_positions = maze.candidate_moves(position) #pega as posições possíveis
        next_positions = sorted(next_positions, key=dfs_heuristic)  #ordena as posições possíveis pela heurística

        for nl, nc in next_positions:
            if dfs_heuristic_solve(maze, (nl, nc)):
                path.append(position)
                return True

        return False

    dfs_heuristic_solve(maze, maze.start)
    path.reverse()
    return MazeSolution(maze, steps, path)


if __name__ == "__main__":
    print("This file is not meant to be run directly.")
