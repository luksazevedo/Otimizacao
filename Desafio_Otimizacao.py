"""Desafio_Otimização.ipynb
"""

# importar o pulp
from pulp import *

#Dados do problema

itens = ['item1','item2','item3','item4','item5','item6','item7','item8']

capital = 1000000
custo = {'item1':470000,
        'item2':400000,
        'item3':170000,
        'item4':270000,
        'item5':340000,
        'item6':230000,
        'item7':50000,
        'item8':440000}

retorno ={'item1':410000,
        'item2':330000,
        'item3':140000,
        'item4':250000,
        'item5':320000,
        'item6':320000,
        'item7':90000,
        'item8':190000}

# Variáveis de decisão
var = LpVariable.dict("",(itens),cat = 'Binary')

# Criar o Problema
model = LpProblem("Otimização_investimento",LpMaximize)
# Criar fo
lista_fo =[]

for item in itens:
    lista_fo.append(var[item] * retorno[item])

model += lpSum(lista_fo)


# Criação das restrições
lista_rest = []

for item in itens:
    lista_rest.append(var[item]*custo[item])
    
model += lpSum(lista_rest) <= capital

# Restrições condicionais auxiliares
model += (var['item5']+var['item1'] <= 1) # se item 1 selecionado entao item 5 não deve ser

model += (var['item4']-var['item2'] >= 0) # se item 2 selecionado item 4 tbm deve ser


# Solução do modelo
print(model)
status = model.solve()
print(LpStatus[status])
print(f'O valor total da funçao objetivo é: R${value(model.objective)}')
print(" ")


for x in var.values():
    print(f'{x} = {value(x)}')

selecionados = []
for x in var.values():
  if value(x) ==1:
    selecionados.append(x)
print(" ")
print("Itens selecionados")
print(selecionados)