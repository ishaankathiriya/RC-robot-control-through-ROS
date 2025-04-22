#include <WiFi.h>



#define ENA 14
#define IN1 27
#define IN2 26
#define ENB 13
#define IN3 12
#define IN4 33

int speed = 200; // pwm range: 0-255

// Access Point credentials
const char* ssid = "EEEEEEEEE";  // Name of the WiFi network the ESP32 will create
const char* password = "12345678";  // Password for the network (min 8 chars)

// Server on port 80
WiFiServer server(81);
WiFiClient client;

void setup() {
  Serial.begin(115200);
  
  // Configure ESP32 as Access Point
  WiFi.softAP(ssid, password);
  
  // Print the IP address (should be 192.168.4.1)
  Serial.print("Access Point IP address: ");
  Serial.println(WiFi.softAPIP());
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  pinMode(ENA,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(ENB,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);


  
}

void loop() {
  // Listen for clients
  if (!client || !client.connected()) {
    client = server.available();
    //Serial.println("Server available");
    if (client) {
      Serial.println("New client connected");
    }
  }
  
  // Process incoming messages
  if (client && client.connected()) {
    if (client.available()) {
      String command = client.readStringUntil('\n');
      Serial.print("Received data: ");
      Serial.println(command);
      
      // Process the command here
      // For example: if (data == "LED_ON") digitalWrite(LED_PIN, HIGH);

        if (command == "w"){
          forward();
        }
    
        else if (command == "s"){
          reverse();
        }

        else if (command == "d"){
          right();
        }

         else if (command == "a"){
          left();
        }

         else if (command == "e"){
          stopmotors();
        }
        
      }
    }

    //client.stop();
    //Serial.println("Client disconnected");
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
      
