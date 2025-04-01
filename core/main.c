/* Necessary system libraries */
#include "stdbool.h"
#include "stdint.h"

#include "hw_memmap.h"
#include "sysctl.h"
#include "gpio.h"

/**
 * Application entry point
 */
int main(void)
{

    /* Enable GPIOE clock */
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOE);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOE));

    GPIOPinTypeGPIOOutput(GPIO_PORTE_BASE, GPIO_PIN_3);
    GPIOPinTypeGPIOOutput(GPIO_PORTE_BASE, GPIO_PIN_1);

    while(1)
    {

        /* Set state for LED's */
        GPIOPinWrite(GPIO_PORTE_BASE, GPIO_PIN_1, GPIO_PIN_1);

        for (int i = 0; i < 1000000; i++) {
            
        }

        /* Set state for LED's */
        GPIOPinWrite(GPIO_PORTE_BASE, GPIO_PIN_1, 0x00);

        for (int i = 0; i < 1000000; i++) {
            
        }

}

    /* Never reached! */
	return 0;
}