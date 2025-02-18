#escreva um programa para exibir na tela o nome e a categoria de um lutador. o programa deve ler em STRING para o nome e o NUMERO REAL para o peso.
#conforme o peso ocorrera o enquadramento na categoria.

#maior ou igual a 52 e menor doque 65: categoria pena
#maior ou igual a 65 e menor doque 72: categoria leve
#maior ou igual a 72 e menor doque 79: categoria ligeiro
#maior ou igual a 79 e menor doque 86: meio médio 
#maior ou igual a 86 e menor doque 90: categoria médio
#maior ou igual a 90 e menor doque 100: meio pesado
#maior ou igual a 100: pesado 

print("miguel do amaral paes ronda")
nomelutador = str(input("insira o nome do combatente "))
pesolutador = float(input("insira o peso"))
print(nomelutador)
if pesolutador >= 52 and pesolutador <65:
    print("{} sua gategoria e pena".format(nomelutador))
elif pesolutador >= 65 and pesolutador <72:
    print("{} sua gategoria e leve".format(nomelutador))
elif pesolutador >= 72 and pesolutador <79:
    print("{} sua gategoria e pligeiro".format(nomelutador))
elif pesolutador >= 79 and pesolutador <86:
    print("{} sua gategoria e meio-medio".format(nomelutador))
elif pesolutador >= 86 and pesolutador <90:
    print("{} sua gategoria e medio".format(nomelutador))
elif pesolutador >= 86 and pesolutador <100:
    print("{} sua gategoria e meio-pesado".format(nomelutador))
elif pesolutador >= 100:
    print("{} sua gategoria e pesado".format(nomelutador))
else:
    print("categoria invalida")

