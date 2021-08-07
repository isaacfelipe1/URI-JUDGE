#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
#pagar=0.0
#codigo=int(input())
#numero1=float(input())
#valor1=float(input())
#codigo2=int(input())
#numero2=int(input())
#valor2=float(input())
#pagar=numero1*valor1 + numero2*valor2
#print("VALOR A PAGAR: R$ %0.2f"%pagar)
linha = input().split()
codigo1=int(linha[0])
numero1=int(linha[1])
valor1=float(linha[2])
linha2=input().split()
codigo2=int(linha2[0])
numero2=int(linha2[1])
valor2=float(linha2[2])
pagar=numero1*valor1 + numero2*valor2
print("VALOR A PAGAR: R$ %0.2f"%pagar)


