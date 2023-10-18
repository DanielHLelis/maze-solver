from maze.maze import load_maze_json
from maze.dfs_solve import maze_dfs_solve
from maze.bfs_solve import maze_bfs_solve

if __name__ == "__main__":
    m = load_maze_json("./samples/medium.json")
    dfs_m = maze_dfs_solve(m)
    bfs_m = maze_bfs_solve(m)

    print(f"DFS: {len(dfs_m.steps)} steps, {len(dfs_m.path)} path")
    print(dfs_m)

    print()
    print("=" * 80)
    print()

    print(f"BFS: {len(bfs_m.steps)} steps, {len(bfs_m.path)} path")
    print(bfs_m)
