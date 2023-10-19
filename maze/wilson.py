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
    
    maze = Maze(map)

    def get_random_unvisited(map: List(List(Tuple[int][int])), visited_cells: List(Tuple[int][int])) -> Cell:
        # Pula aleatoriamente pelo tabuleiro até encontrar uma célula não visitada
        position = choice(choice(map))
        while position in visited_cells:
            position = choice(choice(map))  
        return position

    def direction(curr_pos: Tuple[int, int], next_pos: Tuple[int, int]) -> int:
        if   curr_pos[1] < next_pos[1]: return 0 # acima
        elif curr_pos[0] < next_pos[0]: return 1 # direita
        elif curr_pos[1] > next_pos[1]: return 2 # abaixo
        elif curr_pos[0] > next_pos[0]: return 3 # esquerda 

    def move_direction(curr_pos: Tuple[int, int], direction: int):

        # dasdas
        return tuple(curr_pos[0] + direction[0], curr_pos[1] + direction[1])

    def walk(maze: Maze) -> List[Tuple[Cell, Direction]]:
        start_position = get_random_unvisited([])
        path = {}
        current_position = start_position

        while True:
            next_position = choice(maze.candidate_moves(current_position))
            path[current_position] = direction(current_position, next_position)
            
            if next_position in path:
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
        for position, direction in walk():
            visited.append(position)