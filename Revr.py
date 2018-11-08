def revr(text):
  nword = ''
  for letter in text:
    nword = letter + nword
  return nword

print(revr('abecadlower'))
