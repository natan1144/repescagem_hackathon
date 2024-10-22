# listas para onde vai as idades e o nomes 
lista_usuario = []
lista_idade = []

#Laço para repeti o codigo
while True:
    
    #Imprimindo opcoes do sistema 
    print(60*'_')
    print('1. Adicionar usuário')
    print('2. Listar usuário')
    print('3. Editar usuário')
    print('4. Remover usuário')
    print('5. Sair do sistema')
    print(60*'_')

#Recebendo qual e a opçao
    op = input('Digite qual das opções você quer: ')

#Opçao para adicionar usuario e idade
    if op == '1':
        nome = input('Digite qual o nome e o sobrenome do usuário que deseja adicionar: ')
        if nome != '':
            idade = int(input('Digite qual a idade do usuário: '))
            if idade <= 0:
                print(' Digite uma idade que seja positiva')
            else:
                lista_usuario.append(nome)
                lista_idade.append(idade)
                print(f'O usuario {nome} foi cadastrado com sucesso')


#Opçao para mostrar idade e nomes
    elif op == '2':
        print('________Nomes________')
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}º {n}')
        print('________Idades______')
        for j, x in enumerate(lista_idade):
            print(f'{j + 1}º {x} anos')

 #Opçao para mudar idade(editar)           
    elif op == '3':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}º {n}')
        indice = int(input('Indique o indice do usuário que deseja editar a idade: '))
        lista_idade.pop(indice - 1)
        idade2 = int(input('Digite a nova idade do usuário: '))
        lista_idade.insert(indice-1, idade2)
        print('Usuário editado com sucesso!')

#Opçao para excluir um usuario 
    elif op == '4':
        ind = int(input('Digite o número da posição do usuário que deseja excluir: '))
        lista_idade.pop(ind -1)
        lista_usuario.pop(ind - 1)

#Para finalizar o sistema (sair)
    elif op == '5':
        print('Sistema finalizado')
        break

