def enumerate_list(lista):
    enumerated_list = []
    index = 0 
    
    for value in lista:
        if value != "":
            enumerated_list.append(f"{index}. {value}")
            index += 1 
    
    return enumerated_list



def enumerate_backwards(lista):
    enumerated_backwards_list = []
    
    for i, value in enumerate(lista):
        if value != "":
            enumerated_backwards_list.append(f"{i}. {value[::-1]}")
    
    return enumerated_backwards_list
   

