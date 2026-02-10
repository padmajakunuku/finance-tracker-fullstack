import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement);

export default function MonthlyChart({ data }) {
  return (
    <Bar
      data={{
        labels: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
        datasets: [
          { label: "Income", data: data.income },
          { label: "Expense", data: data.expense }
        ]
      }}
    />
  );
}
