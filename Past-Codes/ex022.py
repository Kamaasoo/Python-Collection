nome = input('Digite o seu nome: ')
list = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print('O seu primeiro nome tem:{} letras!'.format(len(list[0])))
