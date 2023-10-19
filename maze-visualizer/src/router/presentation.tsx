import { Deck, Slide, Heading, DefaultTemplate } from "spectacle";

export function Presentation() {
  return (
    <Deck template={<DefaultTemplate />}>
      <Slide>
        <Heading>Welcome to Spectacle</Heading>
      </Slide>
    </Deck>
  );
}
