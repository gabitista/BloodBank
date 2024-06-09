# Cadastro do doador 
def cadastrar_doador(nome, idade, tipo_sanguineo, cpf):
    doador = {
        "nome": nome,
        "idade": idade,
        "tipo_sanguineo": tipo_sanguineo,
        "cpf": cpf,
        # Perguntas para validar os requisitos
        "resfriado": input("Você está com resfriado? (Sim/Não): ").lower() == "sim",
        "gravidez": input("Você está grávida? (Sim/Não): ").lower() == "sim",
        "amamentacao": input("Você está amamentando? (Sim/Não): ").lower() == "sim",
        "bebida_alcoolica": input("Você ingeriu bebida alcoólica nas últimas 12 horas? (Sim/Não): ").lower() == "sim",
        "tatuagem": input("Você fez tatuagem recentemente? (Sim/Não): ").lower() == "sim",
        "maquiagem_definitiva": input("Você fez maquiagem definitiva recentemente? (Sim/Não): ").lower() == "sim",
        "micropigmentacao": input("Você fez micropigmentação recentemente? (Sim/Não): ").lower() == "sim",
        "piercing": input("Você fez piercing recentemente? (Sim/Não): ").lower() == "sim",
        "brinco": input("Você colocou brinco recentemente? (Sim/Não): ").lower() == "sim",
        "peso": float(input("Qual o seu peso? (kg): ")),
        "hemoglobina": float(input("Qual o seu nível de hemoglobina? (g/dL): ")),
        "pressao_sistolica": int(input("Qual a sua pressão sistólica? ")),
        "pressao_diastolica": int(input("Qual a sua pressão diastólica? "))
    }

    with open('doadores.txt', 'a') as file:
        file.write(str(doador) + '\n')

    return doador
