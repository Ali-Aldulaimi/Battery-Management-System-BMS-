import serial
import mysql.connector

# Establish serial connection
ser = serial.Serial('/dev/ttyACM0', 115200)

def extract_numeric(string):
    return int(''.join(filter(str.isdigit, string)))

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
    # Initializing variables to store parsed values
    lm35_temp = None
    MCU_Temp = None
    CellVoltage_1 = None
    CellVoltage_2 = None
    CellVoltage_3 = None
    CellVoltage_4 = None
    BatteryCurrent = None

    while True:
        try:
            # Read data from serial port
            BatteryInfo = ser.readline().decode().strip()
            if BatteryInfo:
                print("Received:", BatteryInfo)
                data_lines = BatteryInfo.split('\n')
                
                # Parsing the data
                for line in data_lines:
                    if line.startswith('LM35 Temp'):
                        lm35_temp = extract_numeric(line.split(':')[1].strip())
                        print("lm35_temp is", lm35_temp)
                    if line.startswith('Internal Temp'):
                        MCU_Temp = extract_numeric(line.split(':')[1].strip())
                        print("MCUTemp ", MCU_Temp)
                    if line.startswith('Cell 1'):
                        CellVoltage_1 = extract_numeric(line.split(':')[1].strip())
                    if line.startswith('cell 2'):
                        CellVoltage_2 = extract_numeric(line.split(':')[1].strip())
                    if line.startswith('cell 3'):
                        CellVoltage_3 = extract_numeric(line.split(':')[1].strip())
                    if line.startswith('cell 4'):
                        CellVoltage_4 = extract_numeric(line.split(':')[1].strip())
                    if line.startswith('Current'):
                        BatteryCurrent = extract_numeric(line.split(':')[1].strip())
                
                if all((lm35_temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3, CellVoltage_4, BatteryCurrent)):
                # Cursor creation and data insertion
                # Cursor creation and data insertion
                    cursor = conn.cursor()
                    insert_query = (
                        "INSERT INTO Battery_state "
                        "(lm35_temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3, CellVoltage_4, BatteryCurrent) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    )
                
                    data = (lm35_temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3, CellVoltage_4, BatteryCurrent)

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
