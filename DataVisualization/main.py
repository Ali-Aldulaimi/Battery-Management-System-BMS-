from database import connect_to_database, clear_table, insert_data
from serial_operations import initialize_serial, send_request_frame
from datetime import datetime, timezone, timedelta
from modbus_frames import *

local_timezone = timezone(timedelta(hours=2))
mydb = connect_to_database()
if mydb.is_connected():
    print("Connected to the database")

cursor = mydb.cursor()

ser = initialize_serial()
clear_table(cursor)
while True:
    # Generate and send all the request frames
    MCU_Temp = get_MCU_Temp_frame()
    lm35_Temp = get_lm35_temp_frame()
    CellVoltage_1 = get_CellVoltage_1_frame()
    CellVoltage_2 = get_CellVoltage_2_frame()
    CellVoltage_3 = get_CellVoltage_3_frame()
    CellVoltage_4 = get_CellVoltage_4_frame()
    BatteryCurrent = get_BatteryCurrent_frame()

    
    Date_Time = datetime.now(local_timezone)
    Date = Date_Time.strftime('%Y-%m-%d')  # Format for date
    Time = Date_Time.strftime('%H:%M:%S')  # Format for time
    print ("Time",Time)
    print ("Date",Date)

    sql = "INSERT INTO Battery_state (Date, Time, lm35_Temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3, CellVoltage_4, BatteryCurrent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


    LM35_TEMP= send_request_frame(ser,lm35_Temp)
    print("LM35_TEMP:",LM35_TEMP)

    MCU_TEMP = send_request_frame(ser,MCU_Temp)
    print("MCU_TEMP:",MCU_TEMP)
    
    CELL_1 = send_request_frame(ser,CellVoltage_1)
    print("CELL_1:",CELL_1)
    
    CELL_2 = send_request_frame(ser,CellVoltage_2)
    print("CELL_2:",CELL_2)
    
    CELL_3 = send_request_frame(ser,CellVoltage_3)
    print("CELL_3:",CELL_3)
    
    CELL_4 = send_request_frame(ser,CellVoltage_4)
    print("CELL_4:",CELL_4)
    
    BATTERYCURRENT = send_request_frame(ser,BatteryCurrent)
    print("BATTERYCURRENT:", BATTERYCURRENT)
    
    values = (Date, Time, LM35_TEMP, MCU_TEMP, CELL_1, CELL_2, CELL_3, CELL_4, BATTERYCURRENT)
    
    
    insert_data(cursor, sql, values)
    mydb.commit()

# Close connections
if mydb.is_connected():
    cursor.close()
    mydb.close()

ser.close()
