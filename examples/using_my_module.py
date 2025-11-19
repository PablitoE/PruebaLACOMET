from midemo.my_module import SuperBasica


def main():
    sb = SuperBasica()

    suma_result = sb.suma(1, 2)
    print(suma_result)
    resta_result = sb.resta(5, 3)
    print(resta_result)
    multiplicacion_result = sb.multiplicacion(2, 3)
    print(multiplicacion_result)


if __name__ == "__main__":
    main()
