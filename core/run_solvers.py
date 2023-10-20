from maze.maze import load_maze_json
from maze.bfs_solve import maze_bfs_solve
from maze.dfs_solve import maze_dfs_solve
from maze.rnd_solve import maze_rnd_solve
from maze.astar_solve import (
    maze_astar_solve_euclidean,
    maze_astar_solve_manhattan,
    maze_astar_solve_dijkstra,
)


def run_solvers(m):
    dfs_m = maze_dfs_solve(m)
    bfs_m = maze_bfs_solve(m)
    rnd_m = maze_rnd_solve(m)
    astar_dijkstra_m = maze_astar_solve_dijkstra(m)
    astar_euclidean_m = maze_astar_solve_euclidean(m)
    astar_manhattan_m = maze_astar_solve_manhattan(m)

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

    print()
    print("=" * 80)
    print()

    print(
        f"ASTAR (Dijkstra): {len(astar_dijkstra_m.steps)} steps, {len(astar_dijkstra_m.path)} path"
    )
    print(astar_dijkstra_m)

    print()
    print("=" * 80)
    print()

    print(
        f"ASTAR (Euclidian): {len(astar_euclidean_m.steps)} steps, {len(astar_euclidean_m.path)} path"
    )
    print(astar_euclidean_m)

    print()
    print("=" * 80)
    print()

    print(
        f"ASTAR (Manhattan): {len(astar_manhattan_m.steps)} steps, {len(astar_manhattan_m.path)} path"
    )
    print(astar_manhattan_m)
