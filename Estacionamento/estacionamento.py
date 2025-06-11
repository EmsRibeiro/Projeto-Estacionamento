import math
from datetime import datetime
from ticket import Ticket

class Estacionamento:
    def __init__(self, capacidade):
        self.matriz = [[None for _ in range(capacidade)] for _ in range(capacidade)]  
        self.veiculos = {}  
        self.estados = {
            'Paraná': [('AAA', 'BEZ'), ('NSE', 'NTC'), ('RHA', 'RHZ')],
            'São Paulo': [('BFA', 'GKI'), ('QTA', 'QTJ')],
            'Minas Gerais': [('GKJ', 'HOK'), ('NYH', 'NZZ'), ('OMI', 'OOF'), ('QAA', 'QAZ'), ('RFA', 'RGD')],
            'Maranhão': [('HOL', 'HQE'), ('NHA', 'NHT'), ('NMP', 'NNI'), ('OJR', 'OKC'), ('ROA', 'ROZ')],
            'Mato Grosso do Sul': [('HQF', 'HTW'), ('NRF', 'NSD'), ('QBA', 'QCZ')],
            'Ceará': [('HTX', 'HZA'), ('NQL', 'NRE'), ('OSW', 'OTZ'), ('RIA', 'RIN')],
            'Sergipe': [('HZB', 'IAP'), ('NVO', 'NWR'), ('RQW', 'RRH')],
            'Rio Grande do Sul': [('IAQ', 'JDO')],
            'Distrito Federal': [('JDP', 'JKR'), ('OVW', 'OVY'), ('PCA', 'PED')],
            'Bahia': [('JKS', 'JSZ'), ('NTD', 'NTW'), ('OAA', 'OAO'), ('PMA', 'POZ')],
            'Pará': [('JTA', 'JWE'), ('NSE', 'NTC'), ('OCB', 'OCU'), ('QFA', 'QFZ')],
            'Amazonas ': [('JWF', 'JXY'), ('NOI', 'NPB'), ('OXN ', 'OXN')],
            'Mato Grosso': [('JXZ', 'KAU'), ('NIY', 'NJW'), ('OBT', 'OCA'), ('QDA', 'QEZ')],
            'Goiás': [('KAV', 'KFC'), ('NFC', 'NGZ'), ('OHB', 'OHK'), ('QTT', 'QTT')],
            'Pernambuco': [('KFD', 'KME'), ('NXX', 'NYG'), ('PEE', 'PFQ'), ('PHA', 'PHZ')],
            'Rio de Janeiro': [('KMF', 'LVE'), ('RIO', 'RIO')],
            'Piauí': [('LVF', 'LWQ'), ('NHU', 'NIX'), ('OEJ', 'OES'), ('PJA', 'PLZ')],
            'Santa Catarina': [('LWR', 'MMM'), ('OKI', 'OLG'), ('RXK', 'RYI')],
            'Paraíba': [('MMN', 'MOW'), ('NPR', 'NQK'), ('QGA', 'QGZ'), ('RLQ', 'RMC')],
            'Espírito Santo': [('MOX', 'MTZ'), ('ODU', 'OEI'), ('OVG', 'OVG'), ('QRN', 'QRZ')],
            'Alagoas': [('MUA', 'MVK'), ('NLV', 'NMO'), ('ORN', 'OSV'), ('QWM', 'QWQ')],
            'Tocantins': [('MVL', 'MXG'), ('QWG', 'QWL')],
            'Rio Grande do Norte': [('MXH', 'MZM'), ('NNJ', 'NOH'), ('OKD', 'OKH'), ('QHA', 'QJZ')],
            'Acre': [('MZN', 'NAG'), ('NXU', 'NXW'), ('OXQ', 'OXZ')],
            'Roraima': [('NAH', 'NBA'), ('NUM', 'NVF'), ('RZA', 'RZD')],
            'Rondônia': [('NBB', 'NEH'), ('QTK', 'QTM')],
            'Amapá': [('NEI', 'NFB'), ('QLU', 'QLZ')],
        }

    def entrar(self, veiculo):
        posicao = self.encontrar_posicao_livre()
        if posicao:
            if veiculo.placa not in self.veiculos:
                self.veiculos[veiculo.placa] = (veiculo, posicao)
                self.matriz[posicao[0]][posicao[1]] = veiculo
                return f"\nVeículo com placa {veiculo.placa} estacionado na posição {posicao}."
            return f"\nVeículo com placa {veiculo.placa} já está no estacionamento."
        else:
            return "\nEstacionamento cheio! Não é possível adicionar o veículo."

    def sair(self, veiculo, hora_saida):
        if veiculo.placa in self.veiculos:
            veiculo_obj, posicao = self.veiculos[veiculo.placa]
            self.matriz[posicao[0]][posicao[1]] = None
            del self.veiculos[veiculo.placa]

            if veiculo_obj.hora_entrada is None:
                return f"Erro: A hora de entrada do veículo {veiculo.placa} não foi registrada corretamente."

            veiculo_obj.set_hora_saida(hora_saida)
            valor = self.calcular_valor(veiculo_obj.hora_entrada, veiculo_obj.hora_saida)
            ticket = Ticket(veiculo_obj.placa, veiculo_obj.hora_entrada, veiculo_obj.hora_saida, valor, veiculo_obj.identificar_estado(self.estados), posicao)
            return ticket.imprimir()

        return "\nVeículo não encontrado no estacionamento."

    @staticmethod
    def calcular_valor(hora_entrada, hora_saida, valor_ate_3h=5.00, valor_adicional=2.00):
        tempo_entrada = datetime.strptime(hora_entrada, "%H:%M")
        tempo_saida = datetime.strptime(hora_saida, "%H:%M")

        duracao = (tempo_saida - tempo_entrada).seconds / 60  

        if duracao <= 0:
            return 0.00

        if duracao <= 180:
            return valor_ate_3h  
        else:
           
            horas_extras = math.ceil((duracao - 180) / 60)  
            return valor_ate_3h + (horas_extras * valor_adicional)
        
    def encontrar_posicao_livre(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] is None:  
                    return (i, j)  
        return None  

    def limpar_matriz(self):
        self.matriz = [[None for _ in range(len(self.matriz))] for _ in range(len(self.matriz))]
        self.veiculos.clear()
        print("\nTodas as posições da matriz do estacionamento foram limpas.")
    
    def vagas_ocupadas(self):
        return sum(1 for linha in self.matriz for vaga in linha if vaga is not None)
