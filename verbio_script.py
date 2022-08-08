from data_verbio import list_of_words

new_list = list_of_words



# TODO > INCLUDE LETTERS
def include_letter_from_list(excluded_letter):
    i = 0
    while i < len(new_list):
        sum = 0
        for letter in new_list[i]:
            if excluded_letter != letter:
                sum += 1
        if sum == 6:
            new_list.remove(new_list[i])
        else:
            i += 1
    return new_list


def remove_letter_from_list(excluded_letter):
    i = 0
    while i < len(new_list):
        sum = 0
        for letter in new_list[i]:
            if excluded_letter != letter:
                sum += 1
        if sum != 6:
            new_list.remove(new_list[i])
        else:
            i += 1
    return new_list

def procurar_palavra_na_lista(palavra):
    if palavra in new_list:
        print("Sim existe a palavra na lista")
    else:
        print("Não existe a palavra na lista")





def include_letter_from_list_by_position(include_letter, position):
    i = 0
    while i < len(new_list):
        a = new_list[i][position]
        if a != include_letter:
            new_list.remove(new_list[i])
        else:
            i += 1
    return new_list


def exclude_letter_from_list_by_position(exclude_letter, position):
    i = 0
    while i < len(new_list):
        a = new_list[i][position]
        if a == exclude_letter:
            new_list.remove(new_list[i])
        else:
            i += 1
    return new_list

def suggested_words():
    i = 0
    vowels = ["A", "E", "I", "O", "U"]
    suggested_words = []
    aux = 0
    while i < len(new_list):
        vowels_count = 0
        finded_vowels = []
        for letter in new_list[i]:
            if letter in vowels and letter not in finded_vowels:
                vowels_count += 1
                finded_vowels.append(letter)
        if vowels_count >= aux:
            aux = vowels_count
            suggested_words.append(new_list[i])
        i += 1
    return suggested_words

# TODO função que remove as letras que nao tem na palavra:
vetor = []
vetor2 = []
def funcao_remover_letras(vetor):
    nao_contem_as_letras = input(f"Quais letras não estão contidas na palavra?: ").upper()
    if nao_contem_as_letras != "PULAR":
        nao_contem_as_letras_lista = list(nao_contem_as_letras)
        vetor.append(nao_contem_as_letras)
        vetor = ''.join(vetor)
        print(f"A palavra não contem as seguintes letras: {vetor}")
        print(nao_contem_as_letras_lista)
        for char in nao_contem_as_letras_lista:
            remove_letter_from_list(char)

def funcao_incluir_letras(vetor2):
    nao_contem_as_letras = input(f"Quais letras estão contidas na palavra?: ").upper()
    if nao_contem_as_letras != "PULAR":
        nao_contem_as_letras_lista = list(nao_contem_as_letras)
        vetor2.append(nao_contem_as_letras)
        vetor2 = ''.join(vetor2)
        print(f"A palavra contem as seguintes letras: {vetor2}")
        print(nao_contem_as_letras_lista)
        for char in nao_contem_as_letras_lista:
            include_letter_from_list(char)

game_is_on = True
rodada = 1
while game_is_on:
    print(f">>>> {rodada}a RODADA <<<<\n")
    funcao_remover_letras(vetor)
    funcao_incluir_letras(vetor2)
    rodada += 1
    print(new_list)
    print(f"length new list: {len(new_list)}")
    print(f"Suggested words: {suggested_words()}")
    print(f"Length suggested words: {len(suggested_words())}")
    continuar = input("Continuar? S ou N: ").upper()
    print("\n")
    if continuar == 'N':
        game_is_on = False















#TODO UMA FUNÇÃO QUE SUGERE A MELHOR ESCOLHA