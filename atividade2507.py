class Fruta:
    def __init__(self, frutas, producao, insumos, mudas_sementes, arrendamento, mao_obra):
        self.frutas = frutas
        self.producao = producao
        self.insumos = insumos
        self.mudas_sementes = mudas_sementes
        self.arrendamento = arrendamento
        self.mao_obra = mao_obra
    
    def calcular_tudo(self):
        return (
        self.producao +
        self.insumos +
        self.mudas_sementes +
        self.arrendamento +
        self.mao_obra)
    
    def relatorio_tudo(self):
        print(f" Fruta: {self.frutas}")
        print(f" Quanto de Produção: R$ {self.producao}")
        print(f" Quanto de Insumos: R$ {self.insumos}")
        print(f" Valor Mudas ou sementes: R$ {self.mudas_sementes}")
        print(f" Gasto com Arrendamento: R$ {self.arrendamento}")
        print(f" Mão de Obra Gasta: R$ {self.mao_obra}")
        print(f" Total de Tudo: R$ {self.calcular_tudo()}\n")

frutas = [
    Fruta("Morango", 1500, 250, 150, 300, 500),
    Fruta("Pêra", 1000, 125, 90, 159, 290),
    Fruta("Acerola", 1900, 145, 120, 240, 350),
    Fruta("Laranja", 1690, 240, 200, 305, 395),
    Fruta("Abacate", 2150, 300, 50, 150, 490)
    ]

gasto_total = 0
for fruta in frutas:
    fruta.relatorio_tudo()
    gasto_total += fruta.calcular_tudo()

print(f"Gasto Total Geral: R$ {gasto_total}")