<<<<<<< HEAD:source/prototype.h
<<<<<<< HEAD

=======
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
=======
/*
 *
 *  Created on: Nov, 2023
 *      
 */

>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9:source/ADC_measurement.h
#ifndef PROTOTYPE_H_
#define PROTOTYPE_H_

#include "stm32l1xx.h"

#define TS_CAL1 *((uint16_t *)0x1FF800FA) // TS_CAL1 for the internal temp sensor
#define TS_CAL2 *((uint16_t *)0x1FF800FE) // TS_CAL2 for the internal temp sensor

#define Select_Pin_B 5		// multiplexer selection pin
#define Select_Pin_A 6		// multiplexer selection pin

<<<<<<< HEAD


=======
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
void Adc_set_up();

void Mux_set_up();

void MFET_set_up();

void Select_mux_pin(int channel);

float Read_Cell_Voltage(void);

<<<<<<< HEAD
int Internal_Temp_Read();

int LM35_Temp_read();
=======
float Read_shunt_resistor(void);

float Internal_Temp_Read();

float LM35_Temp_read();
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8

void delay_Ms(int delay);

#endif /* PROTOTYPE_H_ */
