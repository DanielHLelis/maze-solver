import { useState } from "react";
import {
  Box,
  Button,
  Grid,
  Input,
  Option,
  Select,
  Slider,
  Stack,
  Typography,
} from "@mui/joy";
import { Maze, MazeCoord, MazeViewer } from "../components/MazeViewer";

import sample_maze from "../assets/sample.maze.json";
import sample_maze_sol from "../assets/sample.bfs.json";
import styled from "@emotion/styled";

interface MazeSolution {
  path: MazeCoord[];
  steps: MazeCoord[];
}

type MazeGenerator = "dfs" | "chaos-dfs" | "wilson";
type MazeSolver =
  | "dfs"
  | "dfs-euclidean"
  | "dfs-manhattan"
  | "bfs"
  | "rds"
  | "astar-euclidean"
  | "astar-manhattan"
  | "astar-dijkstra"
  | "bfirst-euclidean"
  | "bfirst-manhattan";

const MAX_SIZE = 501;

export function Root() {
  const [maze, setMaze] = useState<Maze>(sample_maze as Maze);
  const [loadingMatrix, setLoadingMatrix] = useState<boolean>(false);
  const [mazeSolution, setMazeSolution] = useState<MazeSolution>({
    path: sample_maze_sol.path as MazeCoord[],
    steps: sample_maze_sol.steps as MazeCoord[],
  });
  const [loadingSolution, setLoadingSolution] = useState<boolean>(false);

  /*
    Reproduction Settings
  */
  const [playing, setPlaying] = useState<boolean>(false);
  const [currentFrame, setCurrentFrame] = useState<number>(0);
  const [nextFrame, setNextFrame] = useState<number | null>(null);
  const [stepsPerFrame, setStepsPerFrame] = useState<number>(1);

  /* Solver Settings */
  const [solver, setSolver] = useState<MazeSolver>("bfs");
  const [solSeed, setSolSeed] = useState<string>("");

  /* Generator Settings */
  const [width, setWidth] = useState<number>(51);
  const [height, setHeight] = useState<number>(51);
  const [generator, setGenerator] = useState<MazeGenerator>("dfs");
  const [genSeed, setGenSeed] = useState<string>("");
  const [genP, setGenP] = useState<string | number>("");
  const [startLine, setStartLine] = useState<string | number>("");
  const [startCol, setStartCol] = useState<string | number>("");
  const [endLine, setEndLine] = useState<string | number>("");
  const [endCol, setEndCol] = useState<string | number>("");

  /* State Derivations */
  const solverHasSeed = solver === "rds";

  /* Actions */
  const handlePlayStop = () => {
    if (mazeSolution.steps.length === 0) return;
    setPlaying(!playing);
  };

  const handleReset = () => {
    setPlaying(false);
    setNextFrame(0);
  };

  const handleFrameSlider = (e: unknown, v: number | number[]) => {
    setCurrentFrame(v as number);
    setNextFrame(v as number);
  };

  const asyncHandleSolve = async (targetMaze?: Maze) => {
    if (!targetMaze) targetMaze = maze;

    let uri = `${import.meta.env.VITE_API_URL}/maze/solve/${solver}`;

    if (solSeed !== "") {
      uri += `?seed=${encodeURIComponent(solSeed)}`;
    }

    setLoadingSolution(true);

    try {
      const resp = await fetch(uri, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(targetMaze),
      });

      if (!resp.ok) {
        alert("Falha ao gerar labirinto");
        console.error(resp);
        return;
      }

      const mazeSolution = (await resp.json()) as MazeSolution;
      setMazeSolution(mazeSolution);
      setNextFrame(0);
    } catch (e) {
      alert("Falha ao gerar labirinto");
      console.error(e);
    } finally {
      setLoadingSolution(false);
    }
  };

  const asyncHandleGenerate = async () => {
    let uri = `${
      import.meta.env.VITE_API_URL
    }/maze/generate/${generator}/${width}/${height}/${encodeURIComponent(
      genSeed
    )}`;
    const args = [];

    if (startLine !== "" && startCol !== "") {
      args.push(`start=${startLine},${startCol}`);
    }

    if (endLine !== "" && endCol !== "") {
      args.push(`end=${endLine},${endCol}`);
    }

    if (genP !== "") {
      args.push(`p=${genP}`);
    }

    if (args.length > 0) {
      uri += `?${args.join("&")}`;
    }

    setLoadingMatrix(true);

    try {
      const resp = await fetch(uri);

      if (!resp.ok) {
        alert("Falha ao gerar labirinto");
        console.error(resp);
        return;
      }

      const maze = (await resp.json()) as Maze;
      setMaze(maze);
      setPlaying(false);
      setMazeSolution({ path: [], steps: [] });

      await asyncHandleSolve(maze);
    } catch (e) {
      alert("Falha ao gerar labirinto");
      console.error(e);
    } finally {
      setLoadingMatrix(false);
    }
  };

  const handleGenerate = () => {
    if (loadingMatrix) return;
    asyncHandleGenerate().then().catch(console.error);
  };

  const handleSolve = () => {
    if (loadingSolution) return;
    asyncHandleSolve().then().catch(console.error);
  };

  const handleGenP = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.value === "") {
      setGenP("");
      return;
    }

    const v = parseFloat(e.target.value);
    if (isNaN(v)) return;
    if (v < 0) return;
    if (v > 1) return;

    setGenP(e.target.value);
  };

  const positionHandler = (
    setter: (v: string | number) => void,
    cap: number = Number.POSITIVE_INFINITY
  ) => {
    return (e: React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.value === "") {
        setter("");
        return;
      }

      const v = parseInt(e.target.value);
      if (isNaN(v)) return;
      if (v < 0) return;
      if (v >= cap) return;

      setter(v);
    };
  };

  return (
    <Stack
      direction="column"
      alignItems="center"
      spacing={4}
      my={4}
      maxWidth="800px"
      px={4}
      mx="auto"
    >
      <Typography level="h1">A Maze Inc.</Typography>

      <StyledMaze
        maze={maze}
        counter={false}
        path={mazeSolution.path}
        steps={mazeSolution.steps}
        playing={playing}
        setPlaying={setPlaying}
        nextFrame={nextFrame}
        stepsPerFrame={stepsPerFrame}
        setNextFrame={setNextFrame}
        setCurrentFrame={setCurrentFrame}
      />

      <Grid container spacing={2} width="100%" columns={8}>
        <Grid xs={8}>
          <Stack>
            {mazeSolution.steps.length === 0 ? (
              <Typography level="h3" color="danger" textAlign="center">
                Nenhuma solução carregada
              </Typography>
            ) : (
              <>
                <Slider
                  value={currentFrame}
                  onChange={handleFrameSlider}
                  min={0}
                  max={mazeSolution.steps.length}
                  valueLabelDisplay="auto"
                />
                <Typography textAlign="center">
                  Iteração: {currentFrame} / {mazeSolution.steps.length}
                </Typography>
                <Typography textAlign="center">
                  Tamanho da solução: {mazeSolution.path.length}
                </Typography>
              </>
            )}
          </Stack>
        </Grid>
      </Grid>

      <Grid container spacing={2} width="100%" columns={8}>
        {/* Player controls */}
        <Grid xs={8} md={4}>
          <Grid container spacing={2} width="100%" columns={2}>
            <Grid xs={2}>
              <Typography level="h3">Controles</Typography>
            </Grid>
            <Grid xs={1}>
              <Button
                fullWidth
                onClick={handlePlayStop}
                disabled={mazeSolution.steps.length === 0}
              >
                {playing ? "Parar" : "Iniciar"}
              </Button>
            </Grid>
            <Grid xs={1}>
              <Button fullWidth onClick={handleReset}>
                Reiniciar
              </Button>
            </Grid>
            <Grid xs={2}>
              <Stack spacing={2}>
                <Typography gutterBottom>
                  Passos por quadro (velocidade): {stepsPerFrame}
                </Typography>
                <Box px={2}>
                  <Slider
                    defaultValue={1}
                    value={stepsPerFrame}
                    onChange={(e, v) => setStepsPerFrame(v as number)}
                    step={1}
                    min={1}
                    max={100}
                    valueLabelDisplay="auto"
                  />
                </Box>
              </Stack>
            </Grid>
          </Grid>
        </Grid>
        {/* Solution Controls */}
        <Grid xs={8} md={4}>
          <Grid container spacing={2} width="100%" columns={2}>
            <Grid xs={2}>
              <Typography level="h3">Estratégia de solução</Typography>
            </Grid>

            <Grid xs={2}>
              <Stack>
                <Typography gutterBottom>Algoritmo</Typography>
                <Select
                  value={solver}
                  onChange={(_e, v) => setSolver(v as MazeSolver)}
                >
                  <Option value="dfs">DFS</Option>
                  <Option value="dfs-euclidean">
                    DFS com heurística Euclidiana
                  </Option>
                  <Option value="dfs-manhattan">
                    DFS com heurística de Manhattan
                  </Option>
                  <Option value="bfs">BFS</Option>
                  <Option value="rds">Random Walk</Option>
                  <Option value="astar-euclidean">A* Euclidiano</Option>
                  <Option value="astar-manhattan">A* Manhattan</Option>
                  <Option value="astar-dijkstra">Dijkstra</Option>
                  <Option value="bfirst-euclidean">
                    Best-First Euclidiano
                  </Option>
                  <Option value="bfirst-manhattan">Best-First Manhattan</Option>
                </Select>
              </Stack>
              <Stack>
                <Typography gutterBottom>Seed</Typography>
                <Input
                  placeholder="Aleatório"
                  value={solverHasSeed ? solSeed : "Não aplicável"}
                  disabled={!solverHasSeed}
                  onChange={(e) => setSolSeed(e.target.value)}
                />
              </Stack>
            </Grid>

            <Grid xs={2}>
              <Button fullWidth onClick={handleSolve} loading={loadingSolution}>
                Gerar solução
              </Button>
            </Grid>
          </Grid>
        </Grid>
        {/* Labyrinth Controls */}
        <Grid xs={8} md={8}>
          <Grid container spacing={2} width="100%" columns={4}>
            <Grid xs={4}>
              <Typography level="h3">Labirinto</Typography>
            </Grid>

            <Grid xs={4} md={2}>
              <Typography gutterBottom>Altura: {height}</Typography>
              <Slider
                defaultValue={51}
                value={height}
                onChange={(e, v) => setHeight(v as number)}
                step={2}
                min={5}
                max={MAX_SIZE}
                valueLabelDisplay="auto"
              />
            </Grid>
            <Grid xs={4} md={2}>
              <Typography gutterBottom>Largura: {width}</Typography>
              <Slider
                defaultValue={51}
                value={width}
                onChange={(e, v) => setWidth(v as number)}
                step={2}
                min={5}
                max={MAX_SIZE}
                valueLabelDisplay="auto"
              />
            </Grid>

            <Grid xs={4} sm={2}>
              <Typography gutterBottom>Algoritmo</Typography>
              <Select
                value={generator}
                onChange={(_e, v) => setGenerator(v as MazeGenerator)}
              >
                <Option value="dfs">DFS Aleatório</Option>
                <Option value="chaos-dfs">DFS do Caos</Option>
                <Option value="wilson">Wilson</Option>
              </Select>
            </Grid>
            <Grid xs={2} sm={1}>
              <Typography gutterBottom>Seed</Typography>
              <Input
                placeholder="Aleatório"
                value={genSeed}
                onChange={(e) => setGenSeed(e.target.value)}
              />
            </Grid>
            <Grid xs={2} sm={1}>
              <Typography gutterBottom>P</Typography>
              <Input
                placeholder="0.05"
                disabled={generator !== "chaos-dfs"}
                value={generator !== "chaos-dfs" ? "Não aplicável" : genP}
                onChange={handleGenP}
              />
            </Grid>

            <Grid xs={4} sm={2}>
              <Typography gutterBottom>
                Posição Inicial (Linha, Coluna)
              </Typography>
              <Stack direction="row" spacing={2}>
                <Input
                  placeholder="Aleatório"
                  type="number"
                  value={startLine}
                  onChange={positionHandler(setStartLine)}
                />
                <Input
                  placeholder="Aleatório"
                  type="number"
                  value={startCol}
                  onChange={positionHandler(setStartCol)}
                />
              </Stack>
            </Grid>

            <Grid xs={4} sm={2}>
              <Typography gutterBottom>
                Posição Final (Linha, Coluna)
              </Typography>
              <Stack direction="row" spacing={2}>
                <Input
                  placeholder="Aleatório"
                  type="number"
                  value={endLine}
                  onChange={positionHandler(setEndLine)}
                />
                <Input
                  placeholder="Aleatório"
                  type="number"
                  value={endCol}
                  onChange={positionHandler(setEndCol)}
                />
              </Stack>
            </Grid>

            <Grid xs={4}>
              <Button
                fullWidth
                onClick={handleGenerate}
                loading={loadingMatrix}
              >
                Gerar labirinto
              </Button>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Stack>
  );
}

const StyledMaze = styled(MazeViewer)`
  max-width: 720px;
  max-height: 600px;
`;
