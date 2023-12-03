import serial
import mysql.connector

# Establish serial connection
ser = serial.Serial('/dev/ttyACM0', 115200)

# MySQL database configuration
db_config = {
    'host': '172.17.0.1',
    'user': 'root',
    'password': 'admin',
    'database': 'BMS_DATA'
}

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print('Connected to MySQL database')

    # Clear the table before inserting new data
    cursor = conn.cursor()
    truncate_query = "TRUNCATE TABLE Battery_state"
    cursor.execute(truncate_query)
    conn.commit()
    cursor.close()
    print('Table cleared')

    print("Script started")

    while True:
        try:
            # Read data from serial port
            BatteryInfo = ser.readline().decode().strip()
            if BatteryInfo:
                print("Received:", BatteryInfo)

                # Cursor creation and data insertion
                cursor = conn.cursor()
                insert_query = (
                    "INSERT INTO Battery_state "
                    "(BatteryInfo) "
                    "VALUES (%s)"
                )
                data = (BatteryInfo,)

                cursor.execute(insert_query, data)
                conn.commit()

                print('Values inserted successfully')

        except KeyboardInterrupt:
            break

        except mysql.connector.Error as error:
            print('Error:', error)

finally:
    # Closing connections
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection closed')
    ser.close()
    print("Script ended")
