import sqlite3
import json
def check_balance(mobile_no):
    conn = sqlite3.connect("telecom.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT users.name, usage.balance, usage.data_left_gb, usage.last_recharge_date
        FROM users
        JOIN usage ON users.user_id = usage.user_id
        WHERE users.mobile_no = ?
        """, 
        (mobile_no,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        user_data = {
            "name": result[0],
            "balance": result[1],
            "data_left_gb": result[2],
            "last_recharge_date": result[3]
        }
        return json.dumps(user_data, indent=4)  # Convert to JSON with formatting
    else:
        return json.dumps({"error": "User not found"}, indent=4)
