'''
Substitution Cipher
CIS 210 F17 Project 4-1

Author: Lily Jim

Credits: Based on code on p.102, 106, and 107 Miller and Ranum text.

Encrypt then decrypt a plain text message using a substitution cipher
'''

import doctest

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

def genKeyFromPass(password):
    ''' (str) -> str
    Takes the password and removes duplicate characters.
    Then all the other lowercase letters of the English alphabet are added
    to the end, starting with the next letter of the alphabet after the
    last letter in the password. Returns a new string.
    Note: Password should not contain numbers, capitals, spaces, or special characters
    >>> genKeyFromPass('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'
    >>> genKeyFromPass('password')
    'paswordefghijklmnqtuvxyzbc'
    >>> genKeyFromPass('francis')
    'francistuvwxyzbdeghjklmopq'
    '''
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def substitutionEncrypt(plainText, psw):
    ''' (str, str) -> str
    Takes a password to create a key, then encrypts a given string with the key
    Returns the new encrypted string
    Note: plainText should not include numbers or special characters
    >>> substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'
    >>> substitutionEncrypt('deadpool is awesome', 'francis')
    'ncfndbbxuhfmchbyc'
    >>> substitutionEncrypt('ajax is really francis', 'deadpool')
    'drdiqbzodttjlzdvaqb'
    '''
    key = genKeyFromPass(psw)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    plainText = removeMatches(plainText, ' ')
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def substitutionDecrypt(cipherText, psw):
    ''' (str, str) -> str
    Takes a password to create the key to decrypt a string
    Returns the decrypted string -- which will not contain spaces or capitals
    Note: if the original string contained numbers or special characters
    they will appear as 'z' in the decrypted version
    >>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'
    >>> substitutionDecrypt('ncfndbbxuhfmchbyc', 'francis')
    'deadpoolisawesome'
    >>> substitutionDecrypt('drdiqbzodttjlzdvaqb', 'deadpool')
    'ajaxisreallyfrancis'
    '''
    key = genKeyFromPass(psw)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plainText = ''
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    
    return plainText

def main():
    ''' () -> None
    Calls substitutionEncrypt and substitutionDecrypt.
    Prints results and returns none
    '''
    print('What would you like to encrypt?')
    plainText = input()
    print('What is the password?')
    psw = input()
    print('')
    print('Encrypted version:')
    print(substitutionEncrypt(plainText, psw))
    cipherText = substitutionEncrypt(plainText, psw)
    print('')
    print('Decrypted version:')
    print(substitutionDecrypt(cipherText, psw))

    return None
    

print(doctest.testmod())
main()

