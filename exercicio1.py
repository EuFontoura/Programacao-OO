class Veículo:
    def __init__(self, marca, modelo, ano, combustivel) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = int(combustivel)

    def exibir_informacoes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCombustivel (L): {self.combustivel}"
    
    def mover(self):
        if self.combustivel > 0:
            quantidade = 10
            self.combustivel -= quantidade
            return f"O veículo {self.marca} está em movimento e consumiu {quantidade} Litros. Restam {self.combustivel} litros de combustivel"
        else:
            return f"O veículo {self.marca} não pode se mover. Combustível insuficiente!"
        
    def abastecer(self):
        quantidade = 10
        self.combustivel += quantidade
        return f"O combustível do veículo foi abastecido em {quantidade} litros"
    
class Carro(Veículo):
    def __init__(self, marca, modelo, ano, combustivel, portas) -> None:
        super().__init__(marca, modelo, ano, combustivel)
        self.__portas = portas

    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        return f"{info}\nPortas: {self.__portas}"
    
    def ligar_arcondicionado(self):
        return "Ar Condicionado ligado!"

class Moto(Veículo):
    def __init__(self, marca, modelo, ano, combustivel, cilindradas) -> None:
        super().__init__(marca, modelo, ano, combustivel)
        self.__cilindradas = cilindradas
    
    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        return f"{info}\nCilindradas: {self.__cilindradas}"
    
    def empinar(self):
        return "A moto está empinando"

carro1 = Carro("Ford", "Mustang GT", "2024", "120", "4")
moto = Moto("Honda", "MT-03", "2023", "90", "400")

print(carro1.exibir_informacoes())
print(carro1.mover())
