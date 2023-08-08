def calcular_custo_chamada(duracao):
    custo_base = 1.15
    custo_adicional_por_minuto = 0.26

    if duracao <= 3:
        total = custo_base
    else:
        minutos_adicionais = duracao - 3
        custo_adicional = minutos_adicionais * custo_adicional_por_minuto
        total = custo_base + custo_adicional
    
    return total

duracao_chamada = int(input("Digite a duração da chamada em minutos: "))
custo_total = calcular_custo_chamada(duracao_chamada)
print(f"O total a ser pago é R$ {custo_total:.2f}")
