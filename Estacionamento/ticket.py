from datetime import datetime

class Ticket:
    def __init__(self, placa, hora_entrada, hora_saida, valor, estado, posicao):
        self.placa = placa
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.valor = valor
        self.estado = estado
        self.posicao = posicao  

    def imprimir(self):
        tempo_permanencia = (datetime.strptime(self.hora_saida, '%H:%M') - datetime.strptime(self.hora_entrada, '%H:%M')).seconds // 60
        ticket = f"""
        TICKET DE ESTACIONAMENTO
        -------------------------
        Local de estacionamento: Posição {self.posicao}
        Placa do veículo: {self.placa}
        Hora de entrada: {self.hora_entrada}
        Hora de saída: {self.hora_saida}
        Tempo de permanência: {tempo_permanencia} minutos
        Valor cobrado: R$ {self.valor:.2f}
        Estado de origem: {self.estado}
        """
        return ticket