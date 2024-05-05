import { useState, useEffect } from "react";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import Main from "./pages/Main/Main";
import Analysis from "./pages/Analysis/Analysis";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";

export default function App() {
  return (
    <div className="blah">
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/analysis" element={<Analysis />} />
        </Routes>
      </Router>
    </div>
  );
}
