import mysql.connector
from mysql.connector import Error

def check_mysql_connection():
    """
    Connects to the MySQL database and verifies the connection.
    """
    connection = None
    try:
        # Connect using the 'mysql_native_password' plugin
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="4132",
            database="dbms",
            auth_plugin='mysql_native_password' # Add this line
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"✅ Connection to MySQL Server version {db_info} was successful!")
            print(f"You are connected to the database: 'dbms'")

    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("\nMySQL connection is closed.")

if __name__ == '__main__':
    check_mysql_connection()