idades = [1,2,3,4]
idades.append(5)
idades.insert(0,0)
idades.extend([6,7,8,9,10])

if 5 in idades:
    print(True)
    
for i in idades:
    print(i)
    
    
def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()