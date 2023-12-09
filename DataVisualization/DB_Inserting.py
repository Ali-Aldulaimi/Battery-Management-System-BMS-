import mysql.connector

def insert_data_to_mysql(table, columns, data):
    try:
        # MySQL database configuration
        db_config = {
            'host': '172.17.0.1',
            'user': 'root',
            'password': 'admin',
            'database': 'BMS_DATAS'
        }

        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database')

        # Prepare the INSERT query
        cursor = conn.cursor()
        insert_query = (
            f"INSERT INTO {table} ({', '.join(columns)}) "
            f"VALUES ({', '.join(['%s'] * len(columns))})"
        )

        # Insert data into the database
        cursor.execute(insert_query, data)
        conn.commit()
        print('Data inserted successfully')

    except mysql.connector.Error as error:
        print('Error:', error)

    finally:
        # Close connections
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print('MySQL connection closed')
