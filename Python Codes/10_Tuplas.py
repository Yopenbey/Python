t_carros=("HRV", "Golf", "Argo") #tupla
l_carros=list(t_carros)#Conversão da tupla para uma lista
l_carros[2]="Focus"#troca dos valores na lista
t_carros=tuple(l_carros)#conversão da lista para tupla

for x in t_carros:
    print(x)