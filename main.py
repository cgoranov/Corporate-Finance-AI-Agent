import pandas as pd

# === Step 1: Load Data ===
may = pd.read_excel("May Income Statement.xlsx")
june = pd.read_excel("June Income Statement.xlsx")
chart = pd.read_excel("Chart of Accounts.xlsx")

# === Step 2: Normalize Account Names for Reliable Merging ===
may["Account"] = may["Account"].str.strip().str.lower()
june["Account"] = june["Account"].str.strip().str.lower()
chart["Account"] = chart["Account"].str.strip().str.lower()

# === Step 3: Merge May and June on Account ===
merged = pd.merge(may, june, on="Account", suffixes=("_May", "_June"))

# === Step 4: Merge in Account Types from Chart of Accounts ===
merged = pd.merge(merged, chart, on="Account", how="left")

# === Step 5: Warn About Any Unmatched Accounts ===
unmatched = merged[merged["Type"].isna()]
if not unmatched.empty:
    print("\n⚠️ Warning: These accounts were not matched to the chart of accounts:")
    print(unmatched["Account"].unique())

# === Step 6: Variance Logic Based on Account Type ===
def calculate_adjusted_variance(row):
    change = row["Amount_June"] - row["Amount_May"]
    account_type = str(row["Type"]).lower()

    if account_type in ["revenue", "income"]:
        return change  # More is good
    elif account_type == "expense":
        return -change  # More is bad
    else:
        return 0  # Neutral (or unknown type)

merged["Variance"] = merged.apply(calculate_adjusted_variance, axis=1)
merged["% Variance"] = (merged["Variance"] / merged["Amount_May"]) * 100

# Add Status Column
merged["Status"] = merged["Variance"].apply(
    lambda x: "Favorable" if x > 0 else ("Unfavorable" if x < 0 else "No Change")
)

# === Step 7: Optional - Filter Out Net Income or Others ===
summary = merged[~merged["Account"].str.contains("net income", case=False)]

# === Step 8: Output Results ===
print("\n📊 P&L Variance Summary:\n")
print(summary[["Account", "Type", "Amount_May", "Amount_June", "Variance", "% Variance", "Status"]])

# Save to CSV
summary.to_csv("pnl_variance_summary.csv", index=False)
