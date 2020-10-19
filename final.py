import sys
import telnetlib
import math

host = '142.93.73.149'
port = 25909

connection = telnetlib.Telnet(host, port)
print(connection.read_until('ar: '))
connection.write('start')

while True:
  print(connection.read_until('es: '))
  entrada = connection.read_until(']\n')
  print(entrada)
  print(connection.read_until(': '))

  entrada2 = eval(entrada)
  linha_atual = entrada2[0:1]
  resposta = 0

  def calcula_distancia(linha_atual, proxima_linha = 0):
    respostaLista = []
    for i_proxima in range(len(proxima_linha)):
    
      if(i_proxima == 0):
        resposta = int(linha_atual[i_proxima]) + int(proxima_linha[i_proxima])
        respostaLista.append(resposta)
      if(i_proxima == 1):
        resposta = int(linha_atual[i_proxima-1]) + int(proxima_linha[i_proxima])
        respostaLista.append(resposta)
      if(i_proxima > 1):
        resposta1 = int(linha_atual[i_proxima-1]) + int(proxima_linha[i_proxima-1])
        resposta2 = int(linha_atual[i_proxima-1]) + int(proxima_linha[i_proxima])

        if(resposta1 < respostaLista[i_proxima-1]):
          respostaLista.pop(i_proxima-1)
          respostaLista.append(resposta1)
        
        respostaLista.append(resposta2)
      i_proxima += 1
    return respostaLista



  i=0
  indice = 1
  tamanho = 2

  while (indice  < len(entrada2)):
    
    proxima_linha = entrada2[indice:indice+tamanho]
    distancia_atual = list(calcula_distancia(linha_atual, proxima_linha))
    linha_atual = distancia_atual
    indice = indice + tamanho
    tamanho += 1      

  resposta = min(linha_atual)

  print('Resposta: ' + str(resposta))
  connection.write(str(int(resposta)))

connection.close()