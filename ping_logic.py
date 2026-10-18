import sqlite3
import pandas as pd

# 1. Database connected 
conn = sqlite3.connect('ping_pnl_data.db')

# 2. SQL Query - PingP&L core Business Logic
query = """
SELECT 
    notifications_received as Pings,
    COUNT(user_id) as Total_Users,
    SUM(churned) as Churned_Users,
    ROUND((SUM(churned) * 100.0 / COUNT(user_id)), 2) as Churn_Rate_Pct,
    (COUNT(user_id) * notifications_received * 40) as Gross_Revenue,
    (SUM(churned) * 350) as Churn_Loss_CAC,
    ((COUNT(user_id) * notifications_received * 40) - (SUM(churned) * 350)) as Net_PnL
FROM user_metrics
GROUP BY notifications_received
ORDER BY notifications_received;
"""

# 3. Query run
df_result = pd.read_sql_query(query, conn)

print("--- PingP&L Business Analysis ---")
print(df_result.to_string(index=False))

conn.close()
