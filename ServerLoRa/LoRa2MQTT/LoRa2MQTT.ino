#include <RH_RF95.h>

//#include <LoRaNow.h>

#include <WiFi.h>
#include "time.h"
 
#define LORA_SCK    18
#define LORA_MISO   19
#define LORA_MOSI   23
#define LORA_CS     5
#define LORA_INT    17
#define LORA_RST    21

//#define LED_PIN     0

#define RF95_FREQ 868.0

const char* ssid       = "FBTest";
const char* password   = "Dasist1Test!";

RH_RF95 rf95(LORA_CS, LORA_INT);


void setup()
{
  pinMode(LORA_RST, OUTPUT);
  //pinMode(LED_PIN, OUTPUT);

 /* pinMode(LORA_SCK, OUTPUT);
  pinMode(LORA_MISO, OUTPUT);
  pinMode(LORA_MOSI, OUTPUT);
  pinMode(LORA_CS, OUTPUT);
  pinMode(LORA_INT, OUTPUT);*/
  
  Serial.begin(115200);

  digitalWrite(LORA_RST, LOW);
  delay(10);
  digitalWrite(LORA_RST, HIGH);
  delay(10);
  //digitalWrite(LED_PIN, LOW);
  //connect to WiFi
  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }
  Serial.println(" CONNECTED");

  if(!rf95.init())
  {
    Serial.println("LoRa init failed. Check your connections.");
    while (true);
  }
  rf95.setModemConfig(RH_RF95::Bw500Cr45Sf128);
  rf95.setFrequency(868E6);
  

  //LoRaNow.setFrequencyEU(); // Select the frequency 868.3 MHz - Used in Europe

  //LoRaNow.setPinsSPI(LORA_SCK, LORA_MISO, LORA_MOSI, LORA_CS, LORA_INT); // Only works with ESP32
  //LoRaNow.setSpreadingFactor(8);
  //LoRaNow.setSignalBandwidth(125E3);
  //LoRaNow.setCodingRate4(5);
  //LoRaNow.setSyncWord(0x12);
  //LoRaNow.disableInvertIQ();
  /*if (!LoRaNow.begin())
  {
    Serial.println("LoRa init failed. Check your connections.");
    while (true)
      ;
  }

  LoRaNow.onMessage(onMessage);
  LoRaNow.gateway();
  LoRaNow.showStatus(Serial);*/

  //digitalWrite(LED_PIN, HIGH);
 
  //disconnect WiFi as it's no longer needed
  //WiFi.disconnect(true);
  //WiFi.mode(WIFI_OFF);
}

void loop()
{ 
  if (rf95.available())
  {
    // Should be a message for us now   
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (rf95.recv(buf, &len))
    {
      //digitalWrite(led, HIGH);
//      RH_RF95::printBuffer("request: ", buf, len);
      Serial.print("got request: ");
      Serial.println((char*)buf);
//      Serial.print("RSSI: ");
//      Serial.println(rf95.lastRssi(), DEC);
      
      // Send a reply
      uint8_t data[] = "And hello back to you";
      rf95.send(data, sizeof(data));
      rf95.waitPacketSent();
      Serial.println("Sent a reply");
      //digitalWrite(led, LOW);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  //LoRaNow.loop();
  /*int pins[] = {LORA_RST, LORA_SCK, LORA_MISO, LORA_MOSI, LORA_CS, LORA_INT};
  for(int i = 0; i < 6; i++){
    digitalWrite(pins[i], LOW);
    delay(10);
    digitalWrite(pins[i], HIGH);
  }*/
}
/*void onMessage(uint8_t *buffer, size_t size)
{
  unsigned long id = LoRaNow.id();
  byte count = LoRaNow.count();

  Serial.print("Node Id: ");
  Serial.println(id, HEX);
  Serial.print("Count: ");
  Serial.println(count);
  Serial.print("Message: ");
  Serial.write(buffer, size);
  Serial.println();
  Serial.println();

  // Send data to the node
  LoRaNow.clear();
  LoRaNow.print("LoRaNow Gateway Message ");
  LoRaNow.print(millis());
  LoRaNow.send();
}*/
