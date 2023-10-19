const debugMode = false;
const solver: "dfs" | "bfs" = "bfs";

const searchStart = [63, 71];
const searchEnd = [0, 1];

const wallColor = [255, 255, 255, 0.2];
const animationColorOld = [58, 134, 255, 1.0];
const animationColorRecent = [255, 0, 110, 1.0];
const animationSolvedColor = [131, 56, 236, 1.0];

const animationSpeed = 36.8;
const stepsPerFrame = 40;
const animationElapsedCap = 1000;

function toRGBString(color: number[]) {
  if (color.length === 4) {
    return `rgba(${color[0]}, ${color[1]}, ${color[2]}, ${color[3]})`;
  }

  if (color.length === 3) {
    return `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
  }

  return "rgb(0, 0, 0)";
}

function dfsMazeSolver(maze: number[][], start: number[], end: number[]) {
  const path: number[][] = [];
  const steps: number[][] = [];
  const visited = maze.map((row) => row.map(() => false));

  const dfs = (y: number, x: number) => {
    if (
      y < 0 ||
      y >= maze.length ||
      x < 0 ||
      x >= maze[0].length ||
      maze[y][x] === 1
    ) {
      return false;
    }

    if (visited[y][x]) {
      return;
    }

    visited[y][x] = true;
    steps.push([y, x]);

    if (y === end[0] && x === end[1]) {
      path.push([y, x]);
      return true;
    }

    const neighbors = [
      [y - 1, x],
      [y + 1, x],
      [y, x - 1],
      [y, x + 1],
    ];

    for (const [ny, nx] of neighbors) {
      if (ny < 0 || ny >= maze.length || nx < 0 || nx >= maze[0].length) {
        continue;
      }

      if (maze[ny][nx] === 1) {
        continue;
      }

      if (dfs(ny, nx)) {
        path.push([y, x]);
        return true;
      }
    }

    return false;
  };

  dfs(start[0], start[1]);
  return [path.reverse(), steps];
}

const bfsMazeSolver = (maze: number[][], start: number[], end: number[]) => {
  const path: number[][] = [];
  const steps: number[][] = [];

  const parents = maze.map((row) => row.map(() => null));
  const visited = maze.map((row) => row.map(() => false));

  const queue = [start];
  let found = false;

  while (queue.length > 0) {
    const [y, x] = queue.shift()!;
    if (
      y < 0 ||
      y >= maze.length ||
      x < 0 ||
      x >= maze[0].length ||
      maze[y][x] === 1
    ) {
      continue;
    }

    if (visited[y][x]) {
      continue;
    }

    visited[y][x] = true;
    steps.push([y, x]);

    if (y === end[0] && x === end[1]) {
      found = true;
      break;
    }

    const neighbors = [
      [y - 1, x],
      [y + 1, x],
      [y, x - 1],
      [y, x + 1],
    ];

    for (const [ny, nx] of neighbors) {
      if (ny < 0 || ny >= maze.length || nx < 0 || nx >= maze[0].length) {
        continue;
      }

      if (maze[ny][nx] === 1) {
        continue;
      }

      if (visited[ny][nx]) {
        continue;
      }

      parents[ny][nx] = [y, x];
      queue.push([ny, nx]);
    }
  }

  if (found) {
    let cur = end;
    while (cur !== null) {
      path.push(cur);
      cur = parents[cur[0]][cur[1]];
    }
  }

  return [path.reverse(), steps];
};

function aStarMazeSolver(maze: number[][], start: number[], end: number[]) {}

function stepColor(curTime: number, stepTime: number) {
  const timeCap = animationElapsedCap;
  const elapsed = curTime - stepTime;

  let c = [...animationColorOld];
  if (elapsed <= timeCap) {
    for (let i = 0; i < c.length; i++) {
      const deltaC = animationColorRecent[i] - animationColorOld[i];
      c[i] += deltaC * (((timeCap - elapsed) * 1.0) / timeCap);
    }
  }

  return toRGBString(c);
}

function drawMaze(
  el: HTMLCanvasElement,
  maze: number[][],
  steps: number[][] = [],
  time: number = 0,
  path: number[][] = []
) {
  const targetRes = 2400;
  const scaler = Math.ceil(
    Math.min(targetRes / maze[0].length, targetRes / maze.length)
  );
  el.width = maze[0].length * scaler;
  el.height = maze.length * scaler;

  const ctx = el.getContext("2d");
  ctx.reset();
  ctx.imageSmoothingEnabled = false;

  for (let y = 0; y < maze.length; y++) {
    for (let x = 0; x < maze[y].length; x++) {
      if (maze[y][x] === 1) {
        ctx.fillStyle = toRGBString(wallColor);
        ctx.fillRect(x * scaler, y * scaler, scaler, scaler);
      }
    }
  }

  for (let i = 0; i < time && i < steps.length; i++) {
    ctx.fillStyle = stepColor(time, i + 1);
    ctx.fillRect(steps[i][1] * scaler, steps[i][0] * scaler, scaler, scaler);
  }

  for (let i = 0; i < path.length; i++) {
    ctx.fillStyle = toRGBString(animationSolvedColor);
    ctx.fillRect(path[i][1] * scaler, path[i][0] * scaler, scaler, scaler);
  }

  if (debugMode) {
    for (let y = 0; y < maze.length; y++) {
      for (let x = 0; x < maze[y].length; x++) {
        ctx.fillStyle = "magenta";
        ctx.font = "10px sans-serif";
        ctx.fillText(`${y},${x}`, x * scaler + 5, y * scaler + 15);
      }
    }
  }
}

function setupCanvas(el: HTMLCanvasElement) {
  el.width = 200;
  el.height = 200;
}

let animationTimeoutId: number | null = null;
let animationActiveStep: number = 0;
function animateMaze(
  el: HTMLCanvasElement,
  maze: number[][],
  steps: number[][],
  time: number = 0,
  speed: number = 100,
  path: number[][] = []
) {
  animationActiveStep = time;
  drawMaze(el, maze, steps, time, time <= steps.length ? [] : path);
  if (time <= steps.length + animationElapsedCap) {
    animationTimeoutId = setTimeout(() => {
      animateMaze(el, maze, steps, time + stepsPerFrame, speed, path);
    }, speed);
  }
}

function stopMazeAnimation() {
  if (animationTimeoutId) {
    clearTimeout(animationTimeoutId);
    animationTimeoutId = null;
  }
}

function resetMaze(el: HTMLCanvasElement, maze: number[][]) {
  stopMazeAnimation();
  animationActiveStep = 0;
  drawMaze(el, maze);
}

async function init() {
  const mazeRaw = await fetch("./maze_2.json");
  const maze = await mazeRaw.json();
  maze[searchStart[0]][searchStart[1]] = 0;
  maze[searchEnd[0]][searchEnd[1]] = 0;

  const canvasEl = document.getElementById("maze-canvas") as HTMLCanvasElement;
  setupCanvas(canvasEl);
  resetMaze(canvasEl, maze);

  let sol: number[][][] = [[], []];

  if (solver === "dfs") {
    sol = dfsMazeSolver(maze, searchStart, searchEnd);
  } else if (solver === "bfs") {
    sol = bfsMazeSolver(maze, searchStart, searchEnd);
  }

  let [path, steps] = sol;

  const startBtn = document.getElementById("start-btn");
  const stopBtn = document.getElementById("stop-btn");
  const resetBtn = document.getElementById("reset-btn");

  startBtn.addEventListener("click", () => {
    animateMaze(
      canvasEl,
      maze,
      steps,
      animationActiveStep,
      animationSpeed,
      path
    );
  });

  stopBtn.addEventListener("click", () => {
    stopMazeAnimation();
  });

  resetBtn.addEventListener("click", () => {
    resetMaze(canvasEl, maze);
  });
}

init();
