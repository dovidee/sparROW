building_B = {'B1007': 500,
     'B1006': 400,
     'B1005': 49}

def room_size(selection : str, building : dict) -> dict:
    ''' Ta et valg i et rom og et bygg og se hvor mange rom den har '''
    for element in building:
        if element == selection: # Hvis elementet er lik valget, så kan den vises til bruker
            print(building[element])

room_size("B1007", building_B) # 500

def change_size(selection : str, building : dict, free : int, add : bool) -> dict:
    ''' 
    Ta et valg i et rom og et bygg, velg deretter hvor mange seter, og om du vil legge til/fjerne
    '''
    for element in building:
        if element == selection:
            if add == True: # Hvis den er true, vil den legge til.
                building[element] += free
            elif add == False: # Hvis den er false, vil den fjerne.
                building[element] -= free
    print(building)

change_size("B1007", building_B, 10, True) # {'B1007': 510, 'B1006': 400, 'B1005': 49}

def min_size() -> dict:
    ''' Filtrer alle rom som har mindre enn 50 seter '''
    for key, value in list(building_B.items()):
        if value < 50: 
            del building_B[key] # Fjern rommet fra bygningen i listen
    print(building_B)

min_size() # {'B1007': 510, 'B1006': 400}
