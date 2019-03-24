def print_reverse(text):
    reverse_word = ''
    for x in text:
        reverse_word = x + reverse_word
    return reverse_word

print(print_reverse('fsdfrvwaaa'))
