
def capitalize(text):
    if (len(text) != 0):
        return text[0].upper() + text[1:].lower()
    else:
        return None

def upper(text):
    string = ''
    for char in txt:
        # Uppercase
        if (ord(char) >= 97 and ord(char) <= 122):
            string += chr(ord(char)-32) # Subtract 32 to make it uppercase
        else:
            string += char
    return string

def lower(text):
    string = ''
    for char in txt:
        # Uppercase
        if (ord(char) >= 65 and ord(char) <= 90):
            string += chr(ord(char)+32) # Add 32 to make it lowercase
        else:
            string += char
    return string

def isalpha(text):
    c = 0 
    for char in text:
        if((ord(char) >= 97 and ord(char)<=122) or (ord(char) >= 65 and ord(char) <=90)): # (97-122 : lowercase) | (65-90 : Uppercase)
            c += 1
    if(c == len(text)):
        return True
    else:
        return False
    
def isdigit(text):
    c = 0 
    for i in text:
        if(ord(i) >= 48 and ord(i)<= 57):
            c +=1
    if(len(text)==c):
        return True
    else:
        return False
    
def isalnum(text):
    c = 0 
    for i in text:
        if((ord(i) >= 48 and ord(i)<= 57) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >=65 and ord(i) <= 90)):
            c +=1
    if(len(text)==c):
        return True
    else:
        return False
    
def title(text):
    output = []
    for word in text.split(' '):
        if word:
            output.append(word[0].upper() + word[1:].lower() + ' ')
    return ' '.join(output)
