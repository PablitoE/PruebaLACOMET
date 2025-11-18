from modules.my_module import SuperBasica


def main():
    sb = SuperBasica()

    return sb.suma(1, 2), sb.resta(4, 2), sb.multiplicacion(2, 3)    # 3, 2 , 6


if __name__ == "__main__":
    main()
