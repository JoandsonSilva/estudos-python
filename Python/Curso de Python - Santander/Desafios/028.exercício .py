enunciado = 'Escreva um programa que faça o computador "pensar em um número inteiro entre 0 e e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador' \
'O programa deverá escrever na tela se o usuário venceu ou perdeu'



n1 = int(input('Digite um número de 0 a 5: '))

if n1==3:
  print('Você acertou! Parabéns ')
else:
  print(' Você errou, o computador venceu')