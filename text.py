#Övning: läs textfil → räkna ord.

def count(file):
    count = 0
    with open(file, "r") as f:
        text = (f.read())
        print(text)
        for word in text.split():
            count += 1

        print(f"Denna texten innehåller: {count} ord")


def main():
    count("text.txt")


main()