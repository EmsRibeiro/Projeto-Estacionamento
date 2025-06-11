from veiculo import Veiculo
from estacionamento import Estacionamento


def testar_input(prompt, validacao, tentativas=3):
    for i in range(tentativas):
        dado = input(prompt).strip()
        if validacao(dado):
            return dado
        else:
            print(f"Entrada inválida. Você ainda tem {tentativas - i - 1} tentativa(s).")
    print("Número máximo de tentativas atingido. Fechando o programa.")
    exit()


def validar_placa(placa):
    return len(placa) == 7 and \
           placa[:3].isalpha() and \
           placa[3].isdigit() and \
           placa[4].isalpha() and \
           placa[5:].isdigit()


def validar_hora(hora):
    if len(hora) == 5 and hora[2] == ':' and hora[:2].isdigit() and hora[3:].isdigit():
        horas = int(hora[:2])
        minutos = int(hora[3:])
        return 0 <= horas <= 23 and 0 <= minutos <= 59
    return False

if __name__ == "__main__":
    estacionamento = Estacionamento(2)

    while True:
        print("\nMENU:")
        print("1 - Entrar com o veículo")
        print("2 - Sair com o veículo")
        print("3 - Ver vagas ocupadas")
        print("4 - Limpar estacionamento")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo do sistema.")
            break

        elif opcao == "1":
            placa_entrada = testar_input("\nDigite a placa do veículo (formato Mercosul, ex: 'OXH5L56'): ",validar_placa).strip().upper() 

            veiculo = Veiculo(placa_entrada)

            hora_entrada = testar_input(
                "Digite a hora de entrada do veículo (formato HH:MM, ex: '10:00'): ",
                validar_hora
            )

            
            veiculo.set_hora_entrada(hora_entrada)

            
            print(estacionamento.entrar(veiculo))
        elif opcao == "2":
            placa_saida = input("\nDigite a placa do veículo que está saindo: ").strip().upper()

            if placa_saida in estacionamento.veiculos:
                veiculo = estacionamento.veiculos[placa_saida][0]

                hora_saida = testar_input(
                    "Digite a hora de saída do veículo (formato HH:MM, ex: '13:30'): ",
                    validar_hora
                )

                print(estacionamento.sair(veiculo, hora_saida))
            else:
                print("Veículo não encontrado no estacionamento.")

        elif opcao == "3":
            print(f"\nVagas ocupadas: {estacionamento.vagas_ocupadas()}")

        elif opcao == "4":
            estacionamento.limpar_matriz()

        else:
            print("Opção inválida. Tente novamente.")
