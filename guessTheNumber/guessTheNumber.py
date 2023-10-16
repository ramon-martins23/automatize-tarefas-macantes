#1 esse programa vai gerar um numero aleatorio entre 1 e 20
#2 pedir pro usuario adivinhar
#3 se ele errar, dizer se o numero é maior ou menor do que o que deve ser adivinhado
#4 se ele acertar, dizer em quantas tentativas ele conseguiu.

import random
randomNum = random.randint(1,20) #1
print('I am thinking of a number between 1 and 20.')
i = 0
while True:
      i = i + 1
      guess = int(input('Take a guess: ')) #2
      if guess < randomNum:
            print('Your guess is too low.')#3
      elif guess > randomNum:
            print('Your guess is too high.')#3
      else:
            print(f'Good job! You guessed my number in {i} guesses!') #4
            break
            