estoque_sangue = []

def cadastrar_bolsa(doador):
    bolsa = {
        "doador": doador,
        "tipo_sanguineo": doador["tipo_sanguineo"]
    }
    
    estoque_sangue.append(bolsa)    
    return bolsa
