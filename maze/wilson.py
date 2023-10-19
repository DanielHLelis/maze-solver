from typing import List, Tuple

from .maze import Maze, MazeSolution
from random import randint, choice

def WilsonsGenerator(height: int, width: int) -> Maze:
    map = []
    for i in range(height):
        map.append([])
        for j in range(width):
            map[i].append([1]) # Inicialmente, todos os movimentos são válidos
    
    maze = Maze(map)

    def get_random_unvisited(visited_cells: List(Tuple[int][int])) -> Tuple[int, int]:
        # Pula aleatoriamente pelo tabuleiro até encontrar uma célula não visitada
        position = tuple(randint(0, height - 1), randint(0, width - 1))
        while position in visited_cells:
            position = tuple(randint(0, height - 1), randint(0, width - 1))
        return position

    def direction(curr_pos: Tuple[int, int], next_pos: Tuple[int, int]) -> Tuple[int][int]:
        if curr_pos[0] > next_pos[0]:   return tuple(-1,  0) # esquerda 
        elif curr_pos[0] < next_pos[0]: return tuple( 1,  0) # direita
        elif curr_pos[1] > next_pos[1]: return tuple( 0, -1) # acima
        elif curr_pos[1] > next_pos[1]: return tuple( 0,  1) # abaixo

    def move_direction(curr_pos: Tuple[int, int], direction:[int, int]):
        return tuple(curr_pos[0] + direction[0], curr_pos[1] + direction[1])

    def walk(maze: Maze) -> List[Tuple[Cell, Direction]]:
        """Perform a random walk through unvisited cells of the maze and return the path walked."""
        start_position = get_random_unvisited([])
        # visited = [start_position]
        path = {}
        current_position = start_position

        while True:
            next_position = choice(maze.candidate_moves(current_position))
            path[current_position] = direction(current_position, next_position)
            
            if next_position in path:
                break
            
            # visited.append(next_position)
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
            

    # def generate_maze(self) -> None:
    #     """Generate paths through a maze using Wilson's algorithm for generating uniform spanning trees."""
    #     self.included_cells = set()
    #     start_cell = self.get_random_start_cell()
    #     self.included_cells.add(start_cell)
    #     while len(self.included_cells) < self.maze.width * self.maze.height:
    #         for cell, direction in self.walk():
    #             neighbor = self.maze.neighbor(cell, direction)
    #             self.open_wall(cell, neighbor)
    #             self.included_cells.add(cell)