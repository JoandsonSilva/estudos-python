enunciado = '(Análise do seu nome ) - Fça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente - Ex. Ana Maria - Primeiro nome = ana - último nome = souza'

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))