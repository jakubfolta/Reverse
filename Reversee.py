def reversee(letters):
  word = ''
  for char in letters:
    word = char + word
  return word

print(reversee('abesedefegh'))


def printInReverse(text):
  revword = ''
  for x in range(1, len(text) + 1):
    revword += text[len(text) - x]
  return revword

print(printInReverse('kdhteuiofgo'))