def replace_word():
    str = "Hello Everybody, this is me. hi hi hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    word = input("Enter the word replacement: ")
    str = str.replace(word_to_replace, word)
    print(str)


replace_word()
