#include <stdio.h>
#include <wiringPi.h>

int main(void){
	const int led_pin1=1;//red
	const int led_pin2=26;//yellow
	const int led_pin3=23;//green
	wiringPiSetup();
	int t_high;
	int i=0;
	for(i=0;i<5;i++){
		pinMode(led_pin1,PWM_OUTPUT);
		pinMode(led_pin2,OUTPUT);
		pinMode(led_pin3,PWM_OUTPUT);
		pwmWrite(led_pin1,0);
		digitalWrite(led_pin2,0);
		pwmWrite(led_pin3,0);
		for(t_high=0;t_high*50<=1000;t_high++){
			pwmWrite(led_pin1,t_high*50);
			delay(100);
		}
		delay(1000);
		pinMode(led_pin1,OUTPUT);
		digitalWrite(led_pin1,HIGH);
		pinMode(led_pin2,PWM_OUTPUT);
		for(t_high=0;t_high*50<=1000;t_high++){
			pwmWrite(led_pin2,t_high*50);
			delay(100);
		}
		delay(1000);
		for(t_high=0;t_high*50<=1000;t_high++){
			pwmWrite(led_pin3,t_high*50);
			delay(100);
		}
		delay(1000);
		pinMode(led_pin1,PWM_OUTPUT);
		pwmWrite(led_pin1,1000);
		for(t_high=20;t_high*50>=0;t_high--){
			pwmWrite(led_pin1,t_high*50);
			pwmWrite(led_pin3,t_high*50);
			delay(100);
		}
		pinMode(led_pin1,OUTPUT);
		pinMode(led_pin2,OUTPUT);
		pinMode(led_pin3,OUTPUT);
		for(t_high=0;t_high<3;t_high++){
			digitalWrite(led_pin3,LOW);
			digitalWrite(led_pin1,HIGH);
			delay(1000);
			digitalWrite(led_pin1,LOW);
			digitalWrite(led_pin2,HIGH);
			delay(1000);
			digitalWrite(led_pin2,LOW);
			digitalWrite(led_pin3,HIGH);
			delay(1000);
		}
		digitalWrite(led_pin3,LOW);
		delay(1000);
	}
}
