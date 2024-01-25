print("Insira seu nome:: ")
nome = input()

while True:
    print(f"Seja bem vindo {nome} ao sistema integrado de contas e leitura de caracteres")
    print("1 para entrar no sistema de contas")
    print("2 para entrar no sistema de contagem de caracteres ")
    print("3 para encerrar o programa ")
    
    opc = input()

    if opc == "1":
        print("Escolha uma das operações para calcular: ")
        print("A para adição")
        print("B para subtração")
        print("C para multiplicação")
        print("D para Divisão ")
        cont = input()

        if cont == "A":
            print("Escolha um numero: ")
            n1 = int(input())
            print("Escolha outro numero: ") 
            n2 = int(input())
            nf = n1 + n2
            print(f"o resultado da sua conta foi {nf}")
        elif cont == "B":
            print("Escolha um numero: ")
            n1 = int(input())
            print("Escolha outro numero: ")
            n2 = int(input())
            nf = n1 - n2
            print(f"o resultado da sua conta foi {nf}")
        elif cont == "C":
            print("Escolha um numero: ")
            n1 = int(input())
            print("Escolha outro numero: ")
            n2 = int(input())
            nf = n1 * n2
            print(f"o resultado da sua conta foi {nf}")
        elif cont == "D":
            print("Escolha um numero: ")
            n1 = int(input())
            print("Escolha outro numero: ")
            n2 = int(input())
            nf = n1 / n2
            print(f"o resultado da sua conta foi {nf}")
            break

    elif opc == "2":
        print("Seja bem vindo ao sistema de contagem de caracteres: ")
        print("Por favor digite o seu texto ou palavra")
        palavra = input()
        quantidade_caracteres = len(palavra)
        print(f"A quantidade de caracteres da sua frase ou palavra é {quantidade_caracteres}")

    elif opc == "3":
        print("Programa encerrado, até mais")
        break