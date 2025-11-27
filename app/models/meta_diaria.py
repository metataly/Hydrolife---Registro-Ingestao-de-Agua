class MetaDiaria:
    def __init__(self, peso=None, fumante=None, ativ_fisica=None, quantidade_litros=0):
        self.peso = peso
        self.fumante = fumante
        self.ativ_fisica = ativ_fisica
        self.quantidade_litros = quantidade_litros
        
    def calcular_meta(self, peso=None, fumante=None, ativ_fisica=None):

        if peso is not None:
            self.peso = peso
        if fumante is not None:
            self.fumante = fumante
        if ativ_fisica is not None:
            self.ativ_fisica = ativ_fisica

        if self.peso is None:
            raise ValueError("Peso não definido antes de calcular a meta.")

        # Lógica de cálculo
        if self.fumante:
            self.quantidade_litros = self.peso * 0.035 + 0.5
        elif self.ativ_fisica == "intenso":
            self.quantidade_litros = self.peso * 0.05
        elif self.ativ_fisica == "moderado":
            self.quantidade_litros = self.peso * 0.04
        else:
            self.quantidade_litros = self.peso * 0.035

        return self.quantidade_litros

    def ajustar_meta(self, peso=None, fumante=None, ativ_fisica=None):
        if peso is not None:
            self.peso = peso
        if fumante is not None:
            self.fumante = fumante
        if ativ_fisica is not None:
            self.ativ_fisica = ativ_fisica
