class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome  
        self.cargo = cargo  
        self.__salario = salario  

    def obter_salario(self):
        return self.__salario

    def alterar_salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
            print(f"Salário de {self.nome} alterado para R${novo_salario:.2f}")
        else:
            print("Salário inválido! O salário deve ser positivo.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.__salario:.2f}")


class Departamento:
    def __init__(self, nome):
        self.nome = nome  
        self.funcionarios = []  

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} adicionado ao departamento {self.nome}.")

    
    def exibir_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for funcionario in self.funcionarios:
            funcionario.exibir_informacoes()

class Empresa:
    def __init__(self, nome):
        self.nome = nome  
        self.departamentos = []  

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)
        print(f"Departamento {departamento.nome} adicionado à empresa {self.nome}.")

    def exibir_departamentos(self):
        print(f"Departamentos da empresa {self.nome}:")
        for departamento in self.departamentos:
            departamento.exibir_funcionarios()


#ex
funcionario1 = Funcionario("Manu", "Engenheira de Software", 8000)
funcionario2 = Funcionario("Gustavo", "Analista de Sistemas", 6500)
funcionario3 = Funcionario("Bruno", "Gerente de Projetos", 12000)

departamento_ti = Departamento("TI")
departamento_gerencia = Departamento("Gerência")

departamento_ti.adicionar_funcionario(funcionario1)
departamento_ti.adicionar_funcionario(funcionario2)
departamento_gerencia.adicionar_funcionario(funcionario3)

empresa = Empresa("Fasa")
empresa.adicionar_departamento(departamento_ti)
empresa.adicionar_departamento(departamento_gerencia)


empresa.exibir_departamentos()

funcionario1.alterar_salario(8500)

empresa.exibir_departamentos()
