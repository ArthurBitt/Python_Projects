class Conta:

    """Constuctor da Classe"""
    def __init__(self, numero, titular, saldo, limite):
        print("contruindo objeto {}".format(self))

        # Atributos da classe encapsulados
        self.__numero = numero       # self.__ ENCAPSULAMENTO DO ATRIBUTO, POSSIBILITANDO,
                                     # CONSULTAR APENAS POR MÉTODO
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco ="001"
    # Métodos da classe conta

    def extrato(self):
        """mostra o nome do titular e o saldo de um objeto da classe Conta"""
        print(f'Esse é o saldo na conta do titular {self.__titular} {self.__saldo}')

    # Método de teste lógico de poder sacar com base no limite
    def __pode_sacar(self, valor_saque): #privatizando o método, chamado apenas dentro da classe
        #variável valor diponível é o saldo mais o limite
        valor_disponivel = self.__saldo + self.__limite
        #condição lógica, o valor do saque só é permitido se for menor que o limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
        #Saca valor de um objeto da classe Conta"""
            self.__saldo -= valor
        else:
            print(f"o valor de {valor} solicitado excede o limite de retirada")

    def deposita(self, valor):
        """Deposita valor em um objeto da classe Conta"""
        self.__saldo += valor

    # encapsulamento do método transfeir// boa prática não escrever código da ação fora de uma função
    def transferir(self, conta_destino, valor):
        # da conta self.objeto/referência saca valor e passa para conta destino
        self.saca(valor)
        conta_destino.deposita(valor)

    # Métodos getter(print!) e setter(input!)
    #mostra o saldo do objeto que chama o método
    @property # @property =  get_método sem parÊntesis e sem get_
    def saldo(self):
        return self.__saldo

    #mostra o titular do objeto que chama o método
    @property # @property =  get_método sem parÊntesis e sem get_
    def titular(self):
        return self.__titular

    # mostra o limite do objeto que chama o método
    @property # @property =  get_método sem parÊntesis e sem get_
    def limite(self):
        return self.__limite

    #altera o valor do limite do objeto que chama o método
    @limite.setter  #@atributo.setter = rodando o método setter atributwo.set_método sem parêntesis e sem set_
    def limite(self,limite):
        self.__limite = limite

    @staticmethod #métodos estáticos são métodos das classes e não dos atributos dos objetos. Esse é passado sem o self
    def cod_banco():
        return "001"

    @staticmethod  # métodos estáticos são métodos das classes e não dos atributos dos objetos. Esse é passado sem o
    # self e sem parâmetros
    def cod_outros_bancos():
        return {"BB":"001", "CAIXA":"104","BRADESCO":"237"}



class Data:
    """Recebendo os paramêtros de dia, mÊs e ano"""
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print("objeto criado")

    """Passando os valores no formato (dia/ mês/ ano/)"""
    def formato_data(self):
        print(f'({self.dia}/{self.mes}/{self.ano})')


