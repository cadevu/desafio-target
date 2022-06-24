
fibonacci = [0,1]
k=2
resp ='s'
while (resp == 's'):
    n = int(input("qual o número? "))
    while ( k <= n):
        prox_numero = fibonacci[k-1] + fibonacci[k-2]
        fibonacci.append(prox_numero)
        k+=1
    if n in fibonacci:
        print("O número está na sequencia")
    else:
        print("o número nao está na sequencia")
    resp = input("Deseja continuar? (s/n) ")
