'''
Substitution Cipher
CIS 210 F17 Project 4-1

Author: Lily Jim

Credits: Based on code on p.102, 106, and 107 Miller and Ranum text.

Encrypt then decrypt a plain text message using a substitution cipher
'''

def removeDupes(myString):
    ''' (str) -> str
    Returns a string that has removed all duplicate
    characters from the original string
    >>> removeDupes('hello world')
    'helo wrd'
    >>> removeDupes('password')
    'pasword'
    >>> removeDupes('the quick brown fox')
    'the quickbrownfx'
    '''
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def removeMatches(myString, removeString):
    ''' (str, str) -> str
    Removes all characters that are present in removeString
    from myString. Returns a new string
    >>> removeMatches('the quick brown fox', ' ')
    'thequickbrownfox'
    >>> removeMatches('hello world', 'l')
    'heo word'
    >>> removeMatches('password', 'pas')
    'word'
    '''
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def removeSpecialCharacters(myString):
    '''(str) -> str
    Removes numbers and special characters from the given string
    returning a new string containing only spaces and letters
    from the English alphabet
    >>> removeSpecialCharacters('#The *quick* /brown/ Fox!')
    'The quick brown Fox'
    >>> removeSpecialCharacters('#My Password 123')
    'My Password '
    >>> removeSpecialCharacters('Is it @Ajax or @Francis?')
    'Is it Ajax or Francis'
    '''
    newstr = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
    for ch in myString:
        if ch in alphabet:
            newstr = newstr + ch
    return newstr

def genKeyFromPass(password):
    ''' (str) -> str
    Takes the password and removes all special characters, numbers,
    spaces, and duplicate characters, and changes any capitals to lowercase.
    Then all the other lowercase letters of the English alphabet are added
    to the end, starting with the next letter of the alphabet after the
    last letter in the password. Returns a new string
    >>> genKeyFromPass('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'
    >>> genKeyFromPass('#Ajax123')
    'ajxyzbcdefghiklmnopqrstuvw'
    >>> genKeyFromPass('My Password')
    'mypaswordefghijklnqtuvxzbc'
    '''
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeSpecialCharacters(password) #remove non-letters
    password = removeMatches(password, ' ') #remove spaces
    password = password.lower() #change any capitals to lowercase
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def substitutionEncrypt(plainText, psw):
    ''' (str) -> str
    TODO
    >>> substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'
    >>> substitutionEncrypt('#2017 @Ajax is really @Francis', '#MyPassword123')
    'memzdqnsmggbwnmipdq'
    >>> substitutionEncrypt('ajax is really francis', 'mypassword')
    'memzdqnsmggbwnmipdq'
    >>> substitutionEncrypt('a simple phrase', 'easy')
    'epfjmizmdoepz'
    '''
    key = genKeyFromPass(psw)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower() #change capitals to lowercase
    plainText = removeMatches(plainText, ' ') #remove spaces
    plainText = removeSpecialCharacters(plainText) #remove special characters and numbers
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def substitutionDecrypt(cipherText, psw):
    ''' (str, str) -> str
    TODO
    >>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'
    >>> substitutionDecrypt('memzdqnsmggbwnmipdq', '#MyPassword123')
    'ajaxisreallyfrancis'
    >>> substitutionDecrypt('epfjmizmdoepz', 'easy')
    'asimplephrase'
    '''
    key = genKeyFromPass(psw)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plainText = ''
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    
    return plainText

def main():
    ''' (TODO) -> TODO
    TODO
    >>> TODO
    TODO
    >>> TODO
    TODO
    >>> TODO
    TODO
    '''
    #TODO Combine substitutionEncrypt and substitutionDecrypt
    print('What would you like to encrypt?')
    plainText = input()
    print('What is the password?')
    psw = input()
    print('Encrypted version:')
    print(substitutionEncrypt(plainText, psw))
    cipherText = substitutionEncrypt(plainText, psw)
    print('Decrypted version:')
    print(substitutionDecrypt(cipherText, psw))

    return None
    

#TODO doctest.testmod()
