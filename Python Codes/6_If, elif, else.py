clima="noite"
dinheiro=400
lugar=""

if clima=="ensolarado" and(dinheiro>=300 and dinheiro<=500):
    lugar="clube"
    print("Eu vou para o " + lugar)
elif clima=="noite":
    lugar="cinema"
    print("Eu vou para o " + lugar)
else:
    lugar="casa"
    print("eu vou ficar em " + lugar)

