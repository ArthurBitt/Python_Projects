#List: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"] #os dados envolvidos por colchetes caracterizam uma lista

#A lista armazena vários tipos de dados
mylist2=["5", 5, 5.0, True]

print(mylist, mylist2)

#----------------------------------------------------interação--------------------------------------------------------------------

#list[index]
#len(list)
#list.count("item")
#if "item" in list
#for "item" in list


#os itens de uma lista podem ser consultados por sua ordem de indexação
item = mylist2[0]
print(item)

item = mylist[0]
print(item)

#o índex negativo percorre a lista em ordem decrescente
item = mylist[-1]
print(item)

item = mylist[-2]
print(item)

item = mylist[-3]
print(item)

# O tamnho da lista pode ser obtido através da função len()
mylist = ["banana", "cherry", "apple"]

print(len(mylist))

#o método .count("item") retorna quantas vezes o item se repete dentro da lista
mylist = ["banana", "cherry", "apple"]

print(mylist.count("banana"))

#verificar se um item está dentro da lista
mylist = ["banana", "cherry", "apple"]

if "banana" in mylist:
    print(f" {item} esta na lista")
else:
    print("o item não esta na lista")

#percorrer uma lista com loop
mylist = ["banana", "cherry", "apple"]

for item in mylist:
    print(item)
    
#---------------------------------------------------------------Mutabilidade/adicionar a lista----------------------------------------
#list.append("item")
#list.inser(pos, "item")
#list[índice] = "item"

#é possível adicionar itens na última posição de uma lista utilizando a função appen("item")
mylist = ["banana", "cherry", "apple"]

mylist.append("Lemon")
print(mylist)
if "Lemon" in mylist:
    print(f" {item} esta na lista")
else:
    print("o item não esta na lista")

#Para adicionar em uma posiçaõ específica é usado o insert(posição, "item")
mylist=["banana","cherry","apple"]

mylist.insert(0,"Lemon")
print(mylist)
if "Lemon" in mylist:
    print(f" {item} esta na lista")
else:
    print("o item não esta na lista")


#Para adicionar um item diretamente a um posição
mylist = ["banana", "cherry", "apple"]

mylist[1] = "Lemon"
print(f'aqui está no lugar da cherry, o {mylist[1]} adicionado')
if "Lemon" in mylist:
    print(f" {item} esta na lista")
else:
    print("o item não esta na lista")

#----------------------------------------------------------Mutabilidade/Remover da Lista----------------------------------------------
#list.pop()
#list.remove("item")
#list.clear()

#Para remover o último item da lista é usado a função pop()
mylist = ["banana", "cherry", "apple"]
print(mylist)
item = mylist.pop()
print(item)
print(mylist)

#indicando uma posição na função pop(index) essa irá apagar o item na posição passada
mylist = ["banana", "cherry", "apple"]
print(mylist)
item = mylist.pop(1)
print(item)
print(mylist)


#utilizar a função remove("item") permite excluir na lista um item em específico, para excluir todos, caso haja mais de um, é necessaário usar um loop
mylist = ["banana", "cherry", "apple"]

item=mylist.remove("cherry")
print(item)
print(mylist)

mylist = ["banana", "banana", "apple"]
item = mylist.remove("banana")
print(item)


#utilizar a função clear() irá apagar a lista, deixando-a vazia

mylist = ["banana", "cherry", "apple"]

item = mylist.clear()

print(item)#retorna none

print(mylist)

#------------------------------------------------------------Ordenar------------------------------------------------------------------
#.reverse() / [::-1]
# .sort()
#sorted(list)
#Usar a função reverse() irá inverter o sentido da lista
mylist = ["banana", "cherry", "apple"]

mylist.reverse()
print(mylist)

# Usar o slice [::-1]
mylist = ["banana", "cherry", "apple"]
print(mylist[::-1])


#a função sort() irá ordenar ou em ordem alfabética, pu numérica a lista
mylist = ["banana", "cherry", "apple"]#alfabética
#mylist2 = ["5", 5, 5.0, True]#Não suporta ordenar listas com dados diferenters
mylist3 = [11, 4, 6.0, ]

mylist.sort()
print(mylist)
#mylist2.sort()
mylist3.sort()
print(mylist3)


#usando a função sorted(list) a estrutura de dados passada na função será ordenada
mylist = ["banana", "cherry", "apple"]

new_list = sorted(mylist)

print(new_list)

#---------------------------------------------------------Slice----------------------------------------------------------------------
#slice - é um método de obter um lugar específico da lista, ou mesmo itens específicos dentro de uma sequência
#[:] toda a lista
#[1::1] 1<x até o final pulando de 1 em 1
#[::-1] inverte a estrutura complexa
#[:-1] outra notação para último valor




mylist = [1,2,3,4,5,6,7,8,9]
        # 0 1 2 3 4 5 6 7 8

mylist1 = ["A","R","T","H","U","R"]
        #   0   1   2   3   4   5

a = mylist[1:5]# é interpretado como pegue na lista os itens que estão entre o índex 1 e 5 sem sem incluir-los (1<x<5)
b = mylist1[1:5]

print(a)
print(b)

a = mylist[:-1:2]  # é interpretado como 0<x pulando de 2 em 2... note que o -1 indica o último valor da lista, portanto percorrerá toda a lista pulando com salto de 2 em 2 números
print(a)

#-----------------------------------------------------------------------Copiar uma Lista----------------------------------------------
#para copiar uma lista não basta simplesmente fazer uma lista1 = lista1copy, fazendo isso elas viram uma única lista, ou seja, ao mexer em uma, a outra também será alterada.

# list_copy = list.copy()
#list_copy = list[:]

list1 =[1,2,3]

list2 = list1

print(list1, list2)

list2.append(4)

print(list1, list2)#note que introduzindo 4 diretamente na lista 2, a lista1 também recebeu o valor


#A forma correta de copiar uma lista é utilizar o slice [:] correndo toda a lista que será copiada, ou usar a função copy()
list1 = [1, 2, 3]

#list2 = list1.copy()
list2 = list1[:]

print(list2)

list2.append(4)

print(list1, list2)#lista2 cotém o 4, mas lista1 não

#--------------------------------------------------------------List Comprehension-----------------------------------------------------
#listcomprehension listcomp = [ação(i+i) loop(for) sofrerá a ação(i in list1)]
list1 = [1, 2, 3]

listcomp = [i+i for i in list1]# em uma nova lista (listcomp) foi somado o valor de i por ele mesmo, usando o for levando em consideração os itens i na lista1

print(list1)
print(listcomp)



