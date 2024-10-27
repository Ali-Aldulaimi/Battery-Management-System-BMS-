def get_MCU_Temp_frame():
    return bytes([0x04, 0x04, 0x00, 0x01, 0x00, 0x01, 0x60, 0x5F])

def get_lm35_temp_frame():
    return bytes([0x04, 0x04, 0x00, 0x02, 0x00, 0x01, 0x90, 0x5F])

def get_CellVoltage_1_frame():
    return bytes([0x04, 0x04, 0x00, 0x03, 0x00, 0x01, 0xC1, 0x9F])

def get_CellVoltage_2_frame():
    return bytes([0x04, 0x04, 0x00, 0x04, 0x00, 0x01, 0x70, 0x5E])

def get_CellVoltage_3_frame():
    return bytes([0x04, 0x04, 0x00, 0x05, 0x00, 0x01, 0x21, 0x9E])

def get_CellVoltage_4_frame():
    return bytes([0x04, 0x04, 0x00, 0x06, 0x00, 0x01, 0xD1, 0x9E])

def get_BatteryCurrent_frame():
    return bytes([0x04, 0x04, 0x00, 0x07, 0x00, 0x01, 0x80, 0x5E])