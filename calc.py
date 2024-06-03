def inicjacja():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    return a, b


def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    if b == 0:
        return ("Nie można dzielić przez 0!")
    else:
        return a / b


print("Witaj w prostym kalkulatorze!")
print("Oto jakie działania obsługujemy:")
print("================================")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Wyjście")
choice = int(input("Wpisz cyfrę swojego wyboru: "))
match choice:
    case 1:
        a,b = inicjacja()
        print("Twój wynik to: ", dodawanie(a, b))
    case 2:
        a,b = inicjacja()
        print("Twój wynik to: ", odejmowanie(a, b))
    case 3:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print("Twój wynik to: ", mnozenie(a, b))
    case 4:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print("Twój wynik to: ", dzielenie(a, b))
