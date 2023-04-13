import json 

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

diaMenorFaturamento = 0
valorMenorFaturamento = 0.0
diaMaiorFaturamento = 0
valorMaiorFaturamento = 0.0
diaPercorrido = 0

while diaPercorrido < 29:
    
        if diaMenorFaturamento != 0:
            valor1 = dados[diaMenorFaturamento-1] 
        else:
            valor1 = dados[diaMenorFaturamento]
        valor2 = dados[diaPercorrido+1]
                
        if (valor1['valor'] > valor2['valor']) and (valor2['valor']>0):
              diaMenorFaturamento = valor2['dia']
              valorMenorFaturamento = valor2['valor']
              
        else:
            diaMenorFaturamento = valor1['dia']
            valorMenorFaturamento = valor1['valor'] 

        diaPercorrido = diaPercorrido + 1

diaPercorrido = 0

while diaPercorrido < 29:
    
        if diaMaiorFaturamento != 0:
            valor1 = dados[diaMaiorFaturamento-1] 
        else:
            valor1 = dados[diaMaiorFaturamento]
        valor2 = dados[diaPercorrido+1]
                
        if (valor1['valor'] < valor2['valor']):
              diaMaiorFaturamento = valor2['dia']
              valorMaiorFaturamento = valor2['valor']
              
        else:
            diaMaiorFaturamento = valor1['dia']
            valorMaiorFaturamento = valor1['valor'] 

        diaPercorrido = diaPercorrido + 1        

diaPercorrido = 0
qtdDias = 0
soma = 0.0

while diaPercorrido < 30:
    valor1 = dados[diaPercorrido]['valor']
    soma = soma + valor1
    if valor1 != 0:
         qtdDias = qtdDias + 1
    diaPercorrido = diaPercorrido + 1

media = soma/qtdDias

diaPercorrido = 0 
qtdDiasMaiorMedia = 0

while diaPercorrido < 30:
    valor1 = dados[diaPercorrido]['valor']
    if valor1 > media:
        qtdDiasMaiorMedia = qtdDiasMaiorMedia + 1
    diaPercorrido = diaPercorrido + 1



print(f'O dia de menor faturamento foi o dia {diaMenorFaturamento} com o valor de: {valorMenorFaturamento}')
print(f'O dia de maior faturamento foi o dia {diaMaiorFaturamento} com o valor de: {valorMaiorFaturamento}')
print(f'A quantidade de dias com valor de faturamento maior que a média mensal desconsiderando os dias com valor nulo, é de: {diaMaiorFaturamento}, sendo que a média tem o valor de: {round(media, 2)}')




        





