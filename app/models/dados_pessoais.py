class DadosPessoais:
    def __init__(self, altura, peso, idade, sexo, fumante, ativ_fisica):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.fumante = fumante
        self.ativ_fisica = ativ_fisica

    def atualizar_dados(self, altura, peso, idade, sexo, fumante, ativ_fisica):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.fumante = fumante
        self.ativ_fisica = ativ_fisica

        
    def calcular_imc(self):
        self.imc = self.peso / (self.altura * self.altura)

        if self.imc < 18.5:
            classificacao = "Abaixo do peso"
        elif self.imc < 25:
            classificacao = "Peso Normal"
        elif self.imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        return self.imc, classificacao
