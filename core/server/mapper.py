from ..maze.maze import Maze, MazeSolution


def maze_to_dict(maze: Maze) -> dict:
    """
    Convert a maze to a dictionary.
    """
    return {
        "width": maze.width,
        "height": maze.height,
        "start": maze.start,
        "end": maze.end,
        "matrix": maze.matrix,
    }


def maze_solution_to_dict(maze_solution: MazeSolution) -> dict:
    """
    Convert a maze solution to a dictionary.
    """
    return {
        "maze": maze_to_dict(maze_solution.maze),
        "steps": maze_solution.steps,
        "path": maze_solution.path,
    }


def dict_to_maze(maze_dict: dict) -> Maze:
    """
    Convert a dictionary to a maze.
    """
    return Maze(maze_dict["matrix"], maze_dict["start"], maze_dict["end"])


def dict_to_maze_solution(maze_solution_dict: dict) -> MazeSolution:
    """
    Convert a dictionary to a maze solution.
    """
    return MazeSolution(
        dict_to_maze(maze_solution_dict["maze"])
        if "maze" in maze_solution_dict
        else None,
        maze_solution_dict["steps"],
        maze_solution_dict["path"],
    )
