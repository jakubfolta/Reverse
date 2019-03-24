def print_reverse(text):
    reverse_word = ''
    for x in text:
        reverse_word = x + reverse_word
    return reverse_word

print(print_reverse('fsdfrvwaaa'))


def print_reverse(text):
    rev_word = ''
    for x in range(1, len(text) + 1):
        rev_word += text[len(text) - x]
    return rev_word

print(print_reverse('abecadlo'))
