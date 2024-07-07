def print_frame(size):
    print('+' + '-' * size + '+')

def print_shape(choice, size):
    if choice == 'a':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if i <= j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'b':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if i <= j:
                    print(' ', end='')
                else:
                    print('*', end='')
            print('|')
    elif choice == 'c':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if j >= i and j < size - i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'd':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if i >= size // 2 and j >= size // 2 - (i - size // 2) and j <= size // 2 + (i - size // 2):
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'e':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if (i >= j and i + j >= size - 1) or (i <= j and i + j <= size - 1):
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'f':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if (i <= j and i + j >= size - 1) or (i >= j and i + j <= size - 1):
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'g':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if j <= i < size - j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'h':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if j >= i > size - j - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'i':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if j < size - i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    elif choice == 'j':
        for i in range(size):
            print('|', end='')
            for j in range(size):
                if i + j >= size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print('|')
    else:
        print("Chybně zadáno.")
    print_frame(size)

def main():
    print("""
Vítejte v programu pro kreslení tvarů!
Můžete si vybrat z následujících možností:

    +---+ +---+ +---+ +---+ +---+
    |\\  | |  /| |\\  /| |\\/\\| |/\\ |
    | \\ | | / | | \\/ | |/  \\| |  \\|
    |  \\| |/  | |    | |    | |   \\
    +---+ +---+ +---+ +---+ +---+
      a     b     c     d     e

    +---+ +---+ +---+ +---+ +---+
    |/\\ | |\\   | |  /| |  \\ | |   \\
    |  \\| | \\  | | / | |   \\| |    \\
    |   \\| |  \\| |/  | |    | |     \\
    +---+ +---+ +---+ +---+ +---+
      f     g     h     i     j


    """)
    while True:
        print("Vyberte tvar (a-j) nebo zadejte 'k' pro ukončení:")
        choice = input("Zadejte volbu: ").lower()
        
        if choice == 'k':
            print("")
            break
        
        if choice not in 'abcdefghij':
            print("Chyba.")
            continue
        
        try:
            size = int(input("Zadejte velikost (min 5): "))
            if size < 5:
                print("Velikost musí být alespoň 5!")
                continue
        except ValueError:
            print("Chyba.")
            continue
        
        print_frame(size)
        print_shape(choice, size)
        print()

if __name__ == "__main__":
    main()

