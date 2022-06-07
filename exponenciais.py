#na lista abaixo foi criado uma lista Y que é o elevado da lista X. Para isto, foi criado uma lista x, depois a lista Y vazia, feito um for na x e adicionado os elementos dela com as exponenciais (representado por **).

x=[1, 2, 3, 4, 5]
y=[]
for i in x:
  y.append(i**2)
print(x)
print(y)