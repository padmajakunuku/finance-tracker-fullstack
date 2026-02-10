import { useState } from "react";
import API from "../api";

export default function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const register = async () => {
    await API.post("/register", { username, password });
    alert("Registered! Now login.");
  };

  return (
    <div>
      <h2>Register</h2>
      <input placeholder="Username" onChange={e=>setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e=>setPassword(e.target.value)} />
      <button onClick={register}>Register</button>
    </div>
  );
}
