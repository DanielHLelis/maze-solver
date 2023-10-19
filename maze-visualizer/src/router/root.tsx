import {
  Box,
  Grid,
  Input,
  Option,
  Select,
  Slider,
  Stack,
  Typography,
} from "@mui/joy";
import { MazeViewer } from "../components/MazeViewer";

import maze from "../assets/maze-sample.json";
import { useState } from "react";

export function Root() {
  const [width, setWidth] = useState<number>(51);
  const [height, setHeight] = useState<number>(51);

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

      <Stack></Stack>

      {/* eslint-disable-next-line @typescript-eslint/ban-ts-comment */}
      {/* @ts-ignore */}
      <MazeViewer maze={maze} counter />
      <Grid container spacing={2} width="100%" columns={8}>
        <Grid sm={8}>
          <Typography level="h2">Preferências:</Typography>
        </Grid>
        <Grid sm={4}>
          <Typography gutterBottom>Altura: {height}</Typography>
          <Slider
            defaultValue={51}
            value={height}
            onChange={(e, v) => setHeight(v as number)}
            step={2}
            min={1}
            max={201}
            valueLabelDisplay="auto"
          />
        </Grid>
        <Grid sm={4}>
          <Typography gutterBottom>Largura: {width}</Typography>
          <Slider
            defaultValue={51}
            value={width}
            onChange={(e, v) => setWidth(v as number)}
            step={2}
            min={1}
            max={201}
            valueLabelDisplay="auto"
          />
        </Grid>
        <Grid sm={4}>
          <Typography gutterBottom>Gerador</Typography>
          <Select defaultValue="dfs">
            <Option value="dfs">DFS</Option>
          </Select>
        </Grid>
        <Grid sm={4}>
          <Typography gutterBottom>Seed</Typography>
          <Input defaultValue="seed feliz :)" />
        </Grid>
      </Grid>
    </Stack>
  );
}
