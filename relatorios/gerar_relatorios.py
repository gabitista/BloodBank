from armazenamento.verificar_armazenamento import verificar_armazenamento

def gerar_relatorio():
    # Simples relatório de exemplo
    relatorio = "Relatório de Doadores e Armazenamento de Sangue\n"
    relatorio += "=======================================\n"
    
    with open('doadores.txt', 'r') as file:
        doadores = file.readlines()
        relatorio += f"Total de Doadores: {len(doadores)}\n"
    
    tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    for tipo in tipos_sanguineos:
        armazenamento = verificar_armazenamento(tipo)
        relatorio += f"Armazenamento de Sangue {tipo}: {armazenamento} mL\n"
    
    with open('relatorio.txt', 'w') as file:
        file.write(relatorio)
    
    return relatorio
