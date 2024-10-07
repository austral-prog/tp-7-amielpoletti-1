def enumerate_list(lista):
    enumerated_list = []
    
    for i, value in enumerate(lista):
        if value != "":
            enumerated_list.append(f"{i}. {value}")
    return enumerated_list


def enumerate_backwards(lista):
    enumerated_backwards_list = []
    
    for i, value in enumerate(lst):
        if value != "":
            enumerated_backwards_list.append(f"{i}. {value[::-1]}")
    
    return enumerated_backwards_list


