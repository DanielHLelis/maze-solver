from maze.maze import load_maze_json
from maze.dfs_solve import maze_dfs_solve
from maze.bfs_solve import maze_bfs_solve
from maze.dfs_heuristic_solve import maze_dfs_heuristic_solve
from maze.bhfs_solve import maze_bhfs_solve
from typing import Tuple

def heu_1(end: Tuple[int, int],candidate: Tuple[int, int]):
    return ((end[0]-candidate[0])**2 + (end[1]-candidate[1])**2)

def heu_2(end: Tuple[int, int],candidate: Tuple[int, int]):
    return (abs(end[0]-candidate[0]) + abs(end[1]-candidate[1]))

def heu_3(end: Tuple[int, int],candidate: Tuple[int, int]):
    return (abs(end[0]-candidate[0]))

def heu_4(end: Tuple[int, int],candidate: Tuple[int, int]):
    return (abs(end[1]-candidate[1]))

def heu_5(end: Tuple[int, int],candidate: Tuple[int, int]):
    return abs((end[0]-candidate[0])*(end[1]-candidate[1]))

if __name__ == "__main__":
    m = load_maze_json("./samples/medium.json")
    dfs_m = maze_dfs_solve(m)
    bfs_m = maze_bfs_solve(m)
    dfs_heu1_m = maze_dfs_heuristic_solve(m,heu_1)
    dfs_heu2_m = maze_dfs_heuristic_solve(m,heu_2)
    dfs_heu3_m = maze_dfs_heuristic_solve(m,heu_3)
    dfs_heu4_m = maze_dfs_heuristic_solve(m,heu_4)
    dfs_heu5_m = maze_dfs_heuristic_solve(m,heu_5)
    bhfs1_m = maze_bhfs_solve(m,heu_1)
    bhfs2_m = maze_bhfs_solve(m,heu_2)
    bhfs3_m = maze_bhfs_solve(m,heu_3)
    bhfs4_m = maze_bhfs_solve(m,heu_4)
    bhfs5_m = maze_bhfs_solve(m,heu_5)

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

    print(f"DFS Heuristic1: {len(dfs_heu1_m.steps)} steps, {len(dfs_heu1_m.path)} path")
    print(dfs_heu1_m)

    print()
    print("=" * 80)
    print()

    print(f"DFS Heuristic2: {len(dfs_heu2_m.steps)} steps, {len(dfs_heu2_m.path)} path")
    print(dfs_heu2_m)

    print()
    print("=" * 80)
    print()

    print(f"DFS Heuristic3: {len(dfs_heu3_m.steps)} steps, {len(dfs_heu3_m.path)} path")
    print(dfs_heu3_m)

    print()
    print("=" * 80)
    print()

    print(f"DFS Heuristic4: {len(dfs_heu4_m.steps)} steps, {len(dfs_heu4_m.path)} path")
    print(dfs_heu4_m)

    print()
    print("=" * 80)
    print()

    print(f"BHFS1: {len(bhfs1_m.steps)} steps, {len(bhfs1_m.path)} path")
    print(bhfs1_m)

    print()
    print("=" * 80)
    print()

    print(f"BHFS2: {len(bhfs2_m.steps)} steps, {len(bhfs2_m.path)} path")
    print(bhfs2_m)

    print()
    print("=" * 80)
    print()

    print(f"BHFS3: {len(bhfs3_m.steps)} steps, {len(bhfs3_m.path)} path")
    print(bhfs3_m)

    print()
    print("=" * 80)
    print()

    print(f"BHFS4: {len(bhfs4_m.steps)} steps, {len(bhfs4_m.path)} path")
    print(bhfs4_m)

    print()
    print("=" * 80)
    print()


    print(f"DFS: {len(dfs_m.steps)} steps, {len(dfs_m.path)} path")
    print(f"BFS: {len(bfs_m.steps)} steps, {len(bfs_m.path)} path")
    print(f"DFS Heuristic1: {len(dfs_heu1_m.steps)} steps, {len(dfs_heu1_m.path)} path")
    print(f"DFS Heuristic2: {len(dfs_heu2_m.steps)} steps, {len(dfs_heu2_m.path)} path")
    print(f"DFS Heuristic3: {len(dfs_heu3_m.steps)} steps, {len(dfs_heu3_m.path)} path")
    print(f"DFS Heuristic4: {len(dfs_heu4_m.steps)} steps, {len(dfs_heu4_m.path)} path")
    print(f"DFS Heuristic5: {len(dfs_heu5_m.steps)} steps, {len(dfs_heu5_m.path)} path")
    print(f"BHFS1: {len(bhfs1_m.steps)} steps, {len(bhfs1_m.path)} path")
    print(f"BHFS2: {len(bhfs2_m.steps)} steps, {len(bhfs2_m.path)} path")
    print(f"BHFS3: {len(bhfs3_m.steps)} steps, {len(bhfs3_m.path)} path")
    print(f"BHFS4: {len(bhfs4_m.steps)} steps, {len(bhfs4_m.path)} path")
    print(f"BHFS5: {len(bhfs4_m.steps)} steps, {len(bhfs5_m.path)} path")
