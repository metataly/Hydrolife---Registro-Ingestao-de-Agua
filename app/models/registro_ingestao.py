from datetime import datetime

class RegistroIngestao:
    def __init__(self):
        self.registros = []

    def registrar_ingestao(self, quantidade_ml):
        self.registros.append({
            "quantidade_ml": quantidade_ml,
            "data": datetime.now().strftime("%Y-%m-%d")
        })

    @property
    def total_dia(self):
        hoje = datetime.now().strftime("%Y-%m-%d")
        return sum(item["quantidade_ml"] for item in self.registros if item["data"] == hoje)

