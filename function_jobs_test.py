from function_jobs import osszaadas, mennyi_space, count_params


def test_osszaadas(): #függvény teszteset
    result = osszaadas(2, 3)# tesztelendő függvény meghívása
    assert result == 5

def test_osszaadas2(): #függvény teszteset
    result = osszaadas(0, 0)# tesztelendő függvény meghívása
    assert result == 0


def test_osszaadas3(): #függvény teszteset
    result = osszaadas(-5, -6)# tesztelendő függvény meghívása
    assert result == -11

def test_mennyi_space():
       assert mennyi_space("an ya") == 1

def test_count_params():
    result = count_params("almakorte")
    assert result == 4