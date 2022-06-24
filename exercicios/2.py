import json
count = 0
from statistics import mean
with open("dados.json",encoding='utf-8') as my_file:
    dados = json.load(my_file)
faturamentos =list()
for dia in dados:
    if dia['valor'] > 0:
        faturamentos.append(dia['valor'])
print(f'Faturamento minimo: {min(faturamentos):.2f}')
print(f'Faturamento maximo: {max(faturamentos):.2f}')
for tpv in faturamentos:
    if tpv > mean(faturamentos):
        count +=1
print(f'Quantidade de dias acima da média: {count}')
