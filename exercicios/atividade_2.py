class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo  
        self.autor = autor 
        self.__preco = preco  
        self.__estoque = estoque  


    def obter_preco(self):
        return self.__preco


    def verificar_disponibilidade(self, quantidade):
        return self.__estoque >= quantidade


    def atualizar_estoque(self, quantidade):
        if self.verificar_disponibilidade(quantidade):
            self.__estoque -= quantidade
            return True
        else:
            print(f'Estoque insuficiente para o livro: {self.titulo}')
            return False



class Pedido:
    def __init__(self, livro, quantidade):
        self.livro = livro 
        self.quantidade = quantidade  

    def calcular_total(self):
        if self.livro.verificar_disponibilidade(self.quantidade):
            return self.livro.obter_preco() * self.quantidade
        else:
            return 0

    def processar_pedido(self):
        if self.livro.atualizar_estoque(self.quantidade):
            print(f'Pedido de {self.quantidade} livro(s) "{self.livro.titulo}" processado com sucesso.')
        else:
            print(f'Não foi possível processar o pedido de {self.quantidade} livro(s) "{self.livro.titulo}".')



class Cliente:
    def __init__(self, nome):
        self.nome = nome  
        self.pedidos = []  

    def fazer_pedido(self, pedido):
        if pedido.calcular_total() > 0:
            self.pedidos.append(pedido)
            pedido.processar_pedido()
        else:
            print(f'O pedido de {pedido.quantidade} livro(s) "{pedido.livro.titulo}" não pode ser realizado.')

    def exibir_pedidos(self):
        print(f'Pedidos de {self.nome}:')
        for pedido in self.pedidos:
            total = pedido.calcular_total()
            print(f'{pedido.quantidade}x {pedido.livro.titulo} - Total: R${total:.2f}')


#exemplos
livro1 = Livro("O Senhor dos Anéis", "autor tal", 50.0, 10)
livro2 = Livro("Revoluçao dos Bichos", "George Orwell", 40.0, 5)

cliente = Cliente("maria")

pedido1 = Pedido(livro1, 2)
pedido2 = Pedido(livro2, 1)

cliente.fazer_pedido(pedido1)
cliente.fazer_pedido(pedido2)

cliente.exibir_pedidos()
