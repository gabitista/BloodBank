def verificar_armazenamento(tipo_sanguineo):
    armazenamento = 0
    with open('bolsas.txt', 'r') as file:
        for linha in file:
            bolsa = eval(linha.strip())
            if bolsa['tipo_sanguineo'] == tipo_sanguineo:
                armazenamento += bolsa['quantidade']
    return armazenamento
