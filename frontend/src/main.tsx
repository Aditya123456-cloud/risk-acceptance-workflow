import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./style.css";
import ListPage from "./pages/ListPage";

const App = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<h1>Welcome</h1>} />
      <Route path="/list" element={<ListPage />} />
    </Routes>
  </BrowserRouter>
);

ReactDOM.createRoot(document.getElementById("app")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
