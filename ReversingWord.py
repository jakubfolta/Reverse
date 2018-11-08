def reversing_word(text):
  in_reverse = ''
  for letter in text:
    in_reverse = letter + in_reverse
  return in_reverse

print(reversing_word('babajaga'))
