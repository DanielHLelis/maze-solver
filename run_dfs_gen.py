import sys
import time
from maze.dfs_gen import maze_dfs_gen
from maze.dfs_solve import maze_dfs_solve
from maze.bfs_solve import maze_bfs_solve
from maze.rnd_solve import maze_rnd_solve

if __name__ == "__main__":
    seed = sys.argv[1] if len(sys.argv) > 1 else "time"

    if seed == "time":
        seed = str(time.time())

    m = maze_dfs_gen(41, 41, seed=seed)
    dfs_m = maze_dfs_solve(m)
    bfs_m = maze_bfs_solve(m)
    rnd_m = maze_rnd_solve(m, seed=seed)

    print(f"Seed: {seed}", end="\n\n")

    print(f"DFS: {len(dfs_m.steps)} steps, {len(dfs_m.path)} path")
    print(dfs_m)

    print()
    print("=" * 80)
    print()

    print(f"BFS: {len(bfs_m.steps)} steps, {len(bfs_m.path)} path")
    print(bfs_m)

    print()
    print("=" * 80)
    print()

    print(f"RND: {len(rnd_m.steps)} steps, {len(rnd_m.path)} path")
    print(rnd_m)
