
class Roupa:
    def __init__(self, tipo, cor, tamanho, preco):
        self.tipo = tipo 
        self.cor = cor  
        self.__tamanho = tamanho  
        self.__preco = preco  

    def obter_tamanho(self):
        return self.__tamanho

    def obter_preco(self):
        return self.__preco

    def exibir_informacoes(self):
        print(f"Roupa: {self.tipo}, Cor: {self.cor}, Tamanho: {self.__tamanho}, Preço: R${self.__preco:.2f}")

class CarrinhoDeCompras:
    def __init__(self):
        self.roupas = []  

    def adicionar_roupa(self, roupa):
        self.roupas.append(roupa)
        print(f"Roupa {roupa.tipo} de cor {roupa.cor} adicionada ao carrinho.")

    def remover_roupa(self, roupa):
        if roupa in self.roupas:
            self.roupas.remove(roupa)
            print(f"Roupa {roupa.tipo} de cor {roupa.cor} removida do carrinho.")
        else:
            print("A roupa não está no carrinho.")

    def calcular_total(self):
        total = sum([roupa.obter_preco() for roupa in self.roupas])
        return total

    def exibir_roupas(self):
        if not self.roupas:
            print("O carrinho está vazio.")
        else:
            print("Roupas no carrinho:")
            for roupa in self.roupas:
                roupa.exibir_informacoes()

class Cliente:
    def __init__(self, nome):
        self.nome = nome 
        self.carrinho = CarrinhoDeCompras()  

    def adicionar_roupa_ao_carrinho(self, roupa):
        self.carrinho.adicionar_roupa(roupa)

    def remover_roupa_do_carrinho(self, roupa):
        self.carrinho.remover_roupa(roupa)

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        print(f"Total da compra para {self.nome}: R${total:.2f}")


#exemplos
roupa1 = Roupa("Camiseta", "Azul", "M", 50.0)
roupa2 = Roupa("Calça", "Preta", "G", 120.0)
roupa3 = Roupa("Jaqueta", "Vermelha", "L", 200.0)

cliente = Cliente("Maria")

cliente.adicionar_roupa_ao_carrinho(roupa1)
cliente.adicionar_roupa_ao_carrinho(roupa2)

cliente.carrinho.exibir_roupas()

cliente.remover_roupa_do_carrinho(roupa1)

cliente.carrinho.exibir_roupas()

cliente.adicionar_roupa_ao_carrinho(roupa3)
cliente.finalizar_compra()
