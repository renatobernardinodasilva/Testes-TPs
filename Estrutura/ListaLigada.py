class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.inicio = None

    def inserirFim(self, numero):
        novo_no = No(numero)
        if self.inicio is None:
            self.inicio = novo_no 
            return
        ultimo_no = self.inicio
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        ultimo_no.proximo = novo_no

    def inserirInicio(self, numero):
        novo_no = No(numero)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    def inserir_apos(self, numero, novo_numero):
        no_atual = self.inicio
        while no_atual and no_atual.numero != numero:
            no_atual = no_atual.proximo
        if no_atual is None:
            raise ValueError("Número não encontrado na lista")
        novo_no = No(novo_numero)
        novo_no.proximo = no_atual.proximo
        no_atual.proximo = novo_no

    def delete_no(self, numero):
        if self.inicio is None:
            raise ValueError("Lista vazia")
        if self.inicio.numero == numero:
            self.inicio = self.inicio.proximo
            return
        no_atual = self.inicio
        while no_atual.proximo and no_atual.proximo.numero != numero:
            no_atual = no_atual.proximo
        if no_atual.proximo is None:
            raise ValueError("Número não encontrado na lista")
        no_atual.proximo = no_atual.proximo.proximo

    def imprimir_lista(self):
        no_atual = self.inicio
        while no_atual:
            print(no_atual.numero, end=" -> ")
            no_atual = no_atual.proximo
        print("FIM")

def main():
    lista = ListaLigada()
    lista.inserirFim(4)
    lista.inserirFim(5)
    lista.inserirInicio(6)
    lista.inserirInicio(7)
    lista.inserir_apos(4, 8)
    lista.delete_no(5)
    lista.imprimir_lista()

main()

class ListaOrdenada:
    def __init__(self):
        self.inicio = None

    def inserir(self, numero):
        novo_no = No(numero)
        if self.inicio is None or self.inicio.numero >= numero:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            no_atual = self.inicio
            while no_atual.proximo and no_atual.proximo.numero < numero:
                no_atual = no_atual.proximo
            novo_no.proximo = no_atual.proximo
            no_atual.proximo = novo_no

    def imprimir_lista(self):
        no_atual = self.inicio
        while no_atual:
            print(no_atual.numero, end=" -> ")
            no_atual = no_atual.proximo
        print("FIM")

def main_ordenada():
    lista = ListaOrdenada()
    lista.inserir(4)
    lista.inserir(2)
    lista.inserir(5)
    lista.inserir(1)
    lista.inserir(3)
    lista.imprimir_lista()

main_ordenada()