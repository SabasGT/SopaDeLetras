from random import randint

def random_char():
    word = "abcdefghijklmnopqrstuvwxyz"
    chars = list(word)
    n = len(chars)
    return chars[randint(0,n - 1)]


def generate_soup(n, m):
    # n es la cantidad de filas; m es la cantidad de columnas
    soup = []
    for size in range(n):
        line = []
        for line_size in range(m):
            letter = random_char()
            line.append(letter)
        soup.append(line)
    return soup


def display_soup():
    n = int(input("Por favor ingrese la cantidad de filas de la Sopa de Letras: "))
    m = int(input("Por favor ingrese la cantidad de columnas de la Sopa de Letras: "))
    generatedSoup = generate_soup(n,m)
    for row in range(len(generatedSoup)):
        print(" ".join(generatedSoup[row]))


display_soup()
