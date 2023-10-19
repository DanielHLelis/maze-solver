from flask import request

from .app import app
from .mapper import dict_to_maze, maze_solution_to_dict

from ..maze.dfs_solve import maze_dfs_solve
from ..maze.bfs_solve import maze_bfs_solve
from ..maze.rnd_solve import maze_rnd_solve


@app.route("/maze/dfs_solve", methods=["POST"])
def maze_dfs_solve_route():
    """
    Solve a maze using the DFS algorithm.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_dfs_solve(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/bfs_solve", methods=["POST"])
def maze_bfs_solve_route():
    """
    Solve a maze using the BFS algorithm.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_bfs_solve(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/rnd_solve", methods=["POST"])
def maze_rnd_solve_route():
    """
    Solve a maze using the random walk algorithm.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_rnd_solve(maze)

    return maze_solution_to_dict(maze_solution)
