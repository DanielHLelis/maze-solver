import sys
import time
from random import Random

from maze.maze import dump_maze_json, dump_maze_solution_json, Maze
from maze.dfs_gen import maze_chaos_dfs_gen, maze_dfs_gen
from maze.wilson_gen import maze_wilson_gen
from maze.dfs_solve import maze_dfs_solve, maze_dfs_solve_manhattan
from maze.bfs_solve import maze_bfs_solve
from maze.rnd_solve import maze_rnd_solve
from maze.astar_solve import (
    maze_astar_solve_dijkstra,
    maze_astar_solve_euclidean,
    maze_astar_solve_manhattan,
)
from maze.bfirst_solve import (
    maze_bfirst_solve_dijkstra,
    maze_bfirst_solve_euclidean,
    maze_bfirst_solve_manhattan,
)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_sample.py output")
        sys.exit(1)

    file_name = sys.argv[1]
    seed = str(int(time.time()))
    rng = Random(seed)

    m_dfs = maze_dfs_gen(
        61, 61, start=(1, 1), end=(59, 59), seed=rng.randint(0, 1000000)
    )
    m_dfs.tidy()

    m_wilson = maze_wilson_gen(
        61, 61, start=(1, 1), end=(59, 59), seed=rng.randint(0, 1000000)
    )
    m_wilson.tidy()

    m = maze_chaos_dfs_gen(
        61, 61, start=(1, 1), end=(59, 59), p=0.15, seed=rng.randint(0, 1000000)
    )
    m.tidy()

    dfs = maze_dfs_solve(m)
    dfs_man = maze_dfs_solve_manhattan(m)
    bfs = maze_bfs_solve(m)
    rnd = maze_rnd_solve(m, rng.randint(0, 1000000))
    dij = maze_astar_solve_dijkstra(m)
    euc = maze_astar_solve_euclidean(m)
    man = maze_astar_solve_manhattan(m)
    bdij = maze_bfirst_solve_dijkstra(m)
    beuc = maze_bfirst_solve_euclidean(m)
    bman = maze_bfirst_solve_manhattan(m)

    dump_maze_json(m, f"{file_name}.maze.json")
    dump_maze_json(m_dfs, f"{file_name}.maze-dfs.json")
    dump_maze_json(m_wilson, f"{file_name}.maze-wilson.json")
    dump_maze_solution_json(dfs, f"{file_name}.dfs.json")
    dump_maze_solution_json(dfs, f"{file_name}.dfsm.json")
    dump_maze_solution_json(bfs, f"{file_name}.bfs.json")
    dump_maze_solution_json(rnd, f"{file_name}.rnd.json")
    dump_maze_solution_json(dij, f"{file_name}.adij.json")
    dump_maze_solution_json(euc, f"{file_name}.aeuc.json")
    dump_maze_solution_json(man, f"{file_name}.aman.json")
    dump_maze_solution_json(bdij, f"{file_name}.bdij.json")
    dump_maze_solution_json(beuc, f"{file_name}.beuc.json")
    dump_maze_solution_json(bman, f"{file_name}.bman.json")
