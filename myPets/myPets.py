myPets = ['Hope','Amora', 'Victor']
userPet = input('Escreva o nome de um pet: ')
if userPet not in myPets:
  print(f'Eu não tenho um pet chamado {userPet}. ')
else:
  print(f'{userPet} é meu pet.')