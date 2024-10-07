def index_of_by_index(word, lista, index):
    for i, value in enumerate(lista[index:], start=index):
        if value == word:
            return i
    return -1

def index_of_empty(lista):
    for i, value in enumerate(lista):
        if value == "":
            return i
    return -1


def index_of(word, lista):
    for i, value in enumerate(lista):
        if value == word:
            return i
    return -1

def put(word, lista):
    for i, value in enumerate(lista):
        if value == "":
            lista[i] = word
            return i
    return -1

def remove(word, lista):
    count = 0
    for i, value in enumerate(lista):
        if value == word:
            lista[i] = ""
            count += 1
    return count
