from midemo.my_module import SuperBasica


def test_SuperBasica():
    sb = SuperBasica()
    assert sb.suma(1, 2) == 3
    assert sb.resta(5, 3) == 2
    assert sb.multiplicacion(2, 3) == 6
