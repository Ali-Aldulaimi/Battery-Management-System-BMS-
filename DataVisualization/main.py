from database import connect_to_database, clear_table, insert_data
from serial_operations import initialize_serial, send_request_frame
from datetime import datetime

mydb = connect_to_database()
if mydb.is_connected():
    print("Connected to the database")

cursor = mydb.cursor()

ser = initialize_serial()
clear_table(cursor)
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
    Date = Date_Time.strftime('%Y-%m-%d')
    Time = Date_Time.strftime('%H:%M:%S')

    sql = "INSERT INTO Battery_state (Date, Time, Lm35_Temp, MCU_Temp, CellVoltage_1, CellVoltage_2, CellVoltage_3, CellVoltage_4, BatteryCurrent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


    LM35_TEMP= send_request_frame(ser,lm35_temp)
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
