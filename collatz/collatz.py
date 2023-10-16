#criar funcao que tenha um parametro chamado number
#se number for par, exibir number // 2 e retornar esse valor
#se for impar, exibir e retornar 3 * number + 1

def collatz(number):
      if int(number) % 2 == 0:
            return number // 2
      elif int(number) % 2 == 1:
            return 3 * number + 1



num = int(input('Enter number: ')) #atribui a entrada do usuário a variavel num

while num != 1: #enquanto o valor de num for diferente de 1,
      num = collatz(num) #atribui o valor de num à função collatz
      print(num)