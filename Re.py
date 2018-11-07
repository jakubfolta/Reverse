def reverse(text):
  newword = ''
  for letter in range(1, len(text) + 1):
    newword += text[len(text) - letter]
  return newword

print(reverse('konstantyn'))
