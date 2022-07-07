import json
# Só achei o arquivo JSON quando já havia enviado o teste, o e-mail acabou indo para a caixa de SPAM

arquivo = open('faturamento.json', 'r')

dados = json.load(arquivo)

array = []
i = 0
while i < len(dados['distribuidora']):
    array.append(int(dados['distribuidora'][i].get('faturamento')))
    i = i + 1

menor_valor = min(val for val in array if val > 0)
maior_valor = max(array)
media = sum(array) / len(array)

numero_de_dias = 0
for x in array:
    if x > media:
        numero_de_dias = numero_de_dias + 1

print(numero_de_dias)
