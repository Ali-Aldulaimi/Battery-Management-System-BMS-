<<<<<<< HEAD

=======
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
#ifndef PROTOTYPE_H_
#define PROTOTYPE_H_

#include "stm32l1xx.h"

#define TS_CAL1 *((uint16_t *)0x1FF800FA) // TS_CAL1 for the internal temp sensor
#define TS_CAL2 *((uint16_t *)0x1FF800FE) // TS_CAL2 for the internal temp sensor

#define Select_Pin_B 5
#define Select_Pin_A 6

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

void USART2_Init(void);

void USART2_write(char data);

char USART2_read(void);

void delay_Ms(int delay);

void display(char* buf);

#endif /* PROTOTYPE_H_ */
