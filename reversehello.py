sentence = 'hello_cruel_world!!!'

# echo "hello_cruel_world" | tr _ \\n | rev | tr \\n _


def reverse(text):
    text = text.split('_')
    new_word = ''
    for item in text:
        for x in range(1, len(item) + 1):
            new_word += item[len(item) - x]
            print (new_word)
        if text.index(item) == len(text) - 1:
            print ('break')
            break
        new_word += '_'
    return new_word

print(reverse(sentence))


def rev(text):
    words = text.split('_')

    for i in range(0,len(words)):
        word = words[i]
        for x in range(0, int(len(word)/2)):
            chars = list(word)
            char1 = chars[x]
            char2 = chars[len(word)-1-x]
            chars[x] = char2
            chars[len(word)-1-x] = char1
            print(word + ' => ' + "".join(chars))
            words[i] = "".join(chars)

    return ('_'.join(words))

print (rev(sentence))
