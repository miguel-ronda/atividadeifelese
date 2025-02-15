#escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados recebidos:
#grau de aceitação de risco e o valor a ser investido.
#o grau de aceitação de risco deve ser lido no teclado na forma BX ou AL, se o valor fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor, deve ser um numero REAL 
print("miguel do amaral paes ronda")
grau_aceitacao = input("insira o grau de aceitacao do seu invetimento (Bx\Al) ")
investimento =  float (input ("agora, insira o valor de investimento "))
if grau_aceitacao == "Bx" : 
     if investimento < 1000.00:
          print(" invists na poupanca")
     else:
          print("invista na renda fixa")     
if grau_aceitacao == "Al":
     if investimento < 1000.00:
          print(" invists na bitcois")
     else:
          print("invista na acoes")    