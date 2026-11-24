# Simulator ESP32 (alternatif jika Python terpasang).
# Instal dulu: pip install paho-mqtt
import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime

BROKER = "localhost"
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"

def on_message(client, userdata, msg):
    print(f"<- Kontrol diterima: {msg.payload.decode()}")

# paho-mqtt versi 2.x
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="ESP32-Simulator")
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC_KONTROL)
client.loop_start()

print("ESP32 Simulator berjalan... Ctrl+C untuk stop")
try:
    while True:
        data = {
            "suhu": round(random.uniform(25, 32), 1),
            "kelembaban": round(random.uniform(55, 80), 1),
            "timestamp": datetime.now().isoformat()
        }
        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"-> Publish: {data}")
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
