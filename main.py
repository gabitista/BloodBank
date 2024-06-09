from doadores.cadastro_doador import cadastrar_doador
from validacao.validar_doador import validar_doador
from receptores.cadastro_receptor import cadastrar_receptor
from bolsas.cadastro_bolsa import cadastrar_bolsa
from armazenamento.verificar_armazenamento import verificar_armazenamento
from relatorios.gerar_relatorios import gerar_relatorio

def main():
    while True:
        print("\n1. Cadastrar Doador")
        print("2. Validar Doador")
        print("3. Cadastrar Receptor")
        print("4. Cadastrar Bolsa de Sangue")
        print("5. Verificar Armazenamento de Sangue")
        print("6. Gerar Relatório")
        print("7. Sair")
            
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            cpf = input("CPF: ")
            doador = cadastrar_doador(nome, idade, tipo_sanguineo, cpf)

            print("Doador cadastrado com sucesso.")
        
        elif escolha == '2':
            cpf = input("CPF do Doador: ")
            with open('doadores.txt', 'r') as file:
                doadores = file.readlines()
                for linha in doadores:
                    doador = eval(linha.strip())
                    if doador['cpf'] == cpf:
                        apto, mensagem = validar_doador(doador)
                        print(mensagem)
                        break
                else:
                    print("Doador não encontrado.")
        
        elif escolha == '3':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            cpf = input("CPF: ")
            receptor = cadastrar_receptor(nome, idade, tipo_sanguineo, cpf)
            print("Receptor cadastrado com sucesso.")
        
        elif escolha == '4':
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            quantidade = int(input("Quantidade (em ml): "))
            data_doacao = input("Data da Doação: ")
            bolsa = cadastrar_bolsa(tipo_sanguineo, quantidade, data_doacao)
            print("Bolsa de sangue cadastrada com sucesso.")
        
        elif escolha == '5':
            tipo_sanguineo = input("Tipo Sanguíneo: ")
            armazenamento = verificar_armazenamento(tipo_sanguineo)
            print(f"Armazenamento de sangue {tipo_sanguineo}: {armazenamento} ml.")
        
        elif escolha == '6':
            relatorio = gerar_relatorio()
            print(relatorio)
        
        elif escolha == '7':
            break

if __name__ == "__main__":
    main()
