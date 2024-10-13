# 9.1.8.3 (egentlig 9.1.8.2 men dere har gjort feil)

def all_z_words(wordlist : list) -> list:
    """Lag en liste med string som har Z"""
    zlist = []
    for wd in wordlist:
        if "z" in wd: # Sjekk hvis z er i elementet.
            zlist = [wd] + zlist # Legg til elementet i listen.
    return(zlist)

def all_z_words_f(wordlist : list) -> list:
    ''' 
    For en liste, bruk filter med en lambda funksjon og en ordliste. 
    Funksjonen sjekker om z er i elementet, ellers returnerer den ingenting
    '''
    x = list(filter(lambda elt : elt if("z" in elt) else None, wordlist)) 
    return x

def test_all_z_words():
    assert all_z_words(["a", "b", "z"]) == ["z"]
    assert all_z_words(["a", "b", "bz"]) == ["bz"]
    assert all_z_words(["a", "b", "zzz"]) == ["zzz"]

def test_all_z_words_f():
    assert all_z_words_f(["a", "b", "fz"]) == ["fz"]
    
# Gir assertion error dersom en av dem er feil.
test_all_z_words() 
test_all_z_words_f() 
