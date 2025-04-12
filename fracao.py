class FracaoMista:
    def __init__(self, parte_inteira, numerador, denominador):
        # Construtor que inicializa a fração mista com parte inteira, numerador e denominador.
        self.parte_inteira = parte_inteira
        self.numerador = numerador
        self.denominador = denominador
        # Chamamos o método para simplificar a fração mista.
        self.simplificar()

    def simplificar(self):
        # Caso o numerador seja maior ou igual ao denominador, convertemos parte desse valor
        # para a parte inteira e ajustamos o numerador.
        if self.numerador >= self.denominador:
            self.parte_inteira += self.numerador // self.denominador  # Adiciona à parte inteira
            self.numerador %= self.denominador  # O restante fica como numerador
        
        # Calcula o máximo divisor comum (mdc) para simplificar a fração.
        mdc = self.mdc(self.numerador, self.denominador)
        self.numerador //= mdc  # Simplifica o numerador
        self.denominador //= mdc  # Simplifica o denominador

    def mdc(self, a, b):
        # Método que calcula o máximo divisor comum (mdc) usando o algoritmo de Euclides.
        while b:
            a, b = b, a % b  # Atualiza a e b com os valores intermediários até que b seja 0
        return a  # Quando b for 0, a será o mdc

    def __add__(self, outra_fracao):
        # Método de sobrecarga do operador + para somar duas frações mistas.
        
        # Converte a fração mista para fração imprópria:
        novo_numerador = self.parte_inteira * self.denominador + self.numerador
        outro_numerador = outra_fracao.parte_inteira * outra_fracao.denominador + outra_fracao.numerador
        
        # O denominador comum é o produto dos denominadores das duas frações.
        denominador_comum = self.denominador * outra_fracao.denominador
        
        # Soma os numeradores com base no denominador comum.
        soma_numeradores = novo_numerador * outra_fracao.denominador + outro_numerador * self.denominador
        
        # Calcula a nova parte inteira da fração mista após a soma.
        parte_inteira = soma_numeradores // denominador_comum
        
        # O novo numerador é o resto da divisão entre a soma dos numeradores e o denominador comum.
        novo_numerador = soma_numeradores % denominador_comum
        
        # Retorna uma nova fração mista com os valores resultantes.
        return FracaoMista(parte_inteira, novo_numerador, denominador_comum)

    def __str__(self):
        # Método que define a conversão para string da fração mista.
        if self.numerador == 0:
            # Se não há numerador, a fração é apenas a parte inteira.
            return str(self.parte_inteira)
        elif self.parte_inteira == 0:
            # Se a parte inteira é zero, retornamos apenas a fração.
            return f"{self.numerador}/{self.denominador}"
        else:
            # Se há parte inteira e fração, retornamos o formato misto.
            return f"{self.parte_inteira} {self.numerador}/{self.denominador}"

# Código para testes
if __name__ == "__main__":
    # Teste 1: Somando duas frações mistas.
    f1 = FracaoMista(0, 7, 6)  # Fração 7/6, que será simplificada para 1 1/6
    f2 = FracaoMista(0, 13, 7)  # Fração 13/7, que será simplificada para 1 6/7
    print(f"{f1} + {f2} = {f1 + f2}")  # Deve imprimir 3 5/42

    # Teste 2: Somando frações menores.
    f3 = FracaoMista(0, 1, 3)  # Fração 1/3
    f4 = FracaoMista(0, 2, 3)  # Fração 2/3
    print(f"{f3} + {f4} = {f3 + f4}")  # Deve imprimir 1

    # Teste 3: Somando frações maiores com parte inteira.
    f5 = FracaoMista(3, 1, 2)  # Fração mista 3 1/2
    f6 = FracaoMista(4, 2, 3)  # Fração mista 4 2/3
    print(f"{f5} + {f6} = {f5 + f6}")  # Deve imprimir 8 1/6
