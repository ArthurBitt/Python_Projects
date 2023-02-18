from flask import Flask #importar o Flask no arquivo
from flask import render_template  # vincular o html no arquivo.py

app = Flask(__name__)  # gerar uma instância (uma instância é uma criação de uma classe Flask. Quando você cria uma instância de Flask, você está criando uma aplicação web Flask.) obs. __name__ faz referência ao próprio arquivo/


#-------------------------------------------------------------------------------------------------------------------------------
#oque é uma rota e como cria-la

# Para definir uma rota no Flask, você usa um tipo especial de comando chamado "decorador". Isso ajuda o Flask a entender qual função deve ser chamada quando uma determinada rota é solicitada.



# Você pode pensar nas rotas como uma "mapa" de seu site - elas ajudam o Flask a encontrar o caminho correto para a página que a pessoa deseja visualizar. Por exemplo, se você quiser que a rota "/home" exiba a página inicial de seu site, você pode definir uma função para lidar com essa rota:

@app.route('/home')#decorador @app.route(/endereço da rota) - no caso o endereço remete a raíz, ou página inicial
def home():
    return '<h1>Bem-vindo à minha página inicial!</h1>'# São usadas tags html para renderizar no site o conteúdo do return

#Quando alguém digitar "www.meusite.com.br/home" em seu navegador, o Flask usará a rota que você definiu para chamar a função home() e exibir a mensagem "Bem-vindo à minha página inicial!" na página.
#------------------------------------------------------------------------------------------------------------------------------------

#executar a aplicação


#Quando você escreve um programa em Python, o Python lê o código do topo para baixo e executa cada linha na ordem em que aparece.

#Quando você escreve if __name__ == '__main__': em seu código, é como se você estivesse dizendo: "se eu estiver executando este arquivo diretamente (em vez de importá-lo para outro arquivo), execute o seguinte código".

#A linha if __name__ == '__main__': é como uma porta de entrada especial para seu programa. Quando o Python executa seu código, ele verifica se o nome do arquivo sendo executado é '__main__' - isso significa que o arquivo está sendo executado diretamente, em vez de ser importado por outro arquivo.

#Se o Python descobrir que o arquivo está sendo executado diretamente, ele executará todo o código app.run() que está indentado após a linha if __name__ == '__main__': . Isso é útil se você quiser testar o seu código ou executar alguma ação específica apenas quando o arquivo é executado diretamente.

if __name__ == '__main__':
    app.run()
#-----------------------------------------------------------------------------------------------------------------------------------

#Vinculando o HTML no flask (render_template)

# Primeiro, crie uma pasta chamada templates na mesma pasta onde você tem seu arquivo Python do Flask.

#Dentro da pasta templates, crie um arquivo HTML com o nome da página que você deseja exibir. Por exemplo, se você quiser exibir uma página de home, crie um arquivo chamado home.html.

#Abra o arquivo HTML e adicione o conteúdo da página. Certifique-se de que o arquivo tenha o código HTML completo, incluindo as tags < html > , < head > e < body > . Você pode adicionar CSS e JavaScript também.

#Agora, em seu arquivo Python do Flask, adicione uma rota que renderize o arquivo HTML. Para fazer isso, você precisará importar a função render_template do Flask.

#Em seguida, crie uma função que renderize o arquivo HTML. retorne uma  função render_template e passe o nome do arquivo HTML como argumento. A função render_template buscará o arquivo HTML na pasta templates automaticamente.


# from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')# render_template é retornado como um função que carrega a página login.html da pasta template


if __name__ == '__main__':
    app.run()
#---------------------------------------------------------------------------------------------------------------------------------

# Diretivas {{}} : Em resumo, as diretivas {{}} são usadas no Flask para colocar informações dinâmicas em um site e permitem que o Flask insira essas informações na página da web. São inseridas diretamente na página HTML entre as tags que receberão esse dado dinâmico.



#From flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():

    item =['item1', 'item2',  'item3']
    return render_template('home.html', item=item) #->  # <li > {{item}} < /li >


#<!DOCTYPE html >
#<html >
#<head >
  #<title > Minha lista de itens < /title >
#</head >
#<body >
  #<h1 > Minha lista de itens: < /h1 >
   #<ul >
       # {% for item in items % }
           # <li > {{item}} < /li >
       # {% endfor % }
    #</ul >
#</body >
#</html >


#-------------------------------------------------------------------------------------------------------------------------------------

# Diretivas> {%%}{%end%}

# Para usar uma estrutura de repetição, condicional ou printar dados dinamicamente no html usando o flask  é usada a diretiva        {% estrutura %} e {% endestrutura %} para passar os dados dinamicamente e encerrar a estrutura, em seguida, usar as diretivas {{}} dentro do bloco {% estrutura %} {% endestrutura %} para exibir esses dados na página da web.

# {% print() %} {% endprint %} // ou {{valor a ser exibido}}

# {% if (): %}{%else: %} {% endif %}

# {% for %} {% endfor %}

# {%# comentários no output da página html #%}


#From flask import flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)


@app.route('/inicio')
def inicio():
    #intanciando a classe Jogo

    jogo1 = Jogo("Tetri", "Puzzle", "Atari")
    jogo2 = Jogo("SKYRIM", "RPG", "Multiplataforma")
    jogo3 = Jogo("God of War", "Rack n' Slash", "Playstation")

    #passando os objetos criados em uma
    lista = ["jogo", "jogo2", "jogo3"]

    return render_template('inicio.html', jogos=lista) #-> <td > {{x.nome}} {{x.console}} {{x.categoria}} < /td >

if __name__=='main':
    app.run()

# <table>
#   <thead>
#     <tr>
#       <th>Nome</th>
#     </tr>
#   </thead>
#   <tbody>
#     {% for x in jogos %} a instrução é passada na própria diretiva 
#       <tr>
#         <td>{{ x.nome }}</td> x são os itens iterados da lista armazenda no render_template jogos. E que .nome é o nome do objeto
#          <td > {{x.categoria}} < /td >  .categoria  é a categoria  do objeto
#          <td > {{x.console}} < /td > .console é o console do objeto
#       </tr>
#    {% endfor %} É necessário fechar o for com uma diretiva ded fechamento para que não haja falhas nem perda de desempenho no código
#   </tbody>
# </table>

#------------------------------------------------------------------------------------------------------------------------------------

#Formulários como flask


# adicionar helper request.... from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/criar', methods=["POST",])  # criar nova rota, adicionar método post a rota
def criar():  # criar uma nova função com o nome da rota

    #passar na tag form do HTML propriedades action = "/rota criada" method = "post"
    # buscar na tag input a propriedade name, seu valor deve ser passado para o helper 
    #  <form action = "/criar" method = "post" >
    #         <fieldset >
    #             <div class = "form-group" >
    #                 <label for = "nome" > Nome < /label >
    #                 <input type = "text" id = "nome" name = "nome" class = "form-control" >
    #             </div >
    #             <div class = "form-group" >
    #                 <label for = "categoria" > Categoria < /label >
    #                 <input type = "text" id = "categoria" name = "categoria" class = "form-control" >
    #             </div >
    #             <div class = "form-group" >
    #                 <label for = "console" > Console < /label >
    #                 <input type = "text" id = "console" name = "console" class = "form-control" >
    #             </div >
    #             <button type = "submit" class = "btn btn-primary btn-salvar" > Salvar < /button >
    #         </fieldset >
    #     </form>
    # guardar em variáveis o request.form['valor da propriedade nome do input]
    nome = request.form['valor da propriedade name do input']
#criar um objeto com base na classe do formulário passando as variáveis da classe como parâmetro
    objeto = Classe(variáveis da classe,)
#retornar o render_template da rota de vizualização dos dados
return render_template('index.html', "diretivas")






    
    return render_template('')





#método post(passar informação para o servidor) e método get