import styled from "@emotion/styled";
import {
  Deck,
  Slide,
  Heading,
  DefaultTemplate,
  SpectacleThemeOverrides,
  Text,
  UnorderedList,
  ListItem,
} from "spectacle";
import { QRCodeSVG } from "qrcode.react";

import maze from "../assets/sample.maze.json";
import maze_d from "../assets/sample.maze-dfs.json";
import maze_wilson from "../assets/sample.maze-wilson.json";

import maze_bfs from "../assets/sample.bfs.json";
import maze_dfs from "../assets/sample.dfs.json";
import maze_dfsm from "../assets/sample.dfsm.json";
import maze_man from "../assets/sample.aman.json";
import maze_rnd from "../assets/sample.rnd.json";
import maze_bman from "../assets/sample.bman.json";

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

const gitLink = "https://github.com/DanielHLelis/maze-solver";
const siteLink = "https://maze.usp.lelis.dev/";

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
        <UnorderedList>
          <ListItem>Resolver labirintos programáticamente</ListItem>
          <ListItem>
            Comparar os diferentes algoritmos e suas características
          </ListItem>
          <ListItem>
            Gerar labirintos aleatoriamente para testar os algoritmos
          </ListItem>
          <ListItem>Visualizar os labirintos e suas soluções</ListItem>
        </UnorderedList>
      </Slide>
      <Slide>
        <Heading>O processo</Heading>
        <UnorderedList>
          <ListItem>
            Criamos ferramentas para visualizar os labirintos e suas soluções
          </ListItem>
          <ListItem>
            Testamos diversos algoritmos de busca para compará-los e conferir se
            nossas expectativas se alinhavam
          </ListItem>
          <ListItem>Analisar os dados para entender o que obtemos</ListItem>
        </UnorderedList>
      </Slide>
      <Slide>
        <Heading style={{ marginBottom: 0, paddingBottom: 0 }}>
          Gerando Labirintos
        </Heading>
        <Stack alignItems="center" justifyContent="center" height="100%">
          <Grid container columns={3} spacing={4}>
            <Grid xs={1}>
              <AlgorithmTitle>DFS Aleatório</AlgorithmTitle>
              <MazeSlide maze={maze_d as Maze} />
            </Grid>
            <Grid xs={1}>
              <AlgorithmTitle>DFS Ale. c/ Deleções</AlgorithmTitle>
              <MazeSlide maze={maze as Maze} />
            </Grid>
            <Grid xs={1}>
              <AlgorithmTitle>Wilson's</AlgorithmTitle>
              <MazeSlide maze={maze_wilson as Maze} />
            </Grid>
          </Grid>
        </Stack>
      </Slide>
      <Slide>
        <Stack alignItems="center" justifyContent="center" height="100%">
          <Heading style={{ marginBottom: 0 }}>Resolvendo Labirintos</Heading>
          <Heading style={{ marginTop: 0 }} color="quaternary">
            Buscas Cegas
          </Heading>
          <Text>Sempre possíveis, nem sempre as mais eficientes!</Text>
        </Stack>
      </Slide>
      <Slide>
        <Grid container columns={3} spacing={4}>
          <Grid xs={1}>
            <AlgorithmTitle>BFS</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_bfs as MazeSolution}
            />
          </Grid>
          <Grid xs={1}>
            <AlgorithmTitle>DFS</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_dfs as MazeSolution}
            />
          </Grid>
          <Grid xs={1}>
            <AlgorithmTitle>Random Walk</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_rnd as MazeSolution}
            />
          </Grid>
        </Grid>
      </Slide>
      <Slide>
        <Stack alignItems="center" justifyContent="center" height="100%">
          <Heading style={{ marginBottom: 0 }}>Resolvendo Labirintos</Heading>
          <Heading style={{ marginTop: 0 }} color="quaternary">
            Buscas Informadas
          </Heading>
          <Text style={{ textAlign: "center" }}>
            Quando temos informações do nosso objetivo, podemos podar caminhos
            para melhorar a eficiência.
          </Text>
        </Stack>
      </Slide>
      <Slide>
        <Grid container columns={3} spacing={4}>
          <Grid xs={1}>
            <AlgorithmTitle>A* (Manhattan)</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_man as MazeSolution}
            />
          </Grid>
          <Grid xs={1}>
            <AlgorithmTitle>Best-First (Manhattan)</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_bman as MazeSolution}
            />
          </Grid>
          <Grid xs={1}>
            <AlgorithmTitle>DFS c/ Manhattan</AlgorithmTitle>
            <MazeSlide
              maze={maze as Maze}
              solution={maze_dfsm as MazeSolution}
            />
          </Grid>
        </Grid>
      </Slide>
      <Slide>
        <Heading>Resultados - Iterações</Heading>
        <Stack direction="row" spacing={2} justifyContent="center">
          <GraphImg src="/it-005.png" />
          <GraphImg src="/it-020.png" />
        </Stack>
      </Slide>
      <Slide>
        <Heading>Resultados - Iterações</Heading>
        <UnorderedList>
          <ListItem>Redução de iterações na busca informada</ListItem>
          <ListItem>
            Contraste entre solução ótima e o número de iterações
          </ListItem>
        </UnorderedList>
      </Slide>
      <Slide>
        <Heading>Resultados - Caminho</Heading>
        <Stack direction="row" spacing={2} justifyContent="center">
          <GraphImg src="/sol-005.png" />
          <GraphImg src="/sol-020.png" />
        </Stack>
      </Slide>
      <Slide>
        <Heading>Resultados - Caminho</Heading>
        <UnorderedList>
          <ListItem>A* mostrou-se o mais eficiente para solução ótima</ListItem>
          <ListItem>
            Best-First apresentou o melhor balanço entre o número de iterações e
            o caminho encontrado.
          </ListItem>
          <ListItem>
            DFS mostrou-se o pior algoritmo para solução ótima (muitos
            zig-zags).
          </ListItem>
        </UnorderedList>
      </Slide>
      <Slide>
        <Heading>Resultados - Ratio</Heading>
        <Stack direction="row" spacing={2} justifyContent="center">
          <GraphImg src="/ratio-005.png" />
          <GraphImg src="/ratio-020.png" />
        </Stack>
      </Slide>
      <Slide>
        <Heading>FIM :)</Heading>

        <Grid container spacing={6} columns={2}>
          <Grid xs={1}>
            <Typography level="h1" textAlign="center" gutterBottom>
              <a href={gitLink} target="_blank" rel="noreferrer">
                GitHub
              </a>
            </Typography>
            <QRCodeSVG value={gitLink} width="100%" height="300px" />
          </Grid>
          <Grid xs={1}>
            <Typography level="h1" textAlign="center" gutterBottom>
              <a href={gitLink} target="_blank" rel="noreferrer">
                Site
              </a>
            </Typography>
            <QRCodeSVG value={siteLink} width="100%" height="300px" />
          </Grid>
        </Grid>
      </Slide>
    </Deck>
  );
}

interface MazeSlideProps {
  maze: Maze;
  solution?: MazeSolution;
  initialStepsPerFrame?: number;
}

function MazeSlide({
  maze,
  solution,
  initialStepsPerFrame = 4,
}: MazeSlideProps) {
  const [playing, setPlaying] = useState<boolean>(false);
  const [currentFrame, setCurrentFrame] = useState<number>(0);
  const [nextFrame, setNextFrame] = useState<number | null>(
    solution?.steps.length ?? 0
  );
  const [stepsPerFrame, setStepsPerFrame] =
    useState<number>(initialStepsPerFrame);

  const handlePlayStop = () => {
    if (solution?.steps.length === 0) return;
    setPlaying(!playing);
  };

  const handleReset = () => {
    setNextFrame(0);
    setPlaying(true);
  };

  const handleFrameSlider = (_e: unknown, v: number | number[]) => {
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
    <Grid container spacing={2} columns={3}>
      {solution && (
        <Grid xs={3}>
          <Slider
            value={currentFrame}
            onChange={handleFrameSlider}
            min={0}
            max={solution.steps.length}
            valueLabelDisplay="auto"
          />
        </Grid>
      )}

      <Grid xs={3} alignItems="center" display="flex" flexDirection="column">
        <MazeSlideViewer
          maze={maze}
          steps={solution?.steps || []}
          path={solution?.path || []}
          playing={playing}
          setPlaying={setPlaying}
          nextFrame={nextFrame}
          stepsPerFrame={stepsPerFrame}
          setNextFrame={setNextFrame}
          setCurrentFrame={setCurrentFrame}
        />
      </Grid>

      {solution && (
        <>
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
        </>
      )}
    </Grid>
  );
}

const MazeSlideViewer = styled(MazeViewer)``;

const Authors = styled.ul`
  font-size: 1.5rem;
  list-style: none;
`;

const AlgorithmTitle = styled.h3`
  font-size: 2rem;
  text-align: center;
  color: ${theme.colors?.quaternary};
  margin-bottom: 0;
`;

const GraphImg = styled.img`
  max-width: 600px;
  height: 100%;
`;
