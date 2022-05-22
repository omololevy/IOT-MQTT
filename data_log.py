from http import server
import paho.mqtt. client as mqtt

for received data from server
def on_connect(data_iot, user,events):
    print("connected with code " + str(events))

data = mqtt.Client()
Data.on_connect = on_connect
Data.on_message =on_message
data.loop_forever()