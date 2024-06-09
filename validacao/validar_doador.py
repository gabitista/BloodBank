def validar_doador(doador):
    # Validação dos requisitos, conforme o cadastro

    if not (18 <= doador['idade'] <= 60):
        return False, "Idade fora do limite permitido (18-60 anos)."
    
    if doador['peso'] < 50:
        return False, "O peso mínimo é de 50 kg. Paciente abaixo do limite"
    
    if doador['hemoglobina'] < 12.5:
        return False, "Nível de hemoglobina abaixo do mínimo exigido (12.5 g/dL)."
    
    if doador['pressao_sistolica'] < 90 or doador['pressao_sistolica'] > 160 or doador['pressao_diastolica'] < 60 or doador['pressao_diastolica'] > 100:
        return False, "Pressão arterial fora dos limites permitidos."

    if doador['gravidez']:
        return False, "Não pode doar durante a gravidez."
    
    if doador['amamentacao']:
        return False, "Não pode doar durante a amamentação."

    if doador['resfriado']:
        return False, "Não pode doar com resfriado."

    if doador['bebida_alcoolica']:
        return False, "Não pode doar após ingestão de bebida alcoólica."

    if any(doador[proc] for proc in ["tatuagem", "maquiagem_definitiva", "micropigmentacao", "piercing", "brinco"]):
        return False, "Período de espera após tatuagem, maquiagem definitiva, micropigmentação, piercing ou brinco ainda não completado."

    return True, "Você está apto a doar sangue!"
