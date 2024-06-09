def cadastrar_bolsa(tipo_sanguineo, quantidade, data_doacao):
    bolsa = {
        'tipo_sanguineo': tipo_sanguineo,
        'quantidade': quantidade,
        'data_doacao': data_doacao
    }
   
    with open('bolsas.txt', 'a') as file:
        file.write(f"{bolsa}\n")
    return bolsa