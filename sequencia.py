#Sequência de Fibonacci

#entrada
f = int(input('coloque um numero: '))
lista = [0,1]
n1 = 0
n2 = 1
#verificar se o numero está na sequencia

#cria a sequencia e coloca em uma lista
for i in range(f):
    r = n1 + n2
    n1 = n2
    n2 = r
    lista.append(r)

#verifica se o numero indicado bate com algum da lista
    
for a in range(len(lista)):
    b = lista[a]
    if b == f:
        print( 'o numero pertence a sequencia')
    else:
        if b == len(lista):
            print('o numero não pertence a sequencia')


 
print(lista)
    










































    
               
