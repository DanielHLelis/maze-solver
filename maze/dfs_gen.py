from random import Random
from typing import List, Optional, Any

from .maze import Maze, Cell


# DFS generator works better with a cell matrix, instead of a boolean matrix.


def maze_dfs_gen(
    height: int, width: int, seed: Optional[Any] = "insider_trading_do_bernardo"
) -> Maze:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rng = Random(seed)

    c_height = height // 2
    c_width = width // 2
    height = c_height * 2 + 1
    width = c_width * 2 + 1

    cells = [[Cell(r, c) for c in range(c_width)] for r in range(c_height)]

    start_point = (rng.randint(0, c_height - 1), rng.randint(0, c_width - 1))
    end_point = (rng.randint(0, c_height - 1), rng.randint(0, c_width - 1))

    stack = [(cells[start_point[0]][start_point[1]], None, None)]

    while stack:
        (cur, par, dir) = stack.pop()

        if cur.visited:
            continue

        cur.visited = True

        if par is not None:
            cur.walls[(dir + 2) % 4] = False
            par.walls[dir] = False

        candidates = []
        for i in range(len(moves)):
            move = moves[i]
            nr, nc = cur.row + move[0], cur.col + move[1]
            if nr < 0 or nr >= c_height or nc < 0 or nc >= c_width:
                continue
            if cells[nr][nc].visited:
                continue
            candidates.append((nr, nc, i))

        rng.shuffle(candidates)

        for next_candidate in candidates:
            stack.append(
                (cells[next_candidate[0]][next_candidate[1]], cur, next_candidate[2])
            )

    matrix = [[False] * (width) for _ in range(height)]

    for r in range(c_height):
        for c in range(c_width):
            matrix[r * 2 + 1][c * 2 + 1] = True
            if not cells[r][c].walls[0] and r * 2 > 0:
                matrix[r * 2][c * 2 + 1] = True
            if not cells[r][c].walls[1] and c * 2 + 2 < width:
                matrix[r * 2 + 1][c * 2 + 2] = True
            if not cells[r][c].walls[2] and r * 2 + 2 < height:
                matrix[r * 2 + 2][c * 2 + 1] = True
            if not cells[r][c].walls[3] and c * 2 > 0:
                matrix[r * 2 + 1][c * 2] = True

    return Maze(
        matrix,
        start=(start_point[0] * 2 + 1, start_point[1] * 2 + 1),
        end=(end_point[0] * 2 + 1, end_point[1] * 2 + 1),
    )
