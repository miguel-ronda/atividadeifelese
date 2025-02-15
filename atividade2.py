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
if pesolutador < 55:
    print("categoria invalida")
else     
