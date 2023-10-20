import sys
import time
from maze.wilson_gen import maze_wilson_gen
from run_solvers import run_solvers

if __name__ == "__main__":
    seed = sys.argv[1] if len(sys.argv) > 1 else "time"

    if seed == "time":
        seed = str(time.time())

    m = maze_wilson_gen(41, 81, seed=seed)
    print(m)
    run_solvers(m)
