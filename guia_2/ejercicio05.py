phrase = input("Ingresá una frase, terminala con un punto: \n")
words_with_ta = 0
if len(phrase) != 0 and phrase[-1] == ".":
    words = phrase.lower().split()
    letter_count = [len(x) for x in words]
    average_letter_count = sum(letter_count) / len(letter_count)
    for word in words:
        if word.startswith("ta"):
            words_with_ta += 1

    print("words", words)
    print("letter_count", letter_count)
    print("average_letter_count", average_letter_count)
    print("words_with_ta", words_with_ta)
