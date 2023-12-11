def CRC16(nData):
    crc = 0xFFFF
    for byte in nData:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = crc >> 1
    return crc.to_bytes(2, byteorder='little')

# Given data
requested_data = bytes([0x04, 0x04, 0x00, 0x02, 0x00, 0x01])

# Calculate CRC
crc_value = CRC16(requested_data)


formatted_requested_data = ' '.join([f"{byte:02X}" for byte in requested_data])
formatted_crc_value = ' '.join([f"{byte:02X}" for byte in crc_value])
formatted_requested_frame = ' '.join([f"{byte:02X}" for byte in requested_data + crc_value])

print("Requested data1:", formatted_requested_data)
print("CRC is:", formatted_crc_value)
print("Requested frame is:", formatted_requested_frame)