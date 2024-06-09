def cadastro_doador():
  """
  Função para cadastrar doadores de sangue e verificar sua aptidão para doação.

  Retorno:
    Uma string informando se o doador está apto ou inapto para doar sangue, 
    junto com os motivos da inaptidão (se houver).
  """

  # Dicionário para armazenar as respostas do doador
  respostas = {}

  # Perguntas sobre o estado de saúde do doador
  respostas["resfriado"] = input("Você está com resfriado? (Sim/Não): ").lower()
  respostas["gravidez"] = input("Você está grávida? (Sim/Não): ").lower()
  respostas["amamentacao"] = input("Você está amamentando? (Sim/Não): ").lower()
  respostas["bebida_alcoolica"] = input("Você ingeriu bebida alcoólica nas últimas 12 horas? (Sim/Não): ").lower()

  # Perguntas sobre procedimentos estéticos
  respostas["tatuagem"] = input("Você fez tatuagem recentemente? (Sim/Não): ").lower()
  respostas["maquiagem_definitiva"] = input("Você fez maquiagem definitiva recentemente? (Sim/Não): ").lower()
  respostas["micropigmentacao"] = input("Você fez micropigmentação recentemente? (Sim/Não): ").lower()
  respostas["piercing"] = input("Você fez piercing recentemente? (Sim/Não): ").lower()
  respostas["brinco"] = input("Você colocou brinco recentemente? (Sim/Não): ").lower()

  # Análise das respostas para verificar a aptidão para doação
  apto_doar = True
  motivos_inaptidao = []

  # Resfriado
  if respostas["resfriado"] == "sim":
    apto_doar = False
    motivos_inaptidao.append("Resfriado (aguardar 7 dias após desaparecimento dos sintomas)")

  # Gravidez
  if respostas["gravidez"] == "sim":
    apto_doar = False
    motivos_inaptidao.append("Gravidez")

  # Amamentação
  if respostas["amamentacao"] == "sim":
    apto_doar = False
    motivos_inaptidao.append("Amamentação (aguardar 12 meses após o parto)")

  # Bebida alcoólica
  if respostas["bebida_alcoolica"] == "sim":
    apto_doar = False
    motivos_inaptidao.append("Ingestão de bebida alcoólica nas últimas 12 horas")

  # Procedimentos estéticos
  for procedimento in ["tatuagem", "maquiagem_definitiva", "micropigmentacao", "piercing", "brinco"]:
    if respostas[procedimento] == "sim":
      local_seguro = input(f"O {procedimento} foi feito em local seguro e com os cuidados necessários? (Sim/Não): ").lower()
      if local_seguro != "sim":
        apto_doar = False
        motivos_inaptidao.append(f"{procedimento} (aguardar 12 meses)")
      else:
        tempo_espera = input(f"Há quanto tempo o {procedimento} foi feito? (Em meses): ")
        try:
          tempo_espera = int(tempo_espera)
          if tempo_espera < 6:
            apto_doar = False
            motivos_inaptidao.append(f"{procedimento} (aguardar 6 meses)")
        except ValueError:
          print("Tempo de espera inválido. Por favor, digite um número inteiro.")

  # Mensagem final informando o resultado da avaliação
  if apto_doar:
    mensagem = "Parabéns! Você está apto para doar sangue."
  else:
    mensagem = f"Você está inapto para doar sangue neste momento pelos seguintes motivos: {', '.join(motivos_inaptidao)}."

  print(mensagem)

# Execução da função
cadastro_doador()
