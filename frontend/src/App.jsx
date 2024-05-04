import { useState, useEffect } from "react";
import Login from "./components/Login";
import SignUp from "./components/SignUp";

export default function App() {
  const [variable, setVariable] = useState();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hello")
      .then((response) => response.json())
      .then((data) => {
        setVariable(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    // Here you can send the form data to your backend or perform any other actions
    setVariable();
  };

  return (
    <div className="blah">
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" name="name" required />
        </div>
        <button type="submit">Submit</button>
      </form>
      <div>{variable}</div>
    </div>
  );
}
