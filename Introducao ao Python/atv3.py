x = int(input("Digite um numero: "))

if x == 0: print("o numero é 0")
elif x>0 and x%2 == 0: print("Positivo e par")
elif x>0 and x%2 != 0: print("Positivo e impar")
elif x<0 and x%2 == 0: print("Negativo e par")
elif x<0 and x%2 != 0: print("Negativo e impar")