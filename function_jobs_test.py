from function_jobs import osszaadas


def test_osszaadas(): #függvény teszteset
    result = osszaadas(2, 3)# tesztelendő függvény meghívása
    assert result == 5

def test_osszaadas2(): #függvény teszteset
    result = osszaadas(0, 0)# tesztelendő függvény meghívása
    assert result == 0


def test_osszaadas3(): #függvény teszteset
    result = osszaadas(-5, -6)# tesztelendő függvény meghívása
    assert result == -11
