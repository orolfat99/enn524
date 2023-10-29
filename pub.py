import paho.mqtt.publish as publish
publish.single("enn524", "hello world", hostname="3.27.235.75")
print("Done")
