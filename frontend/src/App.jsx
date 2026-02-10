import { useState } from "react";
import Login from "./components/Login";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  if (!token) {
    return (
      <>
        <Register />
        <Login setToken={setToken} />
      </>
    );
  }

  return <Dashboard token={token} />;
}
