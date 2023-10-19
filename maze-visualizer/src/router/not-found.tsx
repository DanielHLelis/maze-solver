import styled from "@emotion/styled";
import { Typography } from "@mui/joy";

export function NotFound() {
  return (
    <Container>
      <Typography level="h1" color="danger">
        404
      </Typography>
      <Typography level="h4">Página não encontrada 😢</Typography>
    </Container>
  );
}

const Container = styled.div`
  width: 100vw;
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;
