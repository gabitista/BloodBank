def gerar_relatorio():
    relatorio = "Relatório de Doadores e Estoque de Sangue\n"
    relatorio += "=======================================\n"
    
    with open('doadores.txt', 'r') as file:
        doadores = file.readlines()
        relatorio += f"Total de Doadores: {len(doadores)}\n"
        
    tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    for tipo in tipos_sanguineos:
        estoque = verificar_estoque(tipo)
        relatorio += f"Estoque de Sangue {tipo}: {estoque} bolsas\n"
    
    with open('relatorio.txt', 'w') as file:
        file.write(relatorio)
        
    return relatorio
