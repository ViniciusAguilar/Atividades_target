import json

#abre os dados Json

with open("dados.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

#coloca o faturamento em uma lista
lista = []

for i in dados:
      if i['faturamento'] != 0:
          lista.append(i['faturamento'])
         

print(lista)
vmin = (min(lista))
vmax = (max(lista))

#pega os dias dos menores e maiores faturamentos e indica:

for a in dados:
    if vmin == a['faturamento']:
        print('no dia ', a['dia'], ' houve o menor faturamento de R$' ,vmin)
    if vmax == a['faturamento']:
        print('no dia ', a['dia'], ' houve o maior faturamento de R$' ,vmax)

#fazer a media
m = len(lista)
media = sum(lista)/m

#colocar os dias superiores a media mensal

for s in dados:
    if s['faturamento']> media:
        print('no dia ', s['dia'], ' houve um faturamento acima da media de de R$' ,s['faturamento'])


    

        



