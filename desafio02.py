lista = []
opcao = 0
while opcao !=4:
    print('''    [ 1 ] inserir
    [ 2 ] remover
    [ 3 ] imprimir
    [ 4 ] sair''')
    opcao = int(input("Opcao: "))
    if opcao == 1:
        
        valor = (input("Digite um numero: "))

        if not valor.isdigit():
            print("Digite apenas numeros inteiros!")
        else:       
            num = 0
            verifica = int(valor) + int(num)
            if verifica<1 or verifica>15000: 
                print("Numero fora do range 1 a 15000...")
            else: 
                divisores = 0
                for divisor in range(1, verifica):
                    if verifica % divisor == 0:
                        divisores = divisores + 1
                    if divisores > 1:
                        break
                if divisores > 1:
                    if verifica in lista:
                        print("Numero já inserido")
                    else:     
                        lista.append(verifica) 
                else:
                    print("Numero primo, fora do range...")
              
            
    elif opcao == 2:
        remover = (input("Digite o valor a remover: "))
        validacao = 0
        if remover.isdigit():
            valida = int(validacao) + int(remover)
            if valida in lista:
                lista.remove(valida)
            else:    
                print("Numero nao esta na lista")
        else:
            print("Digite um inteiro positivo")    
    elif opcao == 3:
        print(lista)

    elif opcao == 4:
        print("Saindo...") 
    else:
        print("Opcao invalida. Tente novamente") 