#include<avr/io.h>
#include<util/delay.h>
#include<compat/deprecated.h>
#include <avr/interrupt.h>


unsigned char rcvd[4];
unsigned char count=0;

void spi_init(void)
{
SPCR=0x79;			// SPE, DORD, MSTR, CPOL, SPR1 Set
SPSR=0x01;			 
DDRB|=0xaf;
cbi(PORTB,4);
}



void interrupt(void)
{
cbi(DDRB,2);
// PORTB |= ;
MCUCR=0x00;
MCUCR=0x00;
cbi(GICR,5);
sbi(MCUCSR,6);
sbi(GIFR,5);
sbi(GICR,5);
sei();
}

ISR(SPI_STC_vect)
{
count++;
}


void interpret(void)
{
PORTC=0xf0;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				
			
switch (rcvd[2])
{
case 0x80 : PORTC=0x80;break;
case 0x40 : PORTC=0x40;break;
case 0x20 : PORTC=0x20;break;
case 0x10 : PORTC=0x10;break;
default : break;
}

for (int i=0;i<4;i++)
{
rcvd[i]=0x00;
}
}

ISR(INT2_vect)
{
PORTC|=0x08;
switch(count)
{
case 1 :	 PORTC=SPDR;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				
				SPDR=0x42;break;
case 2 :	 PORTC=SPDR;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				SPDR=0x00;
			break;
case 3 :	 PORTC=SPDR;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				
			SPDR=0x00;break;
case 4 :	PORTC=SPDR;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				
			 SPDR=0x00;	break;
default:     PORTC=0xff;
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				_delay_ms(250);
				
			break;
}

//while(!(SPSR & (1<<SPIF)));
if (count==5) {interpret();count=0;}
else rcvd[count]=SPDR;

}


void port_init(void)
{
DDRA=0xff;
PORTA=0xff;
DDRB=0x00;
PORTB=0xff;
DDRC=0xff;
PORTC=0x00;
DDRD=0x00;
PORTD=0xff;
}

int main(void)
{
port_init();
interrupt();
spi_init();


while(1)
{
if (count==0)
	{
	SPDR=0x01;
	//while(!(SPSR & (1<<SPIF)));
	}
}
}
