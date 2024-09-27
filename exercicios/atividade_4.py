class Carro:
    def __init__(self, marca, modelo, quilometragem):
        self.marca = marca 
        self.modelo = modelo  
        self.__quilometragem = quilometragem  
        self.__disponivel = True  

    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Carro {self.marca} {self.modelo} alugado com sucesso!")
        else:
            print(f"O carro {self.marca} {self.modelo} já está alugado.")

    def devolver(self, quilometragem_rodada):
        if not self.__disponivel:
            self.__quilometragem += quilometragem_rodada
            self.__disponivel = True
            print(f"Carro {self.marca} {self.modelo} devolvido com sucesso!")
        else:
            print(f"O carro {self.marca} {self.modelo} não está alugado.")

    def verificar_disponibilidade(self):
        return self.__disponivel

    def exibir_informacoes(self):
        estado = "Disponível" if self.__disponivel else "Alugado"
        print(f"Carro: {self.marca} {self.modelo}, Quilometragem: {self.__quilometragem} km, Estado: {estado}")


class Cliente:
    def __init__(self, nome):
        self.nome = nome  
        self.carros_alugados = []  

    def alugar_carro(self, carro):
        if carro.verificar_disponibilidade():
            carro.alugar()
            self.carros_alugados.append(carro)
        else:
            print(f"O carro {carro.marca} {carro.modelo} não está disponível para aluguel.")

    def devolver_carro(self, carro, quilometragem_rodada):
        if carro in self.carros_alugados:
            carro.devolver(quilometragem_rodada)
            self.carros_alugados.remove(carro)
        else:
            print(f"O carro {carro.marca} {carro.modelo} não foi alugado por {self.nome}.")

class Agencia:
    def __init__(self, nome):
        self.nome = nome  
        self.carros = []  

    def adicionar_carro(self, carro):
        self.carros.append(carro)
        print(f"Carro {carro.marca} {carro.modelo} adicionado à agência {self.nome}.")

    def exibir_carros_disponiveis(self):
        print(f"Carros disponíveis na agência {self.nome}:")
        for carro in self.carros:
            carro.exibir_informacoes()


# exemplo
carro1 = Carro("Toyota", "Corolla", 50000)
carro2 = Carro("Honda", "Civic", 30000)
carro3 = Carro("Ford", "Focus", 40000)

agencia = Agencia("Exclusiva Veiculos")

agencia.adicionar_carro(carro1)
agencia.adicionar_carro(carro2)
agencia.adicionar_carro(carro3)

cliente = Cliente("João")

cliente.alugar_carro(carro1)

agencia.exibir_carros_disponiveis()

cliente.devolver_carro(carro1, 150)

agencia.exibir_carros_disponiveis()
