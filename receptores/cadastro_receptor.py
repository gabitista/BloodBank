def cadastrar_receptor(nome, idade, tipo_sanguineo, cpf):
    receptor = {
        'nome': nome,
        'idade': idade,
        'tipo_sanguineo': tipo_sanguineo,
        'cpf': cpf
    }
    with open('receptores.txt', 'a') as file:
        file.write(f"{receptor}\n")
    return receptor
