def reverse(text):
    text = text.split('_')
    print(text)
    new_word = ''
    for item in text:
        for x in range(1, len(item) + 1):
            new_word += item[len(item) - x]
        if text.index(item) == len(text) - 1:
            break
        new_word += '_'
    return new_word


print(reverse('hello_world'))
