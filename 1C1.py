def num_to_str(liste : list) -> list:
    ''' Ta en liste og lag tallene over til string i en ny liste'''
    empty = []
    for element in liste:
        fixed = round(element)
        if fixed == 0: # Hvis element er null, null
            empty.append("zero") 
        elif fixed > 0: # Hvis element er bedre enn 0, positiv
            empty.append("pos")
        elif fixed < 0: # Hvis element er større enn 0, negativ
            empty.append("neg")
    return empty

test1 = num_to_str([1])
test2 = num_to_str([0])
test3 = num_to_str([-1])

print(num_to_str([-1, 0, 1, -0.4])) # ['neg', 'zero', 'pos', 'zero']

def find_str_len(liste : list) -> list:
    ''' Ta en liste og sjekk hvis den har tallet 5 '''
    for element in liste:
        if len(element) == 5: # Sjekk hvis lengden av elementet er lik 5
            return True
        else:
            pass

print(find_str_len(["a", "bb", "ccccc"])) # True

def even_num(liste : list) -> list:
    ''' Finn partal av en liste mellom 10 og 20 og lag ny liste'''
    empty = []
    for element in liste:
        if 10 <= element <= 20: # Interval comparison
            if element % 2 == 0: # Hvis remainder har 1, er den odd. Hvis 0, er den even.
                empty.append(element) # Legg til i den tomme listen vår. 
    return empty

print(even_num([5, 10, 12, 16, 20, 22, 24])) # [10, 12, 16, 20]
