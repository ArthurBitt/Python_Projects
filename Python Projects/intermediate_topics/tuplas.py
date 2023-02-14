#Tuplas: ordenadas, imutáveis e permitem duplicar elementos

mytuple = ("Arthur", 25, "São Paulo")# os dados envolvidos por parêntesis e separados por vírgula caracterizam uma tupla
print(mytuple)

mytuple = tuple(("Arthur", 25, "São Paulo"))#a função tuple transforma o dado nela contida em uma tupla
print(mytuple)


#mytuple = ("Arthur")/string  mytuple = ("Arthur",)/tupla - a vírgula é a única diferença, mas é a sintaxe correta nesse caso

mytuple = ("Arthur")
print(type(mytuple))
mytuple = ("Arthur",)
print(type(mytuple))

#os itens de uma tupla podem ser acessados pelo index 

mytuple = ("Arthur", 25, "São Paulo")

print(mytuple[0])#aceita normalmente que a busca seja feita por indexação do dado
print(mytuple[-1])#funciona com index negativo
print(mytuple[0:2])#aceita fatiamento

# #Tuplas são imutáveis, portanto, não aceitam adição ou exclusão de valores depois de prontas.

mytuple = ("Arthur", 25, "São Paulo")

#mytuple[1] = "26"#não irá inserir o valor na posição 1
#mytuple.append("26")#não irá adicionar 26 como string no final
#mytuple.insert(1, "26")  # não irá inserir o valor na posição 1
#mytuple.remove(25)#não irá excluir o valor 25 da estrutura
#mytuple.pop()#não irá excluir o último item

#É possível percorrer uma tupla com o loop for

for x in mytuple:
    print(x)

#É possível verificar se uma valor está em uma tupla com condicionais

if "Arthur" in mytuple:
    print("esta contido")

else:
    print("Não esta contido")

#O tamnho da tupla pode ser obtido através da função len()

mytuple = ("Arthur", 25, "São Paulo")

print(len(mytuple))

# o método .count("item") retorna quantas vezes o item se repete dentro da lista
mytuple = ("Arthur", 25, 25, "São Paulo")

print(mytuple.count(25))

#é possível descobrir o primeiro index de um item usando o método .index()

mytuple = ("A", "A", 25, "S")

print(mytuple.index("A"))#note que não retorna o segundo, apenas o primeiro

#desempacotando uma tupla

mytuple = ("Arthur", 25, "São Paulo")

name, age, city = mytuple #note que são geradas três variáveis para os três dados dentro da dupla. Assim a quantidade = len(tuple)

print(name)
print(age)
print(city)

# slice - é um método de obter um lugar específico da tupla, ou mesmo itens específicos dentro de uma sequência

mytuple = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 0 1 2 3 4 5 6 7 8

mytuple1 = ["A", "R", "T", "H", "U", "R"]
#   0   1   2   3   4   5

# é interpretado como pegue na lista os itens que estão entre o índex 1 e 5 sem sem incluir-los (1<x<5)
a = mytuple[1:5]
b = mytuple1[1:5]

print(a)
print(b)


a = mytuple[::-1]#retornará a tupla invertida
print(a)


a = mytuple[:-1:2]  # é interpretado como 0<x pulando de 2 em 2... note que o -1 indica o último valor da lista, portanto percorrerá toda a lista pulando com salto de 2 em 2 números
print(a)



