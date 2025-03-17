import sqlite3

def get_user_data(username):
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Vulnerable SQL query (SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}'"

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    user_data = cursor.fetchall()

    # Close the connection
    conn.close()

    return user_data

# Example usage
username_input = input("Enter your username: ")
user_data = get_user_data(username_input)
print(user_data)
