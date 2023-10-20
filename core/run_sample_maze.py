from maze.maze import load_maze_json
from run_solvers import run_solvers

if __name__ == "__main__":
    m = load_maze_json("./samples/medium.json")
    run_solvers(m)
