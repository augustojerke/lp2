idade = int(input("Digite sua idade: "))

if idade < 5: print("Categoria Indefinida!")
elif idade <= 7: print("Categoria Infantil A")
elif idade <= 10: print("Categoria Infantil B")
elif idade <= 13: print("Categoria Juvenil A")
elif idade <= 17: print("Categoria Juvenil B")
else: print("Adulto")