A full-stack finance tracker web application that helps users manage their income and expenses, visualize monthly statistics, and monitor budget limits with alerts.

🚀 Features

🔐 User Authentication

User registration & login

Secure password hashing

JWT-based authentication

💸 Expense & Income Management

Add income and expense transactions

Categorize transactions

View all transaction history

📊 Monthly Statistics

Monthly income vs expense chart

Backend-driven analytics API

🚨 Budget Alerts

Set monthly budget limits

Get alerts when expenses exceed budget

🧱 Full Stack Architecture

Frontend: React + Vite

Backend: Flask (Python)

Database: SQLite

Charts: Chart.js

Project Structure :

finance-tracker-fullstack/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   └── finance.db
│
└── frontend/
    ├── index.html
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── api.js
        └── components/
            ├── Login.jsx
            ├── Register.jsx
            ├── Dashboard.jsx
            └── MonthlyChart.jsx
