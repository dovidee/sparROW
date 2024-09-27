def my_str_len(l):
    for i in l:
        return len(i)

def test_my_str_len():
    assert my_str_len(["abc"]) == 3

test_my_str_len() # Error om assert value blir endret

def my_num_max(l):
    return max(l)
        
def test_my_num_max():
    assert my_num_max([1, 2, 3]) == 3

test_my_num_max() # Error om assert value blir endret
