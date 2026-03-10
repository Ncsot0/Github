lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Longitud de la lista: ", len(lista))

SUMA = 0
for i in lista:
    SUMA += i
    
print(f"\nSuma de los elementos de la lista: {SUMA}")

mutiplicacion = 1
for i in lista:
    mutiplicacion *= i

print(f"\nMultiplicación de los elementos de la lista: {mutiplicacion}")
