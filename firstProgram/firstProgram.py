#esse programa:
#1- pergunta o nome do usuário
#2- diz quantos caracteres o nome dele tem
#3- pergunta a idade do usuário
#4- diz qual será a idade dele ano que vem

print('Hello world!')
print('What is your name?')
myName = input()
print('Nice to meet you, ' + myName + '!')
print('The length of your name is:')
print(len(myName)) #funcao len() é usada pra contar os caracteres de uma string ou de uma variavel contendo uma string
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
