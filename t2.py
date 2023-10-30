import paho.mqtt.publish as publish


m1 = "A"*1024
m2 = "B"*102400

publish.single("enn524", m1, hostname = "3.27.235.75")
publish.single("enn524", m2, hostname="3.27.235.75")
print("Done")
