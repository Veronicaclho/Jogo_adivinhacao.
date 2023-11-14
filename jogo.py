from random import randint
computador=randint(0, 5) #faz o computador pensar
print('-=-'*20)
print('Vou pensar em um entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que número você está pensando? ')) #jogador tenta adivinhar
if jogador == computador:
    print('Parabéns! Você me venceu!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')