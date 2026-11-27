void setup(){
Serial.begin(9600);
pinMode(6,OUTPUT); // trigg 
pinMode(7,INPUT);  // echo
pinMode(13,OUTPUT);
}

void loop(){
int time,distance ;
digitalWrite(6,LOW); //trigg 
delay(500);
digitalWrite(6,HIGH);
delay(250);
digitalWrite(6,LOW);
time = pulseIn(7, HIGH);
distance = time*0.034/2;
Serial.print(distance);
Serial.println("cm");
  
if (distance<=35)
{
  digitalWrite(13,HIGH);
}
  else{
  digitalWrite(13,LOW);
  }
}
