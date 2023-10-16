import random


def getAnswer(answerNumber): #dá uma resposta aleatória com base num número também aleatório
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
while True:
    r = input('Faça uma pergunta á bola mágica: ')
    if r == '': #se o user não digitar nada, ele pede novamente
        continue
    else: #se o user digitar algo, ele da a resposta aleatória
        print(getAnswer(random.randint(1,9))) #aqui é gerado o número aleatório e passado como parametro para a funcão
        
