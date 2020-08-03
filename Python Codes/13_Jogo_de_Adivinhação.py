import random
import os
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu número: "))
while(sorteado!=jogador):
    os.system('clear')
    if(sorteado>jogador):
        print("Erro, o número é maior")
    elif(sorteado<jogador):
        print("Erro, o número é menor")
    erros+=1
    jogador=int(input("Digite seu número: "))
print("Número " + str(jogador) + ", você acertou em " + str(erros+1) + " tentativas" )