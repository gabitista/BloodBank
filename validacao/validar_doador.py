def validar_doador(doador):
    if doador['idade'] >= 18 and doador['idade'] <= 60:
        return True
      
    if peso < 50:
        return False, "Peso abaixo do mínimo exigido (50 kg)."
    
    if hemoglobina < 12.5:
        return False, "Nível de hemoglobina abaixo do mínimo exigido (12.5 g/dL)."
    
    if pressao_sistolica < 90 or pressao_sistolica > 160 or pressao_diastolica < 60 or pressao_diastolica > 100:
        return False, "Pressão arterial fora dos limites permitidos."
    
    if gravidez:
        return False, "Não pode doar durante a gravidez."
    
    if amamentacao:
        return False, "Não pode doar durante a amamentação."

    if cirurgia_recente:
        return False, "Período de espera após cirurgia ainda não completado."
  
    if vacina_recente:
        return False, "Período de espera após vacinação ainda não completado."
    
    if viagem_recente:
        return False, "Período de espera após viagem para área endêmica ainda não completado."

    if tatuagem_piercing_recente:
        return False, "Período de espera após tatuagem ou piercing ainda não completado."
    
return True, "Você está apto a doar sangue!"

aptidao, mensagem = pode_doar_sangue(idade, peso, hemoglobina, pressao_sistolica, pressao_diastolica, gravidez, amamentacao, cirurgia_recente, vacina_recente, viagem_recente, tatuagem_piercing_recente)
print(mensagem)
