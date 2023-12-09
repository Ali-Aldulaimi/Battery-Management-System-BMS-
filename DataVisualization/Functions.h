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