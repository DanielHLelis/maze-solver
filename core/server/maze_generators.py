import time
from flask import request

from .app import app
from .mapper import maze_to_dict

from ..maze.dfs_gen import maze_dfs_gen, maze_chaos_dfs_gen


@app.route(
    "/maze/generate/dfs/<int:width>/<int:height>/",
    methods=["GET"],
    defaults={"seed": None},
)
@app.route("/maze/generate/dfs/<int:width>/<int:height>/<seed>", methods=["GET"])
def maze_dfs_gen_route(width: int, height: int, seed: str):
    """
    Generate a maze using the DFS algorithm.
    """
    if seed is None:
        seed = time.time()

    start = request.args.get("start").split(",") if request.args.get("start") else None
    end = request.args.get("end").split(",") if request.args.get("end") else None

    maze = maze_dfs_gen(width, height, start=start, end=end, seed=seed)

    return maze_to_dict(maze)


@app.route(
    "/maze/generate/chaos-dfs/<int:width>/<int:height>/",
    methods=["GET"],
    defaults={"seed": None},
)
@app.route("/maze/generate/dfs/<int:width>/<int:height>/<seed>", methods=["GET"])
def maze_chaos_dfs_gen_route(width: int, height: int, seed: str):
    """
    Generate a maze using the "Chaos" DFS algorithm (DFS gen with ranndom wall openings).
    """

    if seed is None:
        seed = time.time()

    start = request.args.get("start").split(",") if request.args.get("start") else None
    end = request.args.get("end").split(",") if request.args.get("end") else None
    p = float(request.args.get("p")) if request.args.get("p") else None

    maze = maze_chaos_dfs_gen(width, height, start=start, end=end, seed=seed, p=p)

    return maze_to_dict(maze)
