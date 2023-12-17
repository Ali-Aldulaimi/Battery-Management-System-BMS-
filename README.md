# Embedded-Systems-Programming-and-Project

                             TABLE OF CONTENT
    1. Overview
    2. Features
    3. Hardware Requirements
    4. Usage
    5. Disclaimer

# 1. Overview
This code repository holds the STM32 neucleo program for a Battery Management System (BMS) created to keep tabs on and control the well-being and condition of a battery pack. 
The system relies on the various BMS functions, with a primary emphasis on monitoring State of Charge (SOC), State of Health (SOH), and safeguarding against issues like overcurrent, overcharge, and overdischarge. 
It's important to mention that this code exclusively works with the STM32 neucleo.
For transferring of data we have used Modbus RTU protocol with USB making the communication between Master and Slave device.

# 2. Features

SOC Calculation: Monitors and calculates the State of Charge of the battery.
SOH Calculation: Determines the State of Health of the battery based on internal resistance.
Protection Circuits: Includes overcurrent, overcharge, and overdischarge protection.
Data Storage:we have used personal Database and showed data in visulised form.
Data Transferr: we have used Modbus RTU protocol to transfer data between Master and Slave device over USB.

# 3. Hardware Requirements

* Microcontroller STM32 neucleo
* Differential Amplifier
* Multiplexer
* Mosfets
* Shunt resistor
* External circuitry for voltage and current measurement
* USB using Modbus RTU protocol

# 4. Usage

Initialization: The BMS is initialized with the BatteryManagement function, setting up various parameters like temperature limits, shunt resistor value, and protection settings.
SOC and SOH Calculation: The SOC_Calc and SOH_Calc functions are responsible for calculating the State of Charge and State of Health, respectively.
Data Storage: The SOC, SOH, and Depth of Discharge (DOD) values are stored in EEPROM for persistence.
Protection Mechanisms: The code includes functions to handle overcurrent situations and to adjust the battery capacity based on its degradation over time.
Communication: For communication, We have used Modbus RTU protocol with usb to send and recieve data on request and response frame in which master request for a particular data and slave responds accordingly.

# 5. Disclaimer

This code is provided without any warranty. The authors are not responsible for any damage caused by the use of this code.
