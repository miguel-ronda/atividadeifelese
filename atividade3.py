#uma empresa financeira consegue empréstimos a pessoas físicas, quando o valor da parcela e menor que 8% do salario da pessoa.
#escreva um programa que leia dois números REAIS o valor do salario e o valor da parcela e informe se o empréstimo será concedido ou não.
salariototal = int(input("qual seu salario"))
parcelas = int(input("quantas parcelas voce quer"))
emprestimototal = int(input("quanto de dinheiro voce quer"))

taxa = salariototal * 0.08
if taxa >= emprestimototal:
    print("o emprestmo sera concedido")
else:
    print("infelizmnete o emprestimo nao sera concedido")
    

