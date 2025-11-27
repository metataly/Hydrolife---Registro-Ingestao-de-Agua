from models.dados_pessoais import DadosPessoais
from models.meta_diaria import MetaDiaria
from models.registro_ingestao import RegistroIngestao

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dados_pessoais = None
        self.meta_diaria = None
    
    
    def configurar_dados_pessoais(self, altura, peso, idade, sexo, fumante, ativ_fisica):
        dados = DadosPessoais(altura, peso, idade, sexo, fumante, ativ_fisica)
        self.dados_pessoais = dados
        
    def configurar_meta_diaria(self):
        meta = MetaDiaria()
        meta.calcular_meta(
            peso=self.dados_pessoais.peso,
            fumante=self.dados_pessoais.fumante,
            ativ_fisica=self.dados_pessoais.ativ_fisica
        )
        self.meta_diaria = meta

        
    def exibir_resumo_diario(self, registro_ingestao):
        meta = self.meta_diaria.quantidade_litros   # litros
        total = registro_ingestao.total_dia         # ml

        total_litros = total / 1000

        quanto_falta = meta - total_litros
        porcentagem = (total_litros / meta) * 100
        
        return int(quanto_falta * 1000), porcentagem