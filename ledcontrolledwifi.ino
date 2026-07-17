#include <ESP8266WiFi.h>

const char* ssid     = "SPS@FF1";
const char* password = "sps@hotspot";

WiFiServer server(80);
const int ledPin = D5; // D5 pin                              
void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // LED starts OFF

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (!client) return; // Wait for a browser to connect

  String request = client.readStringUntil('\r'); // Read the browser request
  client.flush();

  // Check what URL path the browser asked for
  if (request.indexOf("/on") != -1) {
    digitalWrite(ledPin, HIGH);
  } 
  else if (request.indexOf("/off") != -1) {
    digitalWrite(ledPin, LOW);
  }

  // Send a simple response back to the browser screen
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/plain");
  client.println();
  
  // FIXED LINE: Changed digitalWrite to digitalRead
  if (digitalRead(ledPin) == HIGH) {
    client.print("LED is now ON");
  } else {
    client.print("LED is now OFF");
  }
}
