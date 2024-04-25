def str_lst(str):
    return list(str)

codes = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'A"+'SDFGHJKL:"'+"zxcvbnm,./ZXCVCBNM<>? "
codes = str_lst(codes)

def elongate(str, length):
    orstr = str
    while len(str) < length:
        str += orstr
    return str

def totext(text):
    final = str()
    for letter in text:
        letter = chr(letter)
        final += letter
    return final

def unnum(text):
    final = str()
    for item in text:
        final += codes[item]
    return final

def num(str):
    final = list()
    for item in str:
        num = 0
        for code in codes:
            if code == item:
                final.append(num)
            num += 1
    return final

def num_encrypt(str):
    final = list()
    for item in str:
        final.append(ord(item))
    return final

def encrypt(text, key):
    key = elongate(key, len(text))
    text = str_lst(text)
    key = str_lst(key)
    text = num(text)
    key = num(key)
    i = 0
    while i < len(text):
        text[i] = text[i] + key[i]
        i += 1
    text = totext(text)
    return text

def decrypt(text, key):
    key = elongate(key, len(text))
    text = str_lst(text)
    key = str_lst(key)
    text = num_encrypt(text)
    key = num(key)
    i = 0
    while i < len(text):
        text[i] = text[i] - key[i]
        i += 1
    text = unnum(text)
    return text
    
print(encrypt("hello darkness my old friend... I've come to see you again...", "hi"))
print(decrypt(encrypt("hello darkness my old friend... I've come to see you again...", "hi"), "hi"))