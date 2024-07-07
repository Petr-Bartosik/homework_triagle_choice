def print_shape(choice, size):
    if choice == 'a':
        for i in range(size):
            for j in range(size):
                if i <= j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'b':
        for i in range(size):
            for j in range(size):
                if i <= j:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()
    elif choice == 'c':
        for i in range(size):
            for j in range(size):
                if j >= i and j < size - i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'd':
        for i in range(size):
            for j in range(size):
                if i >= size // 2 and j >= size // 2 - (i - size // 2) and j <= size // 2 + (i - size // 2):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'e':
        for i in range(size):
            for j in range(size):
                if (i >= j and i + j >= size - 1) or (i <= j and i + j <= size - 1):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'f':
        for i in range(size):
            for j in range(size):
                if (i <= j and i + j >= size - 1) or (i >= j and i + j <= size - 1):
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'g':
        for i in range(size):
            for j in range(size):
                if j <= i < size - j:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'h':
        for i in range(size):
            for j in range(size):
                if j >= i > size - j - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'i':
        for i in range(size):
            for j in range(size):
                if j < size - i:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    elif choice == 'j':
        for i in range(size):
            for j in range(size):
                if i + j >= size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    else:
        print("Chybně zadáno.")

def main():
    while True:
        print("Vyberte (a-j) nebo zadejte 'k' pro ukončení:")
        choice = input("Zadejte volbu: ").lower()
        
        if choice == 'k':
            break
        
        size = int(input("Zadejte velikost (min 5): "))
        
        print_shape(choice, size)
        print()
#tohle jsem si musel overit a moc tomu nerozumim.. mozna kdybysme si tohle
#volani vysvetlili na hodine? Je to vsak nejspis jedine reseni pro volani
#casti skriptu jako hlavni. 
if __name__ == "__main__":
    main()

