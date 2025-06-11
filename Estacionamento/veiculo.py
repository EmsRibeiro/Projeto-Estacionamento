import re

class Veiculo:
    def __init__(self, placa, hora_entrada=None, hora_saida=None):
        self.placa = placa
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida

    def set_hora_entrada(self, hora_entrada):
        self.hora_entrada = hora_entrada

    def set_hora_saida(self, hora_saida):
        self.hora_saida = hora_saida

    def validar_placa(self):
        padrao_placa = r'^[A-Z]{3}\d[A-Z]\d{2}$'
        return re.match(padrao_placa, self.placa) is not None

    def identificar_estado(self, estados):
        if not self.validar_placa():
            return "Placa inválida! A placa não está no formato Mercosul correto."

        letras = self.placa[:3]  
        for regiao, ranges in estados.items():
            for (inicio, fim) in ranges:  
                if inicio <= letras <= fim:
                    return f"{regiao}"  
        return "A placa não pertence a nenhum dos estados especificados."