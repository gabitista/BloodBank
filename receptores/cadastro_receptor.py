import json

def cadastrar_receptor(nome,cpf, idade, tipo_sanguineo):
    receptor = {
        'nome': nome,
        'CPF': cpf,
        'idade': idade,
        'tipo_sanguineo': tipo_sanguineo
        
    }
    with open('receptores.json', 'a') as file:
        json.dump(receptor, file)
        file.write('\n')
    return receptor

def main():
    print("Cadastro de Receptores de Bolsa de Sangue")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    tipo_sanguineo = input("Tipo Sanguíneo: ")
    
    
    receptor_cadastrado = cadastrar_receptor(nome,cpf, idade, tipo_sanguineo)
    print("Receptor cadastrado com sucesso:")
    print(receptor_cadastrado)

if __name__ == "__main__":
    main()
