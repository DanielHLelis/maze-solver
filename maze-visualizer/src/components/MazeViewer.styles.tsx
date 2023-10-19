import styled from "@emotion/styled";

export interface MazeCanvasProps {
  size?: string;
}

export const MazeCanvas = styled.canvas<MazeCanvasProps>`
  width: max-content;
  height: max-content;

  max-width: ${(props) => props.size ?? "800px"};
  max-height: ${(props) => props.size ?? "800px"};
`;
