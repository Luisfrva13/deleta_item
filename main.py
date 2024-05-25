
import time

#  lista
cidades = ['Brasília','Planaltina','Sobradinho','Santa Maria']

# informar a posição do item que será deletado
indice = int(input('Informe a posição do item que deseja deletar:'))
indice -= 1

# deletar item da lista
try:
    del(cidades[indice])


except:
    print('Não foi possível deletar')


# exibir a lista
for cidade in cidades:
    print(cidade)

