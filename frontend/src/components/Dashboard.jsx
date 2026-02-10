import { useEffect, useState } from "react";
import API from "../api";
import MonthlyChart from "./MonthlyChart";

export default function Dashboard({ token }) {
  const headers = { Authorization: `Bearer ${token}` };

  const [transactions, setTransactions] = useState([]);
  const [stats, setStats] = useState({ income: [], expense: [] });
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [type, setType] = useState("expense");

  const load = async () => {
    const t = await API.get("/transactions", { headers });
    const s = await API.get("/monthly-stats", { headers });

    let income = Array(12).fill(0);
    let expense = Array(12).fill(0);

    s.data.income.forEach(i => income[i[0]-1] = i[1]);
    s.data.expense.forEach(e => expense[e[0]-1] = e[1]);

    setTransactions(t.data);
    setStats({ income, expense });
  };

  useEffect(() => { load(); }, []);

  const add = async () => {
    await API.post("/transaction",
      { amount, category, type },
      { headers }
    );
    load();
  };

  return (
    <div>
      <h2>Dashboard</h2>

      <input placeholder="Amount" onChange={e=>setAmount(e.target.value)} />
      <input placeholder="Category" onChange={e=>setCategory(e.target.value)} />
      <select onChange={e=>setType(e.target.value)}>
        <option value="expense">Expense</option>
        <option value="income">Income</option>
      </select>
      <button onClick={add}>Add</button>

      <MonthlyChart data={stats} />

      <ul>
        {transactions.map(t => (
          <li key={t.id}>
            {t.type} ₹{t.amount} - {t.category}
          </li>
        ))}
      </ul>
    </div>
  );
}
