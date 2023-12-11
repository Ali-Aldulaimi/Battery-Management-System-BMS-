import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="172.17.0.1",
        user="root",
        password="admin",
        database="BMS_DATA"
    )

def clear_table(cursor):
    truncate_query = "TRUNCATE TABLE Battery_state"
    cursor.execute(truncate_query)

def insert_data(cursor, sql, values):
    cursor.execute(sql, values)
