#!/usr/bin/python3
# -*- coding: utf-8 -*-

def cezCrypt(mode, shift, message):
    cryptMessage = ''
    for ind in range(len(message)):
        letter = message[ind]
        code = ord(letter)
        if mode == 1:
            # Шифрование символа по его ASCII в пределах русского алфавита
            cryptCode = ((code + shift - ord('а')) % 32) + ord('а')
        if mode == 2:
            # Дешифрование символа по его ASCII в пределах русского алфавита
            cryptCode = ((code - shift - ord('а')) % 32) + ord('а')
        cryptMessage += chr(cryptCode)
    return cryptMessage
