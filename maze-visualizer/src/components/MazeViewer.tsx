import { ComponentPropsWithoutRef, useEffect, useRef } from "react";
import { MazeCanvas } from "./MazeViewer.styles";
import styled from "@emotion/styled";

export type MazeMatrix = boolean[][];
export type MazeCoord = [number, number];

export interface Maze {
  matrix: MazeMatrix;

  start?: MazeCoord;
  end?: MazeCoord;

  height: number;
  width: number;
}

export type RGBColorArray =
  | [number, number, number]
  | [number, number, number, number];

export interface AnimationConfigs {
  wallColor: RGBColorArray;
  oldColor: RGBColorArray;
  recentColor: RGBColorArray;
  solutionColor: RGBColorArray;
  startColor?: RGBColorArray;
  endColor?: RGBColorArray;
  interpolationRange: number;
}

export interface AnimationState {
  configs: AnimationConfigs;
  playing: boolean;
  currentFrame: number;
  nextFrame: number;
  stepsPerFrame: number;
  updateExternalFrame: (frame: number) => void;
  setPlaying: (playing: boolean) => void;
}

export interface MazeViewerProps
  extends ComponentPropsWithoutRef<typeof MazeCanvas> {
  maze?: Maze;
  steps?: MazeCoord[];
  path?: MazeCoord[];

  resolution?: number;

  stepsPerFrame?: number;
  playing?: boolean;
  setPlaying?: (playing: boolean) => void;
  counter?: boolean;

  nextFrame?: number | null;
  setNextFrame?: (frame: number | null) => void;
  setCurrentFrame?: (frame: number) => void;

  configs?: AnimationConfigs;
}

export const defaultAnimationConfigs: AnimationConfigs = {
  wallColor: [255, 255, 255, 0.9],
  oldColor: [255, 32, 110],
  recentColor: [251, 255, 18],
  solutionColor: [65, 234, 212],
  startColor: [0, 255, 0],
  endColor: [255, 0, 0],
  interpolationRange: 250,
};

export function MazeViewer({
  maze,
  steps = [],
  path = [],
  configs = defaultAnimationConfigs,
  resolution = 2000,
  stepsPerFrame = 1,
  playing = false,
  counter = false,
  nextFrame,
  setCurrentFrame = () => {},
  setNextFrame = () => {},
  setPlaying = () => {},
  ...props
}: MazeViewerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animationRef = useRef<AnimationState>({
    configs,
    playing: false,
    currentFrame: 0,
    nextFrame: 0,
    stepsPerFrame: 0,
    updateExternalFrame: () => {},
    setPlaying: () => {},
  });

  // Control animation state outside of react
  useEffect(() => {
    animationRef.current = {
      ...animationRef.current,
      configs,
      playing: playing,
      nextFrame: nextFrame == null ? animationRef.current.nextFrame : nextFrame,
      stepsPerFrame,
      updateExternalFrame: setCurrentFrame,
      setPlaying,
    };

    if (nextFrame != null) {
      setNextFrame?.(null);
    }
  }, [
    playing,
    stepsPerFrame,
    nextFrame,
    setCurrentFrame,
    setNextFrame,
    setPlaying,
    configs,
  ]);

  // Configure the animation
  useEffect(() => {
    if (canvasRef.current == null) {
      return;
    }

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    if (ctx == null) {
      return;
    }

    ctx.reset();
    ctx.imageSmoothingEnabled = false;

    if (maze == null) {
      canvas.width = resolution;
      canvas.height = resolution;
      return;
    }

    const scaler = Math.ceil(
      Math.min(resolution / maze.height, resolution / maze.width)
    );
    const canvasWidth = maze.width * scaler;
    const canvasHeight = maze.height * scaler;
    canvas.width = canvasWidth;
    canvas.height = canvasHeight;

    let animationFrameId: number = -1;

    const render = () => {
      const state = animationRef.current;
      state.currentFrame = state.nextFrame;

      // Clear canvas
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);

      // Draw maze walls
      const wallColor = toRGBString(state.configs.wallColor);
      for (let y = 0; y < maze.matrix.length; y++) {
        for (let x = 0; x < maze.matrix[y].length; x++) {
          if (!maze.matrix[y][x]) {
            ctx.fillStyle = wallColor;
            ctx.fillRect(x * scaler, y * scaler, scaler, scaler);
          }
        }
      }

      // Draw steps
      for (let i = 0; i < state.currentFrame && i < steps.length; i++) {
        ctx.fillStyle = stepColor(
          state.currentFrame,
          i + 1,
          state.configs.interpolationRange,
          state.configs.oldColor,
          state.configs.recentColor
        );
        ctx.fillRect(
          steps[i][1] * scaler,
          steps[i][0] * scaler,
          scaler,
          scaler
        );
      }

      // Draw solution
      if (state.currentFrame >= steps.length) {
        for (let i = 0; i < path.length; i++) {
          ctx.fillStyle = toRGBString(state.configs.solutionColor);
          ctx.fillRect(
            path[i][1] * scaler,
            path[i][0] * scaler,
            scaler,
            scaler
          );
        }
      }

      if (state.configs.startColor && maze.start) {
        ctx.fillStyle = toRGBString(state.configs.startColor);
        ctx.fillRect(
          maze.start[1] * scaler,
          maze.start[0] * scaler,
          scaler,
          scaler
        );
      }

      if (state.configs.endColor && maze.end) {
        ctx.fillStyle = toRGBString(state.configs.endColor);
        ctx.fillRect(
          maze.end[1] * scaler,
          maze.end[0] * scaler,
          scaler,
          scaler
        );
      }

      // Print counter for debug
      if (counter) {
        ctx.fillStyle = "magenta";
        ctx.font = "42px sans-serif";
        ctx.fillText(
          `Step: ${Math.min(state.currentFrame, steps.length)}`,
          50,
          50
        );
      }

      // Setup next frame
      if (state.playing) {
        state.nextFrame = Math.min(
          state.currentFrame + state.stepsPerFrame,
          steps.length
        );
        if (state.currentFrame >= steps.length) {
          state.setPlaying(false);
        }
      }

      // Request next frame.
      state.updateExternalFrame(state.currentFrame);
      animationFrameId = requestAnimationFrame(render);
    };

    // Reset state
    if (animationRef.current) {
      animationRef.current.currentFrame = 0;
    }

    // Start animation loop
    render();

    // Cancel render on maze change
    return () => {
      cancelAnimationFrame(animationFrameId);
    };
  }, [maze, resolution, steps, path, counter]);

  return <StyledMaze size="400px" {...props} ref={canvasRef} />;
}

/* Utils */

function toRGBString(color: RGBColorArray) {
  if (color.length === 4) {
    return `rgba(${color[0]}, ${color[1]}, ${color[2]}, ${color[3]})`;
  }

  return `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
}

function stepColor(
  curTime: number,
  stepTime: number,
  interpRange: number,
  colorOld: RGBColorArray,
  colorRecent: RGBColorArray
) {
  const elapsed = curTime - stepTime;

  const c: RGBColorArray = [...colorOld];
  if (elapsed <= interpRange) {
    for (let i = 0; i < c.length; i++) {
      const deltaC = colorRecent[i] - colorOld[i];
      c[i] += deltaC * (((interpRange - elapsed) * 1.0) / interpRange);
    }
  }

  return toRGBString(c);
}

/* Styles */

const StyledMaze = styled(MazeCanvas)``;
