import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("connected with result code " + str(rc))
	client.subscribe("ESD/project")
	
def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))
	
	## To check if the connection to HiveMQ is made
	if msg.payload == "Hello":
		print("Recieved Hello")
	if msg.payload == "Hi":
		print("Recieved Hi")
		
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqttdashboard.com", 1883, 60)

client.loop_forever()


	
