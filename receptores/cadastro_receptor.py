import json

def cadastrar_receptor(nome, idade, tipo_sanguineo, cpf):
    receptor = {
        'nome': nome,
        'idade': idade,
        'tipo_sanguineo': tipo_sanguineo,
        'cpf': cpf
    }
    with open('receptores.json', 'a') as file:
        json.dump(receptor, file)
        file.write('\n')
    return receptor

def main():
    print("Cadastro de Receptores de Bolsa de Sangue")
    nome = input("Nome: ")
    idade = input("Idade: ")
    tipo_sanguineo = input("Tipo Sanguíneo: ")
    cpf = input("CPF: ")
    
    receptor_cadastrado = cadastrar_receptor(nome, idade, tipo_sanguineo, cpf)
    print("Receptor cadastrado com sucesso:")
    print(receptor_cadastrado)

if __name__ == "__main__":
    main()
