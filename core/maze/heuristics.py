from typing import Callable, Tuple

from .maze import Maze


def dijkstra_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return 0


def euclidean_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return ((maze.end[0] - current[0]) ** 2 + (maze.end[1] - current[1]) ** 2) ** (0.5)


def manhattan_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return abs(maze.end[0] - current[0]) + abs(maze.end[1] - current[1])


def horizontal_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return abs(maze.end[1] - current[1])


def vertical_heuristic(maze: Maze, current: Tuple[int, int]) -> float:
    return abs(maze.end[0] - current[0])
