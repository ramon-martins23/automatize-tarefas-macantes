def eggs(someParameter):
      someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

#mesmo que a função não retorne nenhum valor, spam tem seu valor 
#alterado pois ambos spam e someParameter fazem referencia
#à mesma lista.