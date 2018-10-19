def reverse(text): #function which will return entered characters in reverse
  word = '' #variable which will contain characters in reverse
  for char in range(1,len(text) + 1): #loop by every character starting from "1" so "char" is starting from number "1" as well and can be used in next line as number "1" and not "0" what would cause an error(string index out of range)
    word += text[len(text) - char] #add every character to variable in reverse
  return word 
 
print (reverse('fs&5!?'))


