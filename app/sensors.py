import random
import json
from typing import List
from datetime import datetime

class Sensor:
    def __init__(self, num):
        self.id = num

    def coletar(self):
        return random.randint(20, 40)

class Atuador:
    ativo = False

    def __init__(self, num):
        self.id = num

    def ativar(self):
        if self.ativo:
            print("Processo desativado.")
            self.ativo = False
        else:
            print("Processo ativado.")
            self.ativo = True

class Coletor:
    id_coletor: int
    sensores: List[Sensor] = list()

    def __init__(self, id, num_s):
        self.id_coletor = id
        self.num_sensores = num_s
        self.sensores = [Sensor(i) for i in range(1, self.num_sensores + 1)]

    def coletar_dados(self):
        coletor_data = []
        for sensor in self.sensores:
            sensor_data = {
                "id_coletor": self.id_coletor,
                "id": sensor.id,
                "value": sensor.coletar(),
                "type": "temperatura", 
                "date": datetime.now().isoformat(),
                "unitMeasurement": "C",  
            }
            coletor_data.append(sensor_data)

        object_json = json.dumps(coletor_data, indent=4)
        return object_json
