catNames = []
i = 0
while True:
  i += 1
  name = input(f'Entre o nome do gato {i} (ou não escreva nada pra parar): ')
  if i == 5:
    print('Você com certeza é uma tia dos gatos.')
  if name == '':
    break
  catNames = catNames + [name] 

print('Os nomes dos gatos:')
for name in catNames:
  print(name)