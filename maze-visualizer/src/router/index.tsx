import { BrowserRouter, Routes, Route } from "react-router-dom";
import { NotFound } from "./not-found";

import "@fontsource/inter";
import { CssBaseline, CssVarsProvider, extendTheme } from "@mui/joy";
import { Presentation } from "./presentation";
import { Root } from "./root";

const theme = extendTheme({
  colorSchemes: {
    dark: {
      palette: {
        primary: {
          100: "#ffebf2",
          200: "#ff99c2",
          300: "##ff80ac",
          400: "##ff4d8b",
          500: "#ff206e",
          600: "#e60050",
          700: "#b3003e",
          800: "#80002d",
          900: "#4d001b",
        },
      },
    },
  },
});

export function EntryPoint() {
  return (
    <>
      <CssVarsProvider defaultMode="dark" theme={theme}>
        <CssBaseline />
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Root />} />
            <Route path="/presentation" element={<Presentation />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </BrowserRouter>
      </CssVarsProvider>
    </>
  );
}
