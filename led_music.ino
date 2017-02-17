void color(int *, int *, int *, int[3], int[3], int[3]);
void color(int *, int *, int *, int[3], int[3], int[3], int[3], int[3], int[3], int[3]);
void stretch(int *, int *, int *);
int choice=0;
int analogPin = 0; // MSGEQ7 OUT
int strobePin = 2; // MSGEQ7 STROBE
int resetPin = 4; // MSGEQ7 RESET
int spectrumValue[7];
int pin_R1=11;
int pin_G1=10;
int pin_B1=9;
int pin_R2=3;
int pin_G2=5;
int pin_B2=6;
int r_t[3]={215, 0, 0};
int g_t[3]={0, 200, 0};
int b_t[3]={0, 0, 200};
int o_t[3]={255, 185, 0};
int w_t[3]={255, 255, 255};
int bl_t[3]={0, 0, 0};
int p_t[3]={138, 0, 128};
int lb_t[3]={135, 206, 250};
int y_t[3]={255, 255, 0};
int mag_t[3]={255, 0, 255};
int bv_t[3]={138, 43, 226};
int ind_t[3]={75, 0, 130};
int viol_t[3]={218, 110, 218};
int bk_t[3]={0, 0, 0,};
int br_t[3]={129, 59, 19};
int lime_t[3]={0, 255, 0};
int cyan_t[3]={0, 255, 255};
int t_1[3]={0};
int t_2[3]={0};
int t_3[3]={0};
int t_4[3]={0};
int t_5[3]={0};
int t_6[3]={0};
int t_7[3]={0};
int t_8[3]={0};

// MSGEQ7 OUT pin produces values around 50-80
// when there is no input, so use this value to
// filter out a lot of the chaff.
int filterValue = 80;
// LED pins connected to the PWM pins on the Arduino
char new_theme='N';
void setup()
{
  Serial.begin(9600);
  // Read from MSGEQ7 OUT
  pinMode(analogPin, INPUT);
  // Write to MSGEQ7 STROBE and RESET
  pinMode(strobePin, OUTPUT);
  pinMode(resetPin, OUTPUT);
   
  // Set analogPin's reference voltage
  analogReference(DEFAULT); // 5V
 
  // Set startup values for pins
  digitalWrite(resetPin, LOW);
  digitalWrite(strobePin, HIGH);
  //theme_fcn=&color;
}
 
void loop()
{
  // Set reset pin low to enable strobe
  digitalWrite(resetPin, HIGH);
  digitalWrite(resetPin, LOW);
  
 if(Serial.available()>0)
 {
    new_theme=Serial.read();        
    switch (new_theme)
		{
		case 'T':
			
			memcpy(t_1, o_t, 3*sizeof *o_t);
                        memcpy(t_2, g_t, 3*sizeof *r_t);
                        memcpy(t_3, b_t, 3*sizeof *b_t);
                        memcpy(t_4, r_t, 3*sizeof *g_t);
			choice=4;
                        break;
		case 'S':
			memcpy(t_1, w_t, 3*sizeof *o_t);
                        memcpy(t_2, p_t, 3*sizeof *o_t);
                        memcpy(t_3, lb_t, 3*sizeof *o_t);
                        memcpy(t_4, bk_t, 3*sizeof *o_t);
                        choice=4;
                        break;
                case 'W':
                        memcpy(t_1, bk_t, 3*sizeof *o_t);
                        memcpy(t_2, bv_t, 3*sizeof *o_t);
                        memcpy(t_3, g_t, 3*sizeof *o_t);
                        memcpy(t_4, p_t, 3*sizeof *o_t);
                        choice=4;
                        break;
                case 'B':
                        memcpy(t_1, lb_t, 3*sizeof *o_t);
                        memcpy(t_2, b_t, 3*sizeof *o_t);
                        memcpy(t_3, y_t, 3*sizeof *o_t);
                        memcpy(t_4, w_t, 3*sizeof *o_t);
                        choice=4;
                        break; 
                case 'D':
                        memcpy(t_1, b_t, 3*sizeof *o_t);
                        memcpy(t_2, bk_t, 3*sizeof *o_t);
                        memcpy(t_3, p_t, 3*sizeof *o_t);
                        memcpy(t_4, r_t, 3*sizeof *o_t);
                        choice=4;
                        break;          
                case 'A':
                        memcpy(t_1, cyan_t, 3*sizeof *o_t);
                        memcpy(t_2, mag_t, 3*sizeof *o_t);
                        memcpy(t_3, lime_t, 3*sizeof *o_t);
                        memcpy(t_4, w_t, 3*sizeof *o_t);
                        choice=4;
                        break;
                case 'I':
                        memcpy(t_1, w_t, 3*sizeof *o_t);
                        memcpy(t_2, lb_t, 3*sizeof *o_t);
                        memcpy(t_3, b_t, 3*sizeof *o_t);
                        memcpy(t_4, cyan_t, 3*sizeof *o_t);
                        choice=4;
                        break;          
                case 'F':
                        memcpy(t_1, o_t, 3*sizeof *o_t);
                        memcpy(t_2, y_t, 3*sizeof *o_t);
                        memcpy(t_3, r_t, 3*sizeof *o_t);
                        memcpy(t_4, bk_t, 3*sizeof *o_t);
                        choice=4;
                        break;
      
                case 'R':
                        memcpy(t_1, r_t, 3*sizeof *o_t);
                        memcpy(t_2, o_t, 3*sizeof *o_t);
                        memcpy(t_3, y_t, 3*sizeof *o_t);
                        memcpy(t_4, g_t, 3*sizeof *o_t);
                        memcpy(t_5, lb_t, 3*sizeof *o_t);
                        memcpy(t_6, b_t, 3*sizeof *o_t);
                        memcpy(t_7, viol_t, 3*sizeof *o_t);
                        memcpy(t_8, b_t, 3*sizeof *o_t);
                        choice=8;
                        break;
                case 'P':
                        memcpy(t_1, bv_t, 3*sizeof *o_t);
                        memcpy(t_2, bk_t, 3*sizeof *o_t);
                        memcpy(t_3, viol_t, 3*sizeof *o_t);
                        memcpy(t_4, p_t, 3*sizeof *o_t);
                        choice=4;
                        break;
		default:
			Serial.print('R');
		}
Serial.flush();
Serial.write(new_theme);
delay(50);
} 
  // Get all 7 spectrum values from the MSGEQ7
  for (int i = 0; i < 7; i++)
  {
    digitalWrite(strobePin, LOW);
    delayMicroseconds(30); // Allow output to settle
 
    spectrumValue[i] = analogRead(analogPin);
 
    //  any value above 1023 or below filterValue
    spectrumValue[i] = constrain(spectrumValue[i], filterValue, 1023);

 
    // Remap the value to a number between 0 and 255
    spectrumValue[i] = map(spectrumValue[i], filterValue, 1023, 0, 255);
    // Remove serial stuff after debugging
    Serial.print(i);
    Serial.print("--------");
    Serial.print(spectrumValue[i]);
    Serial.print("\n");
    digitalWrite(strobePin, HIGH);
   }
   stretch(&spectrumValue[2], &spectrumValue[1], &spectrumValue[0]);
  stretch(&spectrumValue[4], &spectrumValue[5], &spectrumValue[3]);
   if(choice==4)
   {
    color(&spectrumValue[2], &spectrumValue[1], &spectrumValue[0], t_1, t_2, t_3, t_4);
    color(&spectrumValue[4], &spectrumValue[5], &spectrumValue[3], t_1, t_2, t_3, t_4); 
   }
   else if(choice==8)
   {
     color(&spectrumValue[2], &spectrumValue[1], &spectrumValue[0], t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8); 
      color(&spectrumValue[4], &spectrumValue[5], &spectrumValue[3], t_1, t_2, t_3, t_4, t_5, t_6, t_7, t_8); 
   }
   else
   {
     //                                                                    mf        hf       
     color(&spectrumValue[2], &spectrumValue[1], &spectrumValue[0], y_t, mag_t, lb_t, p_t, o_t, g_t, r_t, b_t); 
      color(&spectrumValue[4], &spectrumValue[5], &spectrumValue[3], y_t, mag_t, lb_t, p_t, o_t, g_t, r_t, b_t); 
   }
   for (int i = 0; i < 7; i++)
   {
    if (spectrumValue[i] < 0)
     {
        spectrumValue[i] = 0;
     } 
   }
   analogWrite(pin_R1, spectrumValue[1]); 
   analogWrite(pin_G1, spectrumValue[2]); 
   analogWrite(pin_B1, spectrumValue[0]);
  analogWrite(pin_R2, spectrumValue[4]); 
   analogWrite(pin_G2, spectrumValue[5]); 
   analogWrite(pin_B2, spectrumValue[3]); 
}
int range[2] = {110, 255};
int ext_range[2] = {40, 255};
int middle = (int) ((ext_range[0] + ext_range[1])/2);
void stretch(int* r, int* g, int* b)
{
	*r = (*r - range[0]) * ((ext_range[1]-ext_range[0])/(range[1]-range[0])) + ext_range[0];
        *g = (*g - range[0]) * ((ext_range[1]-ext_range[0])/(range[1]-range[0])) + ext_range[0];
	*b =(*b - range[0]) * ((ext_range[1]-ext_range[0])/(range[1]-range[0])) + ext_range[0];
}
void color(int* r, int* g, int* b, int t_1[3], int t_2[3], int t_3[3], int t_4[3], int t_5[3], int t_6[3],  int t_7[3], int t_8[3])
{
  if( (*r) > middle && *g < middle && *b < middle)
  {
    *r=(int)(t_1[0]-.3*(t_1[0]-*r));
    *g=(int)(t_1[1]-.3*(t_1[1]-*g));
    *b=(int)(t_1[2]-.3*(t_1[2]-*b));
    return;  

  }
  else if(*r < middle && *g>middle && *b< middle)
  {
    *r=(int)(t_2[0]-.3*(t_2[0]-*r));
    *g=(int)(t_2[1]-.3*(t_2[1]-*g));
    *b=(int)(t_2[2]-.3*(t_2[2]-*b));
    return;  
}
    else if(*r< middle  &&  *g<middle && *b>middle)
  {
    *r=(int)(t_3[0]-.3*(t_3[0]-*r));
    *g=(int)(t_3[1]-.3*(t_3[1]-*g));
    *b=(int)(t_3[2]-.3*(t_3[2]-*b));
    return;  

  }
    else if(*r < middle && *g<middle && *b<middle)
  {    
    *r=(int)(t_4[0]-.3*(t_4[0]-*r));
    *g=(int)(t_4[1]-.3*(t_4[1]-*g));
    *b=(int)(t_4[2]-.3*(t_4[2]-*b));
    return;  
  }
    else if(*r>middle && *g > middle  && *b < middle)
  {     
    *r=(int)(t_5[0]-.3*(t_5[0]-*r));
    *g=(int)(t_5[1]-.3*(t_5[1]-*g));
    *b=(int)(t_5[2]-.3*(t_5[2]-*b));
    return;  

  }
  else if(*r>middle && *g<middle && *b>middle )
  {     
    *r=(int)(t_6[0]-.3*(t_6[0]-*r));
    *g=(int)(t_6[1]-.3*(t_6[1]-*g));
    *b=(int)(t_6[2]-.3*(t_6[2]-*b));
    return;  

  }
   else if(*r>middle && *g>middle && *b>middle )
  {
    *r=(int)(t_7[0]-.3*(t_7[0]-*r));
    *g=(int)(t_7[1]-.3*(t_7[1]-*g));
    *b=(int)(t_7[2]-.3*(t_7[2]-*b));
    return;  
  }
  else if (*r<middle && *g>middle && *b>middle)
  {
    *r=(int)(t_8[0]-.3*(t_8[0]-*r));
    *g=(int)(t_8[1]-.3*(t_8[1]-*g));
    *b=(int)(t_8[2]-.3*(t_8[2]-*b));
    return;  

  }
}
void color(int* r, int* g, int* b, int t_1[3], int t_2[3], int t_3[3], int t_4[3])
{
  if( (*r) > middle && *b < middle)
  {
    *r=(int)(t_1[0]-.3*(t_1[0]-*r));
    *g=(int)(t_1[1]-.3*(t_1[1]-*g));
    *b=(int)(t_1[2]-.3*(t_1[2]-*b));
    return;  
  }
  else if(*r < middle && *b < middle)
  {     
    *r=(int)(t_2[0]-.3*(t_2[0]-*r));
    *g=(int)(t_2[1]-.3*(t_2[1]-*g));
    *b=(int)(t_2[2]-.3*(t_2[2]-*b));    
    return;
  }
    else if(*r< middle  && *b > middle)
  {
    *r=(int)(t_3[0]-.3*(t_3[0]-*r));
    *g=(int)(t_3[1]-.3*(t_3[1]-*g));
    *b=(int)(t_3[2]-.3*(t_3[2]-*b));    
    return;
  }
    else if(*r > middle && *b > middle)
  {    
    *r=(int)(t_4[0]-.3*(t_4[0]-*r));
    *g=(int)(t_4[1]-.3*(t_4[1]-*g));
    *b=(int)(t_4[2]-.3*(t_4[2]-*b));
    return;
  }
}
