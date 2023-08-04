opc = str(input("C -> F Digite: c // F -> C Digite: "))
valor = int(input("Digite o valor: "))

if opc == "c": print(f"Valor em F: {(9/5)* valor+32}")
elif opc == "f": print(f"Valor em C: {(5/9)* (valor-32)}")
    