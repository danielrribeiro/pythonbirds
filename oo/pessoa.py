class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    daniel = Pessoa(nome='Daniel')
    geraldo = Pessoa(daniel, nome='Geraldo')
    print(Pessoa.cumprimentar(geraldo))
    print(id(geraldo))
    print(geraldo.cumprimentar())
    print(geraldo.nome)
    print(geraldo.idade)
    for filho in geraldo.filhos:
        print(filho.nome)
    geraldo.sobrenome = 'Ribeiro'
    del geraldo.filhos
    geraldo.olhos = 1
    del geraldo.olhos
    print(daniel.__dict__)
    print(geraldo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(geraldo.olhos)
    print(daniel.olhos)
    print(id(Pessoa.olhos), id(geraldo.olhos), id(daniel.olhos))