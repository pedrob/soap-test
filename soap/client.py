from SOAPpy import SOAPProxy

server = SOAPProxy('http://localhost:8888/calc')

menu = "Selecionar operacoes\n[1]Somar\n[2]Subtrair\n[3]Dividir\n[4]Multiplicar\n[0]Sair"

run = True
while run:
    print(menu)
    op = input(":")
    if op == 1:
        a = int(input("Primeiro valor: "))
        b = int(input("Segundo valor: "))
        print(server.somar(a, b))
    elif op == 2:
        a = int(input("Primeiro valor: "))
        b = int(input("Segundo valor: "))
        print(server.subtrair(a, b))
    elif op == 3:
        a = int(input("Primeiro valor: "))
        b = int(input("Segundo valor: "))
        print(server.dividir(a, b))
    elif op == 4:
        a = int(input("Primeiro valor: "))
        b = int(input("Segundo valor: "))
        print(server.multiplicar(a, b))
    elif op == 0:
        run = False
    else:
        print("Opcao invalida")
