import styled from "@emotion/styled";
import {
  Deck,
  Slide,
  Heading,
  DefaultTemplate,
  SpectacleThemeOverrides,
  Text,
  Box,
  ListItem,
} from "spectacle";

import maze from "../assets/sample.maze.json";
import maze_bfs from "../assets/sample.bfs.json";
import maze_dfs from "../assets/sample.dfs.json";
import maze_dij from "../assets/sample.dij.json";
import maze_euc from "../assets/sample.euc.json";
import maze_man from "../assets/sample.man.json";
import maze_rnd from "../assets/sample.rnd.json";

import { Maze, MazeCoord, MazeViewer } from "../components/MazeViewer";
import { Button, Grid, Input, Slider, Stack, Typography } from "@mui/joy";
import { useState } from "react";

interface MazeSolution {
  steps: MazeCoord[];
  path: MazeCoord[];
}

const theme: SpectacleThemeOverrides = {
  colors: {
    primary: "#ffffff",
    secondary: "#ff206e",
    tertiary: "#0c0f0a",
    quaternary: "#41ead4",
    quinary: "#fbff12",
  },
};

export function Presentation() {
  return (
    <Deck template={<DefaultTemplate />} theme={theme}>
      <Slide>
        <Heading color="quaternary">A Maze Inc.</Heading>
        <Heading fontSize="h3">
          O impacto de diferentes estratégias de busca na resolução de
          labirintos
        </Heading>

        <Text fontSize="2rem">
          Feito por:
          <br />
          <Authors>
            <li>Bernardo "Maurício" Tameirão</li>
            <li>Lelis "Lelis" Lelis</li>
            <li>Pedro "Krules" (Não mais)Gamer</li>
            <li>Samuel "Zeronev" Nickelodeon</li>
            <li>Gustavo "Wadas" Wadas</li>
          </Authors>
        </Text>
      </Slide>
      <Slide>
        <Heading>Motivação e Objetivos</Heading>
      </Slide>
      <Slide>
        <Heading>Gerando Labirintos</Heading>
      </Slide>
      <Slide>
        <Heading>Resolvendo Labirintos</Heading>
      </Slide>
      <Slide>
        <Heading>Visualizando</Heading>
        <MazeSlide maze={maze as Maze} solution={maze_bfs as MazeSolution}>
          <Stack spacing={2} alignItems="center">
            <Heading fontSize="h3" color="quaternary">
              Estratégia: BFS
            </Heading>
          </Stack>
        </MazeSlide>
      </Slide>
      <Slide>
        <Heading>Resultados</Heading>
      </Slide>
    </Deck>
  );
}

interface MazeSlideProps {
  maze: Maze;
  solution: MazeSolution;
  initialStepsPerFrame?: number;
  children?: React.ReactNode;
}

function MazeSlide({
  maze,
  solution,
  initialStepsPerFrame = 4,
  children,
}: MazeSlideProps) {
  const [playing, setPlaying] = useState<boolean>(false);
  const [currentFrame, setCurrentFrame] = useState<number>(0);
  const [nextFrame, setNextFrame] = useState<number | null>(
    solution.steps.length
  );
  const [stepsPerFrame, setStepsPerFrame] =
    useState<number>(initialStepsPerFrame);

  const handlePlayStop = () => {
    if (solution.steps.length === 0) return;
    setPlaying(!playing);
  };

  const handleReset = () => {
    setNextFrame(0);
    setPlaying(true);
  };

  const handleFrameSlider = (e: unknown, v: number | number[]) => {
    setCurrentFrame(v as number);
    setNextFrame(v as number);
  };

  const handleStepsPerFrame = (e: React.ChangeEvent<HTMLInputElement>) => {
    const v = parseInt(e.target.value);

    if (isNaN(v)) return;
    if (v < 1) return;
    if (v > 100) return;

    setStepsPerFrame(v);
  };

  return (
    <Grid container spacing={4} columns={3}>
      <Grid xs={2}>{children}</Grid>
      <Grid xs={1}>
        <Grid container spacing={2} mt={-8} columns={3}>
          <Grid xs={3}>
            <Slider
              value={currentFrame}
              onChange={handleFrameSlider}
              min={0}
              max={solution.steps.length}
              valueLabelDisplay="auto"
            />
          </Grid>

          <Grid
            xs={3}
            alignItems="center"
            display="flex"
            flexDirection="column"
          >
            <MazeSlideViewer
              maze={maze}
              steps={solution.steps}
              path={solution.path}
              playing={playing}
              setPlaying={setPlaying}
              nextFrame={nextFrame}
              stepsPerFrame={stepsPerFrame}
              setNextFrame={setNextFrame}
              setCurrentFrame={setCurrentFrame}
            />
          </Grid>

          <Grid xs={1}>
            <Button
              fullWidth
              onClick={handlePlayStop}
              disabled={solution.steps.length === 0}
            >
              {playing ? "Parar" : "Iniciar"}
            </Button>
          </Grid>
          <Grid xs={1}>
            <Button fullWidth onClick={handleReset}>
              Reiniciar
            </Button>
          </Grid>
          <Grid xs={1}>
            <Input
              type="number"
              value={stepsPerFrame}
              onChange={handleStepsPerFrame}
            />
          </Grid>
          <Grid xs={3}>
            <Typography textAlign="center">
              Iteração: {currentFrame} / {solution.steps.length} ; Solução:{" "}
              {solution.path.length}
            </Typography>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
}

const MazeSlideViewer = styled(MazeViewer)``;

const Authors = styled.ul`
  font-size: 1.5rem;
  list-style: none;
`;
