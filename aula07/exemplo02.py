previsoes = ['Ensolarado','Nublado','Chuvoso','Tempestade','Ensolarado']
# print(previsoes)

PREVISAO_FELIZ = 'Ensolarado'

for p in previsoes:
    if p == PREVISAO_FELIZ:
        print('Vai passear')
    elif p == 'Tempestade':
        print('Não saia de casa')
    else:
        print('leva um guarda-chuva')