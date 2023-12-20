import sys
import  paho.mqtt.client as paho
from sensors import Coletor
import time
import statistics as st
from typing import List
import json

coletores = []
for i in range(4):
    coletores.append(Coletor(i, 5))

client = paho.Client()

if client.connect("10.5.16.131", 1890, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)


# dados = []
while (True):

    time.sleep(2)
    for coletor in coletores:
        msg = json.loads(coletor.coletar_dados())
        # dados.append(st.mean(coletor.coletar_dados()))
        # m_temp = str(st.mean(dados))
        client.publish("temperature_topic", str(msg), 0)

client.disconnect()