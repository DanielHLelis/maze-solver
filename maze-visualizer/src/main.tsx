import React from "react";
import ReactDOM from "react-dom/client";
import { EntryPoint } from "./router";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <EntryPoint />
  </React.StrictMode>
);
