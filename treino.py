def calcular_calorias_gastas(tempo_minutos, intensidade):
    # Fator base de queima calórica por minuto
    fator = {"baixa": 5, "media": 8, "alta": 12}
    return tempo_minutos * fator.get(intensidade, 5)

if __name__ == "__main__":
    gasto = calcular_calorias_gastas(45, "media")
    print(f"Gasto calórico estimado para o treino: {gasto} kcal")