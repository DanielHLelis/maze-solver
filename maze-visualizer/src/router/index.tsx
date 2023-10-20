import { BrowserRouter, Routes, Route } from "react-router-dom";
import { NotFound } from "./not-found";

import "@fontsource/inter";
import { CssBaseline, CssVarsProvider } from "@mui/joy";
import { Presentation } from "./presentation";
import { Root } from "./root";

function SiteRoutes() {
  return (
    <CssVarsProvider defaultMode="dark">
      <CssBaseline />
      <Routes>
        <Route path="/" element={<Root />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </CssVarsProvider>
  );
}

export function EntryPoint() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/presentation" element={<Presentation />} />
        <Route path="*" element={<SiteRoutes />} />
      </Routes>
    </BrowserRouter>
  );
}
