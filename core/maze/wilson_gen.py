from typing import List, Tuple, Optional, Any
from random import Random
from .maze import Maze, Cell


def maze_wilson_gen(
    height: int,
    width: int,
    start: Optional[Tuple[int, int]] = None,
    end: Optional[Tuple[int, int]] = None,
    seed: Optional[Any] = "insider_trading_do_bernardo",
) -> Maze:
    rng = Random(seed)

    c_height = height // 2
    c_width = width // 2
    height = c_height * 2 + 1
    width = c_width * 2 + 1

    cells = []
    for i in range(c_height):
        cells.append([])
        for j in range(c_width):
            cells[i].append(Cell(i, j))  # Inicialmente, todos os movimentos são válidos

    unvisited = [cell for row in cells for cell in row]
    rng.shuffle(unvisited)

    first_visit = unvisited.pop()
    first_visit.visited = True

    def get_random_unvisited() -> Cell:
        # Pula aleatoriamente pelo tabuleiro até encontrar uma célula não visitada
        return rng.choice(unvisited)

    def candidate_moves(curr_pos: Cell) -> List[Cell]:
        moves = []

        if curr_pos.row > 0:  # acima
            moves.append(move_direction(cells, curr_pos, 1))

        if curr_pos.col < len(cells[0]) - 1:  # direita
            moves.append(move_direction(cells, curr_pos, 2))

        if curr_pos.row < len(cells) - 1:  # abaixo
            moves.append(move_direction(cells, curr_pos, -1))

        if curr_pos.col > 0:  # esquerda
            moves.append(move_direction(cells, curr_pos, -2))

        return moves

    def direction_to(curr: Cell, next: Cell) -> int:
        if curr.row < next.row:
            return 0  # acima
        elif curr.col < next.col:
            return 1  # direita
        elif curr.row > next.row:
            return 2  # abaixo
        elif curr.col > next.col:
            return 3  # esquerda

    def move_direction(cells: List[List[Cell]], curr_pos: Cell, direction: int) -> Cell:
        match (direction):
            case 1:
                return cells[curr_pos.row - 1][curr_pos.col]  # acima
            case 2:
                return cells[curr_pos.row][curr_pos.col + 1]  # direita
            case -1:
                return cells[curr_pos.row + 1][curr_pos.col]  # abaixo
            case -2:
                return cells[curr_pos.row][curr_pos.col - 1]  # esquerda

    while len(unvisited) > 0:
        curr = get_random_unvisited()
        path = []

        while curr in unvisited:
            next = rng.choice(candidate_moves(curr))

            path.append([curr, next])

            if next in path:
                path = path[0 : path.index([curr, next]) + 1]

            curr = next

        for prev, next in path:
            prev.walls[direction_to(prev, next)] = False
            try:
                unvisited.remove(prev)
            except:
                pass

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

    if start is None:
        start_point = (rng.randint(0, c_height - 1), rng.randint(0, c_width - 1))
    else:
        start_point = (start[0] // 2, start[1] // 2)

    if end is None:
        end_point = (rng.randint(0, c_height - 1), rng.randint(0, c_width - 1))
    else:
        end_point = (end[0] // 2, end[1] // 2)

    return Maze(
        matrix,
        start=(start_point[0] * 2 + 1, start_point[1] * 2 + 1),
        end=(end_point[0] * 2 + 1, end_point[1] * 2 + 1),
    )
