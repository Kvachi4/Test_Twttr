def main():
    my_text = input("INPUT: ").upper()
    print("OUTPUT: ", shorten(my_text))

def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
        