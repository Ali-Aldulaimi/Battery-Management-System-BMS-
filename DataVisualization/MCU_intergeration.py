import serial
import time
import mysql.connector
from datetime import datetime
#sys.path.append('/home/kali/BMS/DataVisualization/DB_Inserting.py')
#from DB_Inserting import insert_data_to_mysql
mydb = mysql.connector.connect(
    host="172.17.0.1",
    user="root",
    password="admin",
    database="BMS_DATA"
)
if mydb.is_connected():
    print("Connected to the database")

cursor = mydb.cursor()
truncate_query = "TRUNCATE TABLE Battery_state"
cursor.execute(truncate_query)
mydb.commit()
print('Table cleared')

# Open the serial communication with STM32
ser = serial.Serial('/dev/ttyACM0', 115200)

# Flush input to ensure no incomplete data is received
ser.flushInput()
time.sleep(0.1)


def extract_and_convert(frame):
    # Ensure the frame has enough bytes
    
        # Extract bytes 4 and 5
    bytes_to_convert = frame[3:5]
        
        # Convert bytes to an integer value
    decimal_value = int.from_bytes(bytes_to_convert, byteorder='big')
    return decimal_value
    

def send_request_frame(request_frame):
    ser.write(request_frame)
    print("Request frame is sent:", request_frame.hex())
    # Wait for response frame
    response_frame = ser.read(7)  # Adjust the number of bytes to read as needed
    print("Received frame:", response_frame.hex())

    decimal_value = extract_and_convert(response_frame)
    if decimal_value is not None:
        print("DATA IS STORED !")

    # Check if the received frame matches the expected format
    if response_frame and response_frame[0] == 0x04:
        print("Correct slave address")
        # Process the response data as needed
        # ...
    else:
        print("Wrong slave address")
    return decimal_value/10

    print("\n")

# Wait for synchronization
time.sleep(0.1)

while True:
    # Generate and send all the request frames
    MCU_Temp = bytes([0x04, 0x04, 0x00, 0x01, 0x00, 0x01, 0x60, 0x5F])
    lm35_temp = bytes([0x04, 0x04, 0x00, 0x02, 0x00, 0x01, 0x90, 0x5F])
    CellVoltage_1 = bytes([0x04, 0x04, 0x00, 0x03, 0x00, 0x01, 0xC1, 0x9F])
    CellVoltage_2 = bytes([0x04, 0x04, 0x00, 0x04, 0x00, 0x01, 0x70, 0x5E])
    CellVoltage_3 = bytes([0x04, 0x04, 0x00, 0x05, 0x00, 0x01, 0x21, 0x9E])
    CellVoltage_4 = bytes([0x04, 0x04, 0x00, 0x06, 0x00, 0x01, 0xD1, 0x9E])
    BatteryCurrent = bytes([0x04, 0x04, 0x00, 0x07, 0x00, 0x01, 0x80, 0x5E])


    Date_Time = datetime.now()
    # Separate date and time
    Date = Date_Time.strftime('%Y-%m-%d')
    Time = Date_Time.strftime('%H:%M:%S')
    print("date :",Date)
    print("Time :",Time)

    sql = "INSERT INTO Battery_state (Date, Time, Lm35_Temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3,CellVoltage_4, BatteryCurrent) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s)"
    
    
    LM35_TEMP= send_request_frame(lm35_temp)
    print("LM35_TEMP:",LM35_TEMP)

    MCU_TEMP = send_request_frame(MCU_Temp)
    print("MCU_TEMP:",MCU_TEMP)
    
    CELL_1 = send_request_frame(CellVoltage_1)
    print("CELL_1:",CELL_1)
    
    CELL_2 = send_request_frame(CellVoltage_2)
    print("CELL_2:",CELL_2)
    
    CELL_3 = send_request_frame(CellVoltage_3)
    print("CELL_3:",CELL_3)
    
    CELL_4 = send_request_frame(CellVoltage_4)
    print("CELL_4:",CELL_4)
    
    BATTERYCURRENT = send_request_frame(BatteryCurrent)
    print("BATTERYCURRENT:", BATTERYCURRENT)
    
    values = (Date,Time,LM35_TEMP, MCU_TEMP, CELL_1, CELL_2, CELL_3, CELL_4, BATTERYCURRENT)
    # Execute the query
    cursor.execute(sql, values)
    # Commit changes to the database
    mydb.commit()
    print('Values inserted successfully')

# Closing connections
if mydb.is_connected():
    cursor.close()
    mydb.close()
    print('MySQL connection closed')

ser.close()
print("Script ended")
