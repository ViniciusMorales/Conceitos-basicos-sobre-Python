class Car:
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano

    def get_descricao(self):
        return f"{self.ano} {self.montadora} {self.modelo}"
    
    def set_ano(self, ano):
        self.ano = ano
    
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descricao())

my_car.set_ano(2021)
print(my_car.get_descricao())
    