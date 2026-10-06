# 🚀 PingP&L: AI-Driven Notification Guardrail System
> *Preventing marketing teams from burning cash through over-notification.*

**Live Dashboard:** (https://pingp-l-dashboard-1.streamlit.app/)

---

## 🎯 The Project Problem
Every B2C growth team faces a silent killer: **The Notification Paradox**. 
More notifications drive short-term engagement and revenue, but past a certain threshold, they trigger user irritation, app uninstalls (churn), and massive Customer Acquisition Costs (CAC). 

I built **PingP&L** to solve this exact business problem. It’s an end-to-end analytics product that calculates the exact "Tipping Point" where push notifications stop generating profit and start destroying unit economics.

---

## 📊 How It Works (The Unit Economics Breakdown)
The system analyzes data based on a strict business formula:
* **The Reward:** Every successful push notification order yields **₹40 in Gross Revenue**.
* **The Penalty:** Every user lost due to high frequency incurs a **₹350 CAC replacement cost**.
* **The Tipping Point:** Using SQL aggregations, the dashboard highlights the exact notification count where Net P&L crashes from green (profitable) to red (loss-making).

---

## 🧠 Core Features & Architecture
1. **Synthetic Data Pipeline (`generate_data.py`)**: 
   * Engineered a robust 1,000-user dataset simulating real-world behavioral patterns, tracking notification frequency against user churn.
2. **SQL Analytics Engine (`ping_logic.py`)**: 
   * Leveraged advanced grouping and calculations to compute cohort-wise Net Profit/Loss dynamically.
3. **Interactive UI (`app.py`)**: 
   * Built a clean, executive-ready dashboard using **Streamlit** and **Plotly** with conditional color-scaling (Green for profit zones, Red for loss thresholds).
4. **AI-Powered Operations Directive (Gemini API)**: 
   * Integrated **Google Gemini AI** to act as a virtual Chief Business Officer (CBO). With a single click, it reads the live SQL data output and auto-generates strict, actionable strategy memos for the marketing team.

---

## 🛠️ Tech Stack
* **Language & Core:** Python, Pandas, NumPy
* **Database & Queries:** SQLite, SQL
* **Frontend & Visualization:** Streamlit, Plotly Express
* **Artificial Intelligence:** Google Generative AI (`gemini-3.8-flash`)
* **Deployment & DevOps:** GitHub, Streamlit Cloud, Environment Secrets Management.
---

👨‍💻 Developed By

Yash | Aspiring Data Analyst / Product Manager
