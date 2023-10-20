import time
from flask import request

from .app import app
from .mapper import dict_to_maze, maze_solution_to_dict

from ..maze.dfs_solve import (
    maze_dfs_solve,
    maze_dfs_solve_euclidean,
    maze_dfs_solve_manhattan,
)
from ..maze.bfs_solve import maze_bfs_solve
from ..maze.rnd_solve import maze_rnd_solve
from ..maze.astar_solve import (
    maze_astar_solve_dijkstra,
    maze_astar_solve_euclidean,
    maze_astar_solve_manhattan,
)
from ..maze.bfirst_solve import (
    maze_bfirst_solve_dijkstra,
    maze_bfirst_solve_euclidean,
    maze_bfirst_solve_manhattan,
)


@app.route("/maze/solve/dfs", methods=["POST"])
def maze_dfs_solve_route():
    """
    Solve a maze using the DFS algorithm.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_dfs_solve(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/dfs-manhattan", methods=["POST"])
def maze_dfs_manhattan_solve_route():
    """
    Solve a maze using the DFS algorithm with Manhattan heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_dfs_solve_manhattan(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/dfs-euclidean", methods=["POST"])
def maze_dfs_euclidean_solve_route():
    """
    Solve a maze using the DFS algorithm with Euclidean heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_astar_solve_euclidean(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/bfs", methods=["POST"])
def maze_bfs_solve_route():
    """
    Solve a maze using the BFS algorithm.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_bfs_solve(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/rds", methods=["POST"])
def maze_rds_solve_route():
    """
    Solve a maze using the random walk algorithm.
    """
    seed = request.args.get("seed") or time.time()
    maze = dict_to_maze(request.json)
    maze_solution = maze_rnd_solve(maze, seed=seed)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/astar-dijkstra", methods=["POST"])
def maze_astar_solve_dijkstra_route():
    """
    Solve a maze using the A* algorithm with Dijkstra's heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_astar_solve_dijkstra(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/astar-euclidean", methods=["POST"])
def maze_astar_solve_euclidean_route():
    """
    Solve a maze using the A* algorithm with Euclidian heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_astar_solve_euclidean(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/astar-manhattan", methods=["POST"])
def maze_astar_solve_manhattan_route():
    """
    Solve a maze using the A* algorithm with Manhattan heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_astar_solve_manhattan(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/bfirst-dijkstra", methods=["POST"])
def maze_bfirst_solve_dijkstra_route():
    """
    Solve a maze using the A* algorithm with Dijkstra's heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_bfirst_solve_dijkstra(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/bfirst-euclidean", methods=["POST"])
def maze_bfirst_solve_euclidean_route():
    """
    Solve a maze using the A* algorithm with Euclidian heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_bfirst_solve_euclidean(maze)

    return maze_solution_to_dict(maze_solution)


@app.route("/maze/solve/bfirst-manhattan", methods=["POST"])
def maze_bfirst_solve_manhattan_route():
    """
    Solve a maze using the A* algorithm with Manhattan heuristic.
    """
    maze = dict_to_maze(request.json)
    maze_solution = maze_bfirst_solve_manhattan(maze)

    return maze_solution_to_dict(maze_solution)
