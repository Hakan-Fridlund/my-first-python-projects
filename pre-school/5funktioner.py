# Tar två tal och en operator (+, -, *, /) och returnerar resultatet.
def calculator(num1, num2, operator):
    num1, num2 = int(num1), int(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Fel, du kan inte dividera med 0"
        else:
            return num1 / num2
    else:
        return "Fel räknesätt"


# räkna vokaler i en sträng, Perfekt för loopar och stränghantering, Returnerar hur många vokaler som finns i texten.
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiouåäö":
            count += 1
    return count


# temperaturkonvertering Konverterar mellan Celsius ↔ Fahrenheit.
def convert_temperature(value, unit):
    value = float(value)
    if unit.lower() == "c":
        return f"{(value * 1.8 + 32)} Fahrenheit"
    elif unit.lower() == "f":
        return f"{((value -32) / 1.8 )} Celsius"
    else:
        return "Okänd skala"


# statistik om en text, Returnerar antal ord, längsta ordet, kortaste ordet + antal tecken
def text_statistics(text):
    words_number = len(text.split())
    longest_word = ""
    shortest_word = None
    characters = 0
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word
        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word
    for char in text:
        if char != " ":
            characters += 1

    return (words_number, longest_word, shortest_word, characters)


# filtrera tal Tar en lista och returnerar alla tal som är större än ett visst gränsvärde.
# märklig sak att sorted i return sorterar 1000 före 101
def greater_than_100(numbers):
    lista = []
    for number in numbers:
        number = int(number)
        if number > 100:
            lista.append(number)
    return sorted(lista)


def meny():
    while True:
        print("1. Miniräknare")
        print("2. Vokalräknare")
        print("3. Temperaturkonverterare")
        print("4. Text-statistik")
        print("5. Är mitt tal över 100")
        print("6. Avsluta")
        val = input("Välj: ")
        if val == "1":
            num1 = input("Skriv ett tal: ")
            operator = input("Skriv ett räknesätt +-*/: ")
            num2 = input("Skriv ett tal: ")
            print(f"\nSvaret är: {calculator(num1, num2, operator)}\n")
        elif val == "2":
            text = input("Skriv en hel text: ")
            print(f"Det är {count_vowels(text)} vokaler i texten\n")
        elif val == "3":
            value = input("Hur många grader är det?: ")
            unit = input("Vilken skala är det? (C eller F):")
            print(f"\nDet motsvarar: {convert_temperature(value, unit)}\n")
        # unpacking listan som kommit i retur för att separera dom fyra olika svaren
        elif val == "4":
            text = input("Skriv en hel text: ")
            stats = text_statistics(text)
            words, longest, shortest, chars = stats
            print(
                f"\nAntal ord: {words}\nLängsta ordet är: {longest}\nKortaste ordet är: {shortest}\nAntal bokstäver: {chars}\n"
            )
        elif val == "5":
            numbers = input("Skriv flera tal, separerade med mellanslag: ").split()
            print(f"\nDessa tal är över 100: {greater_than_100(numbers)}\n")
        elif val == "6":
            break
        else:
            print("\ninvalid input\n")


def main():
    meny()


main()
