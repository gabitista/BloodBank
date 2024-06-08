def verificar_estoque(tipo_sanguineo):
    estoque = 0
    # Ler o arquivo de bolsas de sangue
    with open('bolsas.txt', 'r') as file:
        for linha in file:
            bolsa = eval(linha.strip())
            if bolsa['tipo_sanguineo'] == tipo_sanguineo:
                estoque += bolsa['quantidade']
    return estoque
