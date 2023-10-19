from flask import request

from .app import app
from .mapper import maze_to_dict

from ..maze.dfs_gen import maze_dfs_gen


@app.route("/maze/dfs_gen/<int:width>/<int:height>/<seed>", methods=["GET"])
def maze_dfs_gen_route(width: int, height: int, seed: str):
    """
    Generate a maze using the DFS algorithm.
    """
    maze = maze_dfs_gen(width, height, seed=seed)

    return maze_to_dict(maze)
