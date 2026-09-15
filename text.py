"""
assignment read textfile -> count the words
"""

def count(file):
    count = 0
    with open(file, "r") as f:
        text = (f.read())
        print(text)
        for word in text.split():
            count += 1

        print(f"This text contain: {count} words")


def main():
    count("text.txt")


main()