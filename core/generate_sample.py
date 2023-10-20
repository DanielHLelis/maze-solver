import sys
import time
from maze.maze import dump_maze_json, dump_maze_solution_json
from maze.dfs_gen import maze_chaos_dfs_gen
from maze.bfs_solve import maze_bfs_solve

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_sample.py output")
        sys.exit(1)

    file_name = sys.argv[1]
    seed = str(int(time.time()))

    m = maze_chaos_dfs_gen(81, 81, seed=seed)
    sol = maze_bfs_solve(m)

    dump_maze_json(m, f"{file_name}-{seed}.maze.json")
    dump_maze_solution_json(sol, f"{file_name}-{seed}.maze.solution.json")
