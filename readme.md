# Month-End Close AI Agent 🧾🤖

This is a finance automation tool designed to assist with month-end close analysis by:
- Comparing monthly P&L reports
- Automatically calculating and flagging favorable/unfavorable variances
- Categorizing accounts using a chart of accounts

---

## 📊 What It Does

✔️ Compares two months of P&L data (May vs June, for example)  
✔️ Calculates dollar and percent variance  
✔️ Flags whether each change is favorable, unfavorable, or neutral  
✔️ Integrates with a chart of accounts to classify Revenue vs Expense  
✔️ Saves a clean summary to a CSV file for AI or reporting use  
✔️ (Coming soon) GPT-powered narrative explanations  

---

## ⚙️ How to Use

### 1. Clone the Repo
```bash
git clone https://github.com/cgoranov/Corporate-Finance-AI-Agent.git
cd month_end_agent
```
### 2. Set Up a Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate        # On Windows
pip install -r requirements.txt
```
### 3. Run Script
```bash
python main.py
```

### This will:

Load May and June P&L data

Merge in the chart of accounts

Calculate variances

Output a CSV summary and print a clean table to the terminal

🧠 Sample Output
| Account |   Type  | Amount_May |  Amount_June	| Variance | % Variance |   Status   | 
|---------|---------|------------|--------------|----------|------------|------------|
| Revenue |	Revenue |	50000	 |    47000	    |  -3000   |    -6.0%	| Unfavorable|
|  COGS	  | Expense	|   20000	 |    19000	    |   1000   |	 5.0%	|  Favorable |
|Marketing| Expense	|    5000	 |     8000	    |  -3000   |   -60.0%	| Unfavorable|

## 🔮 Roadmap
 Add OpenAI GPT integration for automatic written explanations

 Add Streamlit dashboard interface

 Allow multi-month comparisons (not just May vs June)

 Add account grouping and department-level rollups

 
 