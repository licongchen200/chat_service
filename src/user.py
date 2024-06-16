from lib.conn import get_connection
from flask import jsonify
import datetime
import json


def get_user():
    conn = get_connection()

    cursor = conn.cursor()
    # Example query
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = {
            "id": row[0],
            "email": row[1],
            "first_name": row[2],
            "last_name": row[3]
        }
        users.append(user)
    print(json.dumps(users, indent=4))
    return json.dumps(users)


# get_user()

def create_user(email, firstname, lastname, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO users (email, first_name, last_name, password_hash) VALUES (%s, %s, %s, %s)"
        user_data = (email, firstname, lastname, password)
        cursor.execute(insert_query, user_data)
        conn.commit()
        return jsonify(user_data), 201
    except Exception as e:
        print(f"failed: {e}")
        data = {"error": f"message: {e}"}
        return jsonify(data)


# create_user("abc", "abc", "abc", "abc")
def delete_user(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (id,))
        conn.commit()
        print('success')
        data = {"status": "Success"}
        return jsonify(data)
    except Exception as e:
        data = {"error": f"message: {e}"}
        return jsonify(data)
# delete_user(5)
