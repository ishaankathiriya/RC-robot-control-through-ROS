// communication via serial


#define ENA 14
#define IN1 27
#define IN2 26
#define ENB 13
#define IN3 12
#define IN4 33


int speed = 200; // pwm range: 0-255



void setup() {
  Serial.begin(115200);
  
  pinMode(ENA,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(ENB,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  
}

void loop() {
  if (Serial.available()) {
    
    char command = Serial.read();

    if (command == 'w'){
      forward();
    }
    
    else if (command == 's'){
      reverse();
    }

    else if (command =='d'){
      right();
    }

    else if (command =='a'){
      left();
    }

    else if (command =='e'){
      stopmotors();
    }
  }

}

void forward(){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,speed);

  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,speed);
}

void reverse(){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  analogWrite(ENA,speed);

  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  analogWrite(ENB,speed); 
}


void left(){
  int leftspeed = 100;
  int rightspeed = 200;
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,leftspeed);

  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,rightspeed);
}

void right(){
  int leftspeed = 200;
  int rightspeed = 100;
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,leftspeed);

  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,rightspeed);
}

void stopmotors(){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  analogWrite(ENA,0);

  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
  analogWrite(ENB,0);
}
