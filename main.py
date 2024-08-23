# Dice sum probability calculator
# Författare: Ludwig Metelius
# Datum:  2024-08-22

def main():
    N, M = input("").split()

    lista = []
    dictionary = {}

    for n in range (1, int(N)+1):
        for m in range (1, int(M)+1):
            lista.append(n+m)

    for u in range(0, 40):
        dictionary[u] = int(lista.count(u))

    maxvalue = max(dictionary.values())

    for i, o in dictionary.items():
        if o == maxvalue:
            print(i)
        

if __name__ == "__main__":
    main()