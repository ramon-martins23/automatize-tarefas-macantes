def spam():
  eggs = 'spam local'
  print(eggs) #exibe 'spam local'
  
def bacon():
  eggs = 'bacon local'
  print(eggs) #exibe 'bacon local'

eggs = 'eggs global'
bacon()
print(eggs)
