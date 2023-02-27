#entrada
frase = input('escreva algo: ')

#inverter
 #coloca tudo em uma lista
lista = []
for i in frase:
    lista.append(i)

 #inverte os caracteres da lista
invertido = []
for i in range(len(lista)-1, -1, -1):
    a = lista[i]
    invertido.append(a)

resultado = ''.join(invertido)
print(resultado)
