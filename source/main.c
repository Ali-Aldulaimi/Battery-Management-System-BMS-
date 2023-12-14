<<<<<<< HEAD


/* Includes */
#include <stddef.h>
#include <stdio.h>
#include "prototype.h"
#include "nucleo152start.h"

int main(void)
{

=======
/* Includes */
#include <stddef.h>
#include <stdio.h>
#include "stm32l1xx.h"
#include "nucleo152start.h"

#include "ADC_measurement.h"
#include "battery_protect.h"
#include "USART2_DMA_Config.h"
#include "modbus.h"

int flag = 0;		// global flag for MODBUS activities
int main(void) {

	__disable_irq();		//global disable IRQs, M3_Generic_User_Guide p135.
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
	/* Configure the system clock to 32 MHz and update SystemCoreClock */
	SetSysClock();
	SystemCoreClockUpdate();
	USART2_Init();
<<<<<<< HEAD
<<<<<<< HEAD
=======
	// enable USART2 interrupt
	USART2->CR1 |= 0x0020;			//enable RX interrupt
	NVIC_EnableIRQ(USART2_IRQn); 	//enable interrupt in NVIC
	__enable_irq();				//global enable IRQs, M3_Generic_User_Guide p135

>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
	Adc_set_up();
	Mux_set_up();
	MFET_set_up();
=======
	DMA_Init();
	__enable_irq();		//global enable IRQs, M3_Generic_User_Guide p135

	Adc_set_up();	// set up ADC for measurements
	Mux_set_up();	// set up for the multiplexer
	MFET_set_up();	// set up C_FET and D_FET
>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9

<<<<<<< HEAD
	int Int_temp = 0;
	int LM35_temp = 0;

	char buf[200];	// contain transfering data

	float cell_vol[4] = {0, 0, 0, 0};
	float battery_vol = 0;
	float shunt_resistor = 0.01;
	float current = 0;
=======
	float Int_temp = 0;
	float LM35_temp = 0;
	float cell_vol[4] = { 0, 0, 0, 0 };
	float shunt = 0;

<<<<<<< HEAD
	MODBUS Mod;

	char buf[200];	// contain transfering data

>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
=======
	MODBUS Mod;		// modbus object
>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9

	// reset pin A and B of the multipler
	GPIOA->ODR &= ~(1 << Select_Pin_B);
	GPIOA->ODR &= ~(1 << Select_Pin_A);

	/* Infinite loop */
<<<<<<< HEAD
	while (1)
	{

		Int_temp = Internal_Temp_Read();
		delay_Ms(200);
		LM35_temp = LM35_Temp_read();
		delay_Ms(200);
=======
	while (1) {

		switch (flag) {
		case 0:
			break;

		case 1:
			//display("slave address is correct");
			Modbus_routine(&Mod);
			Restart_DMA();
			Reset_DMA_RX_BUFFER();
			USART2->CR1 |= (1 << 2);	////re-enable USART2 RE
			flag = 0;
			break;

		case 2:
			//display("wrong address");
			Restart_DMA();
			Reset_DMA_RX_BUFFER();
			USART2->CR1 |= (1 << 2);	//re-enable USART2 RE
			flag = 0;
			break;
		}
		shunt = Read_shunt_resistor();
		delay_Ms(200);
		Mod.shunt = (int) (shunt * 10);	// update shunt value for modbus protocol
		Current_check(shunt);// check for batter protection (baterry_protect.c)

		Int_temp = Internal_Temp_Read();
		delay_Ms(200);
		Mod.int_temp = (int) (Int_temp * 10);// update int_temp value for modbus protocol
		INT_Temperature_check(Int_temp);// check for batter protection (baterry_protect.c)

		LM35_temp = LM35_Temp_read();
		delay_Ms(200);
<<<<<<< HEAD
		LM35_temperature_check(LM35_temp);

>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
=======
		Mod.LM35_temp = (int) (LM35_temp * 10);	// update LM35_temp value for modbus protocol
		LM35_temperature_check(LM35_temp);// check for batter protection (baterry_protect.c)
>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9

		for (int i = 0; i < 4; i++) {
			Select_mux_pin(i);		// select pin in multiplexer
			cell_vol[i] = Read_Cell_Voltage();
			delay_Ms(200);
<<<<<<< HEAD
<<<<<<< HEAD
			battery_vol += cell_vol[i];
		}

		current = battery_vol / shunt_resistor;
		sprintf(buf, "LM35 Temp: %d C \n\rInternal Temp: %d C\n\rCell 1 (mV): %d\n\rcell 2 (mV): %d\n\rcell 3 (mV): %d\n\rcell 4 (mV): %d\n\rCurrent (mA): %d\n\r"
				, LM35_temp, Int_temp
				, (int)cell_vol[0], (int)cell_vol[1]
				, (int)cell_vol[2], (int)cell_vol[3]
				, (int)current);
		battery_vol = 0;


		display(buf);
		delay_Ms(1000);
=======
=======
			Mod.cell_vol[i] = (int) (cell_vol[i] * 10);	// update cells voltage value for modbus protocol
>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9
		}
		Batt_cells_check(cell_vol);	// check for batter protection (baterry_protect.c)

		BMS_Operation();// batter protection activities after sensing all the value, (battery_protect.c)

		delay_Ms(1000);

<<<<<<< HEAD
#else
		Int_temp = 20;
		INT_Temperature_check((float)Int_temp);
		LM35_temp = 25;
		LM35_temperature_check((float)LM35_temp);

		float cel = 2400.5;
		cell_vol[0] = cel;
		cell_vol[1] = cel;
		cell_vol[2] = cel;
		cell_vol[3] = cel;
		Batt_cells_check (cell_vol);
		shunt = 1200.5;
		Current_check(shunt);
		BMS_Operation();
		display("complete testing");
		delay_Ms(1000);
		delay_Ms(1000);
#endif
>>>>>>> df77f3b343039f117b5eaae631e49b60736c3cb8
=======
>>>>>>> e7ae8b521914911ac8255b10856389300dc514a9
	}
	return 0;
}
