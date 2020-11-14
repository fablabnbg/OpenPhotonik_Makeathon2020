from ssd1306_i2c import Display

class LoRaReceiver:
    def receive(self, lora):
        print("LoRa Receiver")
        display = Display()

        while True:
            if lora.received_packet():
                lora.blink_led()
                print('something here')
                payload = lora.read_payload()
                print(payload)
