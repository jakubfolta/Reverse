def reversee(letters):
  word = ''
  for char in letters:
    word = char + word
  return word

print(reversee('abesedefegh'))
