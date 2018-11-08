def rev(word):
  revword = ''
  for char in range(1, len(word) + 1):
    revword += word[len(word) - char]
  return revword

print(rev('abecadlo'))
