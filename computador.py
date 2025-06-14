class Computador:
    def __init__(self, marca, memoria_ram, armazenamento):
        self.__marca = marca
        self.__memoria_ram = memoria_ram
        self.__armazenamento = armazenamento

    def get_marca(self):
        return self.__marca

    def get_memoria_ram(self):
        return self.__memoria_ram

    def get_armazenamento(self):
        return self.__armazenamento

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_memoria_ram(self, nova_memoria_ram):
        self.__memoria_ram = nova_memoria_ram

    def set_armazenamento(self, novo_armazenamento):
        self.__armazenamento = novo_armazenamento

    def ligar_computador(self):
        return f"O computador {self.__marca} está sendo ligado..."
