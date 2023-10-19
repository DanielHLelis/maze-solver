from typing import List, Tuple

from .maze import Maze, MazeSolution
from random import randint, choice

class Cell:
    row: int
    col: int
    visited: bool
    walls: List[bool]

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]

def WilsonsGenerator(height: int, width: int) -> Maze:
    map = []
    for i in range(height):
        map.append([])
        for j in range(width):
            map[i].append(Cell(i, j)) # Inicialmente, todos os movimentos são válidos
    
    def get_random_unvisited(map: List(List(Cell)), visited_cells: List(Cell)) -> Cell:
        # Pula aleatoriamente pelo tabuleiro até encontrar uma célula não visitada
        position = choice(choice(map))
        while position in visited_cells:
            position = choice(choice(map))  
        return position

    def candidate_moves(map: List(List(Cell)), curr_pos: Cell) -> List(Cell):
        moves = []

        if (curr_pos.row > 1):
            moves.append(move_direction(map, curr_pos,  1))

        if (curr_pos.col < len(map[0]) - 1):
            moves.append(move_direction(map, curr_pos,  2))
        
        if (curr_pos.row < len(map) - 1):
            moves.append(move_direction(map, curr_pos, -1))
        
        if (curr_pos.col > 1):
            moves.append(move_direction(map, curr_pos, -2))

    def direction(curr_pos: Cell, next_pos: Cell) -> int:
        if   curr_pos[1] < next_pos[1]: return  1 # acima
        elif curr_pos[0] < next_pos[0]: return  2 # direita
        elif curr_pos[1] > next_pos[1]: return -1 # abaixo
        elif curr_pos[0] > next_pos[0]: return -2 # esquerda 

    def move_direction(map: List(List(Cell)), curr_pos: Cell, direction: int) -> Cell:
        match(direction):
            case  1:
                return map[curr_pos.row + 1][curr_pos.col] # acima
            case  2:
                return map[curr_pos.row][curr_pos.col + 1] # direita
            case -1:
                return map[curr_pos.row - 1][curr_pos.col] # abaixo
            case -2:
                return map[curr_pos.row][curr_pos.col - 1] # esquerda

    def walk(maze: Maze) -> List[Tuple[Cell, Direction]]:
        start_position = get_random_unvisited([])
        path = {}
        current_position = start_position

        while True:
            current_position.visited = True
            next_position : Cell = choice(maze.candidate_moves(current_position))
            path[current_position] = direction(current_position, next_position)
            
            if next_position.visited:
                break
            
            current_position = next_position

        track = []
        current_position = start_position
        while current_position in path:
            direction = visits[current_position]
            track.append((current_position, direction))
            current_position = move_direction(current_position, direction)
        
        return track

    visited = []
    while len(visited) < height * width:
        for current_position, direction in walk():
            visited.append(current_position)
            next_position = move_direction(map, current_position, direction)
            current_position.walls[direction] = False
            next_position.walls[-direction] = False