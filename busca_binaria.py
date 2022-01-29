from io import SEEK_SET
import os

procurado= int(input("insera o cep: "))
dados = "cep_ordenado.dat"
size_file= os.stat(dados).st_size
arquivo = open("cep_ordenado.dat", 'r')
tamanho_linhas=300
numero_linhas=size_file//tamanho_linhas

def busca(primeiro, ultimo, procurado):
  meio=(primeiro+ultimo)//2
  arquivo.seek(meio*tamanho_linhas, SEEK_SET)
  linha=arquivo.readline()
  cep=int(linha[290:298])
  print(cep)

  if(cep == procurado):
    print("Achou")
    print(linha)
 
  elif(procurado>cep):
    primeiro = meio+1
    busca(primeiro, ultimo, procurado)

  elif(procurado < cep):
    ultimo=meio-1
    busca(primeiro, ultimo, procurado)
  
  else:
   
    print("não encontrado")
  
busca(1, numero_linhas, procurado)
