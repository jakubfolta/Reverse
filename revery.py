def reverse(text):
  revword = ''
  for letter in text:
    revword = letter + revword
  return revword

print(reverse('abecedefegtyoi'))


def reverse(text):
  revword = ''
  for letter in range(1, len(text) + 1):
    revword += text[len(text) - letter]
  return revword

print(reverse('kdhteuiofgo'))
