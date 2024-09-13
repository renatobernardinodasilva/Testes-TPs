# tartarugas.py

class Tartaruga:
    equipe_original = ["Michelangelo", "Leonardo", "Donatello", "Raphael"]
    armas_originais = ["katana", "nunchaku", "bo", "sai"]

    def __init__(self, nome, idade, arma, nivel_radiacao):
        self.nome = nome
        self.idade = idade
        self.arma = arma
        self.nivel_radiacao = nivel_radiacao

    def is_qualificada(self):
        if self.nome in Tartaruga.equipe_original:
            return False
        if self.arma in Tartaruga.armas_originais:
            return False
        if not (15 >= self.idade <= 30):
            return False
        if not (30 >= self.nivel_radiacao <= 80):
            return False 
        return True

class Recrutamento:
    def __init__(self):
        self.tartarugas = []

    def adicionar_tartaruga(self, tartaruga):
        self.tartarugas.append(tartaruga)

    def listar_qualificadas(self):
        return [t for t in self.tartarugas if t.is_qualificada()]