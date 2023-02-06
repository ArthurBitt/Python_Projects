from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=lista)

#cada nova rota criada = uma nova def com return render template (caminho.thml)
@app.route('/novo')
def novo_game():
    #helper render_template
    return render_template("novo.html", titulo ="Novo Jogo")

#rota criar para utilizar no action do form com método post
@app.route('/criar', methods=['POST',])
def criar():
    # helper request referencias da propriedade name na tag input do html
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    objJogo = Jogo(nome, categoria, console)
    lista.append(objJogo)
    return render_template('lista.html', titulo="Jogos", jogos=lista)

#evitar o re runs debug=True
app.run(debug=True)