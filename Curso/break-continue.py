#imprimir solo las letras a
for letra in "anaconda":
    if letra == "a":
        print(letra)
        break
    else:
        print("fin ciclo for")
#Break rompe todo el ciclo inclusive con sentencias despues del mismo

#imprimir solo numeros pares
for i in range(10):
    if i%2 == 0:
        print(i)

#Utilizando continue (Logica invertida)
for i in range(10):
    if i%2 == 0:
        continue
    print(i)