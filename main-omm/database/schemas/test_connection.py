import mysql.connector
from config import config  # Import the config class from config.py

def test_database_connection():
    try:
        # Establish the connection using the details from config class
        connection = mysql.connector.connect(
            user=config.database_username,  # Reference class attributes correctly
            password=config.database_password,
            host=config.database_host,
            database=config.database
        )
        
        # Check if the connection is successful
        if connection.is_connected():
            print("Connection successful!")
        else:
            print("Failed to connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed.")

# Call the function to test the connection
test_database_connection()
