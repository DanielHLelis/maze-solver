import sys
import json
from typing import List, Tuple, Optional


class Cell:
    row: int
    col: int
    visited: bool
    walls: List[bool]

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]  # Up, Right, Down, Left


class Maze:
    start: Tuple[int, int]
    end: Tuple[int, int]
    matrix: List[List[bool]]

    def __init__(
        self,
        matrix: List[List[bool]],
        start: Tuple[int, int] = None,
        end: Tuple[int, int] = None,
        force_start: bool = False,
        force_end: bool = False,
    ):
        self.matrix = matrix
        self.start = tuple(start)
        self.end = tuple(end)

        if force_start:
            self[start] = True

        if force_end:
            self.end = self.find_end()

    @property
    def height(self) -> int:
        return len(self.matrix)

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    def candidate_moves(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Return a list of valid moves from the given position.
        """
        next_positions = (
            (position[0], position[1] + 1),
            (position[0], position[1] - 1),
            (position[0] + 1, position[1]),
            (position[0] - 1, position[1]),
        )

        return tuple(pos for pos in next_positions if self[pos])

    def check_bounds(self, index: Tuple[int, int]) -> bool:
        return 0 <= index[0] < len(self.matrix) and 0 <= index[1] < len(self.matrix[0])

    def __getitem__(self, index: Tuple[int, int]) -> bool:
        if not self.check_bounds(index):
            return False

        return self.matrix[index[0]][index[1]]

    def __setitem__(self, index: Tuple[int, int], value: bool):
        self.matrix[index[0]][index[1]] = value

    def __str__(self):
        cell_mapper = lambda b: " " if b else "█"
        rows = ["".join(map(cell_mapper, row)) for row in self.matrix]
        return "\n".join(rows)


class MazeSolution:
    maze: Optional[Maze]
    steps: List[Tuple[int, int]]
    path: List[Tuple[int, int]]

    def __init__(
        self,
        maze: Optional[Maze],
        steps: List[Tuple[int, int]],
        path: List[Tuple[int, int]],
    ):
        self.maze = maze
        self.steps = steps
        self.path = path

    def __str__(self) -> str:
        if self.maze is None:
            return f"Steps Length: {len(self.steps)}\nPath Length: {len(self.path)}"

        maze_strs = str(self.maze).split("\n")
        for pos in self.steps:
            maze_strs[pos[0]] = (
                maze_strs[pos[0]][: pos[1]] + "*" + maze_strs[pos[0]][pos[1] + 1 :]
            )

        for pos in self.path:
            maze_strs[pos[0]] = (
                maze_strs[pos[0]][: pos[1]] + "o" + maze_strs[pos[0]][pos[1] + 1 :]
            )

        maze_strs[self.maze.start[0]] = (
            maze_strs[self.maze.start[0]][: self.maze.start[1]]
            + "S"
            + maze_strs[self.maze.start[0]][self.maze.start[1] + 1 :]
        )

        maze_strs[self.maze.end[0]] = (
            maze_strs[self.maze.end[0]][: self.maze.end[1]]
            + "E"
            + maze_strs[self.maze.end[0]][self.maze.end[1] + 1 :]
        )

        return "\n".join(maze_strs)


def load_maze_json(path: str) -> Maze:
    with open(path) as f:
        maze_json = json.load(f)

    matrix = maze_json["matrix"]
    start = tuple(maze_json["start"])
    end = tuple(maze_json["end"])

    return Maze(matrix, start, end)


def dump_maze_json(maze: Maze, path: str):
    maze_json = {
        "matrix": maze.matrix,
        "start": list(maze.start),
        "end": list(maze.end),
        "width": maze.width,
        "height": maze.height,
    }

    with open(path, "w") as f:
        json.dump(maze_json, f)


def load_maze_solution_json(path: str) -> MazeSolution:
    with open(path) as f:
        maze_solution_json = json.load(f)

    steps = maze_solution_json["steps"]
    path = maze_solution_json["path"]

    return MazeSolution(None, steps, path)


def dump_maze_solution_json(maze_solution: MazeSolution, path: str):
    maze_solution_json = {
        "steps": maze_solution.steps,
        "path": maze_solution.path,
    }

    with open(path, "w") as f:
        json.dump(maze_solution_json, f)


if __name__ == "__main__":
    file_name = sys.argv[1]
    maze = load_maze_json(file_name)
    print(maze)
