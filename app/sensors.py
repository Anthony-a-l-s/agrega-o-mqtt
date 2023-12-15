import random
import json
from typing import List

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
    sensores: List[Sensor]  = list()
    atuadores: List[Atuador] = list()
    def __init__(self, id, num_s, num_a):
        self.id_coletor = id
        self.num_sensores  = num_s
        self.num_atuadores = num_a

        self.sensores  = []
        self.atuadores = []

        for i in range(self.num_sensores):
            self.sensores.append(Sensor(i))
        for i in range(self.num_atuadores):
            self.atuadores.append(Atuador(i))
    
    def coletar_dados(self):
        coletor_dic = {"id": self.id_coletor}
        for i, sensor in enumerate(self.sensores):
            coletor_dic["sensor {}".format(i)] = sensor.coletar()
        object_json = json.dumps(coletor_dic, indent=4)
        return object_json