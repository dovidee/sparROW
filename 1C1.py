def moonie(earthie : int) -> int:
    new = earthie * 1/6 
    return new
def test_moonie():
    assert round(moonie(100)) == 17 # Endre 17, få error
test_moonie()
