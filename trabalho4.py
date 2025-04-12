from abc import ABC, abstractmethod

# Classe abstrata Terreno, usada como base para diferentes tipos de terrenos.
class Terreno(ABC):

    # Método construtor que inicializa a localização e o preço do terreno.
    def __init__(self, localizacao, preco):
        self.__localizacao = localizacao  # Localização do terreno (atributo privado)
        self.__preco = preco  # Preço do terreno (atributo privado)

    # Propriedade para acessar a localização do terreno.
    @property
    def localizacao(self):
        return self.__localizacao

    # Setter para modificar a localização do terreno.
    @localizacao.setter
    def localizacao(self, valor):
        self.__localizacao = valor

    # Propriedade para acessar o preço do terreno.
    @property
    def preco(self):
        return self.__preco
    
    # Setter para modificar o preço do terreno.
    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    # Método abstrato para calcular o peso do terreno, deve ser implementado nas subclasses.
    @abstractmethod
    def calcula_peso(self):
        pass

# Classe Circular que herda de Terreno, representando terrenos de forma circular.
class Circular(Terreno):

    # Método construtor que inicializa a localização, o preço e o raio do terreno circular.
    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)  # Chama o construtor da classe mãe (Terreno).
        self.__raio = raio  # Raio do terreno (atributo privado)
    
    # Propriedade para acessar o raio do terreno circular.
    @property
    def raio(self):
        return self.__raio
    
    # Implementação do método abstrato para calcular o peso de um terreno circular.
    # O peso é o preço dividido pela área do círculo (π * raio²).
    def calcula_peso(self):
        return (self.preco) / (3.14 * self.__raio * self.__raio)

# Classe Retangular que herda de Terreno, representando terrenos de forma retangular.
class Retangular(Terreno):

    # Método construtor que inicializa a localização, o preço, o lado menor e o lado maior do terreno retangular.
    def __init__(self, localizacao, preco, lado_menor, lado_maior):
        super().__init__(localizacao, preco)  # Chama o construtor da classe mãe (Terreno).
        self.__lado_menor = lado_menor  # Lado menor do terreno (atributo privado)
        self.__lado_maior = lado_maior  # Lado maior do terreno (atributo privado)

    # Propriedade para acessar o lado menor do terreno retangular.
    @property
    def lado_menor(self):
        return self.__lado_menor
    
    # Propriedade para acessar o lado maior do terreno retangular.
    @property
    def lado_maior(self):
        return self.__lado_maior
    
    # Implementação do método abstrato para calcular o peso de um terreno retangular.
    # O peso é o preço dividido pela área do retângulo (lado menor * lado maior).
    def calcula_peso(self):
        return (self.preco) / (self.__lado_menor * self.__lado_maior)

# Bloco principal de execução.
if __name__ == "__main__":
    
    # Cria instâncias de terrenos circulares e retangulares.
    terreno1 = Circular('Vila Rubens', 70000, 15)
    terreno2 = Retangular('Morro Chic', 75000, 20, 35)
    terreno3 = Circular('Centro', 110000, 20)

    # Lista de terrenos para comparação.
    terrenos = [terreno1, terreno2, terreno3]
    
    # Inicializa o terreno com o melhor preço como o primeiro da lista.
    melhor_preco = terreno1
    
    # Percorre todos os terrenos, imprimindo suas informações e comparando os pesos.
    for terreno in terrenos:
        print(f"Localização: {terreno.localizacao}, Preço: {terreno.preco}, Peso: {terreno.calcula_peso():.2f}")

        # Atualiza a variável 'melhor_preco' se o terreno atual tiver um peso menor.
        if terreno.calcula_peso() < melhor_preco.calcula_peso():
            melhor_preco = terreno

    # Imprime a melhor opção de terreno (com menor peso).
    print('\nMelhor opção:')
    print(f"Localizacao: {melhor_preco.localizacao}, Preço: {melhor_preco.preco}, Peso: {melhor_preco.calcula_peso():.2f}")
