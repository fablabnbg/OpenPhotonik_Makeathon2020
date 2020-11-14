#include <RH_RF95.h>
#include <RHSoftwareSPI.h>
//#include <LoRaNow.h>

#include <WiFi.h>
#include "time.h"
 
#define LORA_SCK    5
#define LORA_MISO   19
#define LORA_MOSI   27
#define LORA_CS     18
#define LORA_INT    26
#define LORA_RST    14

//#define LED_PIN     0

#define RF95_FREQ 868.0

const char* ssid       = "FBTest";
const char* password   = "Dasist1Test!";

RHSoftwareSPI spi;
RH_RF95 rf95(LORA_CS, LORA_INT, spi);

void setup()
{
  pinMode(LORA_RST, OUTPUT);
  spi.setPins(LORA_MISO, LORA_MOSI, LORA_SCK);
  spi.begin();
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
  LoRaNow.onSleep(onSleep);
  LoRaNow.showStatus(Serial);

  //digitalWrite(LED_PIN, HIGH);
 
  //disconnect WiFi as it's no longer needed
  //WiFi.disconnect(true);
  //WiFi.mode(WIFI_OFF);*/
}

void loop()
{
  Serial.println("Sending to rf95_server");
  // Send a message to rf95_server
  uint8_t data[] = "Hello World!";
  rf95.send(data, sizeof(data));
  
  rf95.waitPacketSent();
  // Now wait for a reply
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);
 
  if (rf95.waitAvailableTimeout(3000))
  { 
    // Should be a reply message for us now   
    if (rf95.recv(buf, &len))
   {
      Serial.print("got reply: ");
      Serial.println((char*)buf);
//      Serial.print("RSSI: ");
//      Serial.println(rf95.lastRssi(), DEC);    
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  else
  {
    Serial.println("No reply, is rf95_server running?");
  }
  delay(400);
}
