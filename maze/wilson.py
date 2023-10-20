from typing import List, Tuple

from .maze import Maze, MazeSolution
from random import randint, choice, shuffle

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
    maze = []
    for i in range(height):
        maze.append([])
        for j in range(width):
            maze[i].append(Cell(i, j)) # Inicialmente, todos os movimentos são válidos

    unvisited = [cell for row in maze for cell in row]
    shuffle(unvisited)

    first_visit = unvisited.pop()
    first_visit.visited = True

    def get_random_unvisited() -> Cell:
        # Pula aleatoriamente pelo tabuleiro até encontrar uma célula não visitada
        return choice(unvisited)

    def candidate_moves(curr_pos: Cell) -> List[Cell]:
        moves = []

        if (curr_pos.row > 0): # acima
            moves.append(move_direction(maze, curr_pos,  1))

        if (curr_pos.col < len(maze[0]) - 1): # direita
            moves.append(move_direction(maze, curr_pos,  2))
        
        if (curr_pos.row < len(maze) - 1): # abaixo
            # print("------Abaixo:", curr_pos.row, '<', len(maze[0]) - 1)
            moves.append(move_direction(maze, curr_pos, -1))
        
        if (curr_pos.col > 0): # esquerda
            moves.append(move_direction(maze, curr_pos, -2))
        
        return moves

    def direction_to(curr: Cell, next: Cell) -> int:
        if   curr.row < next.row: return  0 # acima
        elif curr.col < next.col: return  1 # direita
        elif curr.row > next.row: return  2 # abaixo
        elif curr.col > next.col: return  3 # esquerda 

    def move_direction(maze: List[List[Cell]], curr_pos: Cell, direction: int) -> Cell:
        match(direction):
            case  1:
                return maze[curr_pos.row - 1][curr_pos.col] # acima
            case  2:
                return maze[curr_pos.row][curr_pos.col + 1] # direita
            case -1:
                return maze[curr_pos.row + 1][curr_pos.col] # abaixo
            case -2:
                return maze[curr_pos.row][curr_pos.col - 1] # esquerda

    while len(unvisited) > 0:
        curr = get_random_unvisited()
        path = [curr]

        while curr in unvisited:
            next = choice(candidate_moves(curr))

            if next in path:
                path = path[0:path.index(next)+1]
            
            else:
                path.append(next)
            
            curr = next
        

        prev : Cell = None
        for cell in path:
            if prev:
                prev.walls[direction_to(prev, cell)] = False
                unvisited.remove(prev)
            
            prev = cell
        
    
    return maze