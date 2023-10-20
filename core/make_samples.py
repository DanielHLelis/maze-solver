import sys
import time
from random import Random

from maze.maze import dump_maze_json, dump_maze_solution_json
from maze.dfs_gen import maze_chaos_dfs_gen
from maze.dfs_solve import maze_dfs_solve
from maze.bfs_solve import maze_bfs_solve
from maze.rnd_solve import maze_rnd_solve
from maze.astar_solve import (
    maze_astar_solve_dijkstra,
    maze_astar_solve_euclidian,
    maze_astar_solve_manhattan,
)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_sample.py output")
        sys.exit(1)

    file_name = sys.argv[1]
    seed = str(int(time.time()))
    rng = Random(seed)

    m = maze_chaos_dfs_gen(61, 61, seed=seed)

    dfs = maze_dfs_solve(m)
    bfs = maze_bfs_solve(m)
    rnd = maze_rnd_solve(m, rng.randint(0, 1000000))
    dij = maze_astar_solve_dijkstra(m)
    euc = maze_astar_solve_euclidian(m)
    man = maze_astar_solve_manhattan(m)

    dump_maze_json(m, f"{file_name}.maze.json")
    dump_maze_solution_json(dfs, f"{file_name}.dfs.json")
    dump_maze_solution_json(bfs, f"{file_name}.bfs.json")
    dump_maze_solution_json(rnd, f"{file_name}.rnd.json")
    dump_maze_solution_json(dij, f"{file_name}.dij.json")
    dump_maze_solution_json(euc, f"{file_name}.euc.json")
    dump_maze_solution_json(man, f"{file_name}.man.json")
