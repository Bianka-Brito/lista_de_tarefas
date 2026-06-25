lista = [ ]

while True: 
    print(50*'-')
    print('1- Adicionar tarefa \n2- Listar tarefas \n3- Remover tarefa \n4- Marca tarefa feita \n5- Sair')
    menu = int(input('O que vamos fazer: '))
    print(50*'-')

    if menu == 1: 
        tar = int(input('Digite quantas tarefas você quer adicionar: '))
        for i in range(0, tar):
            tarefas = input(f'Digite a tarefa {i+1}: ' )
            lista.append([tarefas, False])

    elif menu == 2: 
        print('Tarefas: \n')

        if len(lista) == 0:
            print('Nenhuma tarefa cadastrada')

        for i in range(len(lista)):
            if lista[i][1] == True: 
                status = '[X]'
            else:
                status = '[ ]'
            print(f'{i+1} - {status} {lista[i][0]}')

    elif menu == 3:
        remover = int(input('Digite o número da tarefa que você deseja remover: '))
        if remover >= 1 and remover <= len(lista):
            lista.pop(remover - 1)
            print('Tarefa removida!')
        else: 
            print('Tarefa não encontrada')
    
    elif menu == 4:
        concluir = int(input('Digite o número da tarefa que deseja concluir: '))

        if concluir >= 1 and concluir <= len(lista):
            lista[concluir - 1][1] = True
            print('Tarefa concluída!')
        
        else: 
            print('Tarefa não encontrada')

    elif menu == 5:
        print('Saindo...')
        break 