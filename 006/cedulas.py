valor=int(input())
print(valor)
cedulas=[100,50,20,10,5,2,1]
for cedula in cedulas:
    qtd=int(valor/cedula)
    print("{} notas(s) de R${},00".format(qtd,cedula))
    valor-=qtd*cedula