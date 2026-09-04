# input two numbers and an operator +,-,*,/ and returns the result
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
            return "Error, not divisible by 0"
        else:
            return num1 / num2
    else:
        return "Wrong operator"


# returns vowels count from a string
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiouåäö":
            count += 1
    return count


# converts temperature between celsius and fahrenheit
def convert_temperature(value, unit):
    value = float(value)
    if unit.lower() == "c":
        return f"{(value * 1.8 + 32)} Fahrenheit"
    elif unit.lower() == "f":
        return f"{((value -32) / 1.8 )} Celsius"
    else:
        return "Unknown scale"


# statistics about a text. Returns number of words, longest, shortest and number of signs
def text_statistics(text):
    words_number = len(text.split())
    longest_word = ""
    shortest_word = None
    characters = 0
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word
        # noinspection PyTypeChecker
        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word
    for char in text:
        if char != " ":
            characters += 1

    return words_number, longest_word, shortest_word, characters



#filters numbers in a list, returns numbers greater than 100 in a sorted list
def greater_than_100(numbers):
    lista = []
    for number in numbers:
        number = int(number)
        if number > 100:
            lista.append(number)
    return sorted(lista)


def meny():
    while True:
        print("1. Calculator")
        print("2. Vowelcounter")
        print("3. Temperatureconverter")
        print("4. Text-statistics")
        print("5. Is my number greater than 100?")
        print("6. Exit")
        val = input("Choose: ")
        if val == "1":
            num1 = input("Write a number: ")
            operator = input("Write an operator: +-*/: ")
            num2 = input("Write a number: ")
            print(f"\nThe answer is: {calculator(num1, num2, operator)}\n")
        elif val == "2":
            text = input("Write a text: ")
            print(f"Is is {count_vowels(text)} vowels in the text\n")
        elif val == "3":
            value = input("How many degrees is it?: ")
            unit = input("Which scale do you use? (C or F):")
            print(f"\nThat corresponds to: {convert_temperature(value, unit)}\n")

        elif val == "4":
            text = input("Write a text: ")
            stats = text_statistics(text)
            words, longest, shortest, chars = stats
            print(
                f"\nNumber of words is: {words}\nThe longest word is: {longest}\nThe shortest word is: {shortest}\n"
                f"Number of letters in the text: {chars}\n"
            )
        elif val == "5":
            numbers = input("Write several numbers, separated with a space: ").split()
            print(f"\nThese numbers are greater than 100: {greater_than_100(numbers)}\n")
        elif val == "6":
            break
        else:
            print("\ninvalid input\n")


def main():
    meny()


main()
