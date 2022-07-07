dados = [{"estado": "SP", "faturamento": 67836.43}, {"estado": "RJ", "faturamento": 36678.66},
         {"estado": "MG", "faturamento": 29229.88}, {"estado": "ES", "faturamento": 27165.48},
         {"estado": "OUTROS", "faturamento": 19849.53}]

i = 0
array = []
faturamento_total = 0
while i < len(dados):
    faturamento_total = faturamento_total + dados[i].get('faturamento')
    i = i + 1

estados = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']


def representacao_estado(estado):
    index = estados.index(estado.upper())
    percentual = (dados[index].get('faturamento') / faturamento_total) * 100
    print(f'O estado de {estado.upper()} teve uma contribuição de {percentual:.2f}% no faturamento da empresa')


representacao_estado('SP')
representacao_estado('mg')
representacao_estado('RJ')
representacao_estado('es')
