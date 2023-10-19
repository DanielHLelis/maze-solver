from maze.maze import load_maze_json
from maze.bfs_solve import maze_bfs_solve
from maze.dfs_solve import maze_dfs_solve
from maze.random_solve import maze_rnd_solve

if __name__ == "__main__":
    m = load_maze_json("./samples/medium.json")
    dfs_m = maze_dfs_solve(m)
    bfs_m = maze_bfs_solve(m)
    rnd_m = maze_rnd_solve(m)

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