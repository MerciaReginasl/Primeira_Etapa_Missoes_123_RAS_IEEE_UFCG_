#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROCESSO SELETIVO CAPITULO RAS - IEEE UFCG
#CANDIDATA: MERCIA REGINA DA SILVA

#Missão 2.0: Conhecendo o OpenCV e Numpy 


# In[2]:


import cv2


# In[3]:


import numpy as np


# In[4]:


# A Visão Computacional constroi sistemas artificiais obtendo as informações das imagens ou quaisquer 
# dados multidimensionais. Neste código a imagem de entrada passará por alterações em seu formato em cada execução.
# Temos:


# In[5]:


# Iniciamos com a importação das bibliotecas Opencv - cv2 e a numpy para que os comandos sejam executados.
# Neste In [12] temos a leitura da imagem com a função imread() que permite a importação de imagens de um 
# arquivo em vários formatos e a associação de cada pixel a um elemento de uma matriz.

# A função imshow mostra a figura e podemos atribuir o nome a janela

# E por fim a imagem é escrita, ou seja, gravada no disco.


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("My Dog Marley", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg", imagem)


# In[ ]:


# E a função de leitura da imagem é executada novamente 

# A imagem é lida e armazenada 


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')


# In[ ]:


# Neste comando temos a mostra das caracteristicas da imagem que é uma matriz de 3 dimensões (3 canais):
# RGB (R= red, G=green, B=Blue), porém neste comando a ordem está alterada, logo as cores em sequência as cores
#serem lidas são B=blue, G=green e R=red


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')
(b, g, r) = imagem[0, 0] 


# In[ ]:


# Neste comando será impresso o pixel seguindo a sequência de cores RGB que é a padrão.


# In[ ]:


print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)


# In[ ]:


#A imagem representa uma matriz de inteiros onde cada célula é um inteiro sem sinal de 8 bits que representa o 
# sistema RGB, onde cada pixel da imagem é composta por 3 componentes de 8 bits.
# Observa-se os valores acima, onde é indicado as cores (capacidade de reprodução) de cada cor atribuida.


# In[ ]:


# A sequência de repetições dos eixos y e x que formam a imagem (no caso a imagem é horizontal)
# for y in range(0, imagem.shape[0]): percorre linhas
# for x in range(0, imagem.shape[1]): percorre colunas


# In[ ]:


#A forma de uma imagem é acessada por img.shape. Ele retorna uma tupla do número de linhas, 
#colunas e canais neste comando a imagem é colorida): print (255,0,0)


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')
for y in range(0, imagem.shape[0]):
for x in range(0, imagem.shape[1]):
imagem[y, x] = (255,0,0)
cv2.imshow("/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg", imagem)


# In[ ]:


#for y in range(0, imagem.shape[0]): percorre linhas
# for x in range(0, imagem.shape[1]): percorre colunas

# As variáveis componentes da cor devem assumir valores entre 0 e 255, neste caso foi atribuído x%256
# (resto da divisão por 256), mantendo o resultado entre 0 e 255.

# A alteração nas componentes das cores da imagem geram um efeito na imagem em formato de cubos coloridos (pixels)


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
for x in range(0, imagem.shape[1], 1): #percorre as colunas
imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg", imagem)
cv2.waitKey(0)


# In[ ]:


# No comando acima a alteração nas componentes das cores da imagem é realizada conforme as 
# coordenadas de linha e coluna 


# In[ ]:


imagem = cv2.imread('/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg')
for y in range(0, imagem.shape[0], 10): #percorre linhas
for x in range(0, imagem.shape[1], 10): #percorre colunas
imagem[y:y+5, x: x+5] = (0,255,255)
cv2.imshow("/home/dell/Downloads/MEUS_DOCS_/projeto_opencv/coisas-incriveis-sobre-seu-cachorro.jpg", imagem)
cv2.waitKey(0)


# In[ ]:


# Portanto, foram abordados nas execuções a representação de 3 cores no sistema RGB para cada pixel da imagem
# colorida.

# O sistema de coordenadas e maninpulação de pixel podemos alterar a cor individualmente para cada pixel e 
# podem se manipulados.

