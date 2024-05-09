def replace_word():
    str =input("Enter the string")
    word_to_replace = input("Enter the word to replace: ")
    word = input("Enter the word replacement: ")
    str = str.replace(word_to_replace, word)
    print(str)


replace_word()
