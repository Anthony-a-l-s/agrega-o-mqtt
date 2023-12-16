import sys
import  paho.mqtt.client as paho
from sensors import Coletor
import time
import statistics as st
from typing import List
import json

coletores = []
for i in range(4):
    coletores.append(Coletor(i, 5, 1))

client = paho.Client()

if client.connect("192.168.100.14", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

ticks = 0
# dados = []
while (True):
    if ticks == 30:
        break
    else:
        ticks = ticks + 1
        time.sleep(2)
        for coletor in coletores:
            msg = json.loads(coletor.coletar_dados())
            # dados.append(st.mean(coletor.coletar_dados()))
            # m_temp = str(st.mean(dados))
            client.publish("temperature_topic", str(msg), 0)

client.disconnect()