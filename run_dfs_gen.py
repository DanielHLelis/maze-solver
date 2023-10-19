from maze.dfs_gen import maze_dfs_gen
from maze.dfs_solve import maze_dfs_solve
from maze.bfs_solve import maze_bfs_solve

if __name__ == "__main__":
    m = maze_dfs_gen(41, 81)
    print(m)

    dfs_m = maze_dfs_solve(m)

    print(f"DFS: {len(dfs_m.steps)} steps, {len(dfs_m.path)} path")
    print(dfs_m)

    bfs_m = maze_bfs_solve(m)

    print(f"BFS: {len(bfs_m.steps)} steps, {len(bfs_m.path)} path")
    print(bfs_m)
