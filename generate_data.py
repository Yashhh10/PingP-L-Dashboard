import pandas as pd
import numpy as np
import sqlite3

# 1. 1000 users ka dummy data generate karte hain
np.random.seed(42)
n_users = 1000

data = {
    'user_id': range(1, n_users + 1),
    # Users ko randomly 1 se 7 ke beech "Pings" (notifications) mil rahe hain
    'notifications_received': np.random.randint(1, 8, n_users)
}

df = pd.DataFrame(data)

# 2. Asli Business Logic: Agar 3 se zyada ping gaye, toh user gussa hoke app delete karega (Churn)
def calculate_churn(notifs):
    if notifs <= 2:
        return np.random.choice([0, 1], p=[0.95, 0.05]) # Sirf 5% delete karenge
    elif notifs == 3:
        return np.random.choice([0, 1], p=[0.85, 0.15]) # 15% delete karenge
    elif notifs <= 5:
        return np.random.choice([0, 1], p=[0.40, 0.60]) # 60% gusse me delete kar denge
    else:
        return np.random.choice([0, 1], p=[0.10, 0.90]) # 90% pakka delete karenge

df['churned'] = df['notifications_received'].apply(calculate_churn)

# 3. Data ko local SQLite Database me save karte hain
conn = sqlite3.connect('ping_pnl_data.db')
df.to_sql('user_metrics', conn, if_exists='replace', index=False)
conn.close()

print("PingP&L Data Engine Ready! ping_pnl_data.db file ban gayi hai.")