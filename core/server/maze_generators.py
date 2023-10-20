import time
from flask import request

from .app import app
from .mapper import maze_to_dict

from ..maze.dfs_gen import maze_dfs_gen, maze_chaos_dfs_gen
from ..maze.wilson_gen import maze_wilson_gen


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
    start = (int(start[0]), int(start[1])) if start else None
    end = (int(end[0]), int(end[1])) if end else None

    maze = maze_dfs_gen(height, width, start=start, end=end, seed=seed)
    maze.tidy()

    return maze_to_dict(maze)


@app.route(
    "/maze/generate/chaos-dfs/<int:width>/<int:height>/",
    methods=["GET"],
    defaults={"seed": None},
)
@app.route("/maze/generate/chaos-dfs/<int:width>/<int:height>/<seed>", methods=["GET"])
def maze_chaos_dfs_gen_route(width: int, height: int, seed: str):
    """
    Generate a maze using the "Chaos" DFS algorithm (DFS gen with ranndom wall openings).
    """

    if seed is None:
        seed = time.time()

    start = request.args.get("start").split(",") if request.args.get("start") else None
    end = request.args.get("end").split(",") if request.args.get("end") else None
    start = (int(start[0]), int(start[1])) if start else None
    end = (int(end[0]), int(end[1])) if end else None
    p = float(request.args.get("p")) if request.args.get("p") else None

    maze = maze_chaos_dfs_gen(height, width, start=start, end=end, seed=seed, p=p)
    maze.tidy()

    return maze_to_dict(maze)


@app.route(
    "/maze/generate/wilson/<int:width>/<int:height>/",
    methods=["GET"],
    defaults={"seed": None},
)
@app.route("/maze/generate/wilson/<int:width>/<int:height>/<seed>", methods=["GET"])
def maze_wilson_gen_route(width: int, height: int, seed: str):
    """
    Generate a maze using the Wilson's algorithm.
    """

    if seed is None:
        seed = time.time()

    start = request.args.get("start").split(",") if request.args.get("start") else None
    end = request.args.get("end").split(",") if request.args.get("end") else None
    start = (int(start[0]), int(start[1])) if start else None
    end = (int(end[0]), int(end[1])) if end else None

    maze = maze_wilson_gen(height, width, start=start, end=end, seed=seed)
    maze.tidy()

    return maze_to_dict(maze)
