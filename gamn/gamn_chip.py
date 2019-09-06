#!/usr/bin/python3
# -*- coding: utf-8 -*-

def gamNCrypt(mode, key, msg):
    # --- круговое перемещение ключа ---
    cmsg, lmsg, lspce = [], [], []
    for i in range(len(msg)):
        if ' ' in msg[i]:
            lspce.append(i)
        else:
            lmsg.append(msg[i]) # убираем пробелы
    lkey = list(key)
    rkey = []
    for i in range(len(lmsg)):
        rkey.append(lkey[i % len(lkey)])
    # --- код зашифрованного символа ---
    for i in range(len(lmsg)):
        if mode == 1:
            ccd = ((ord(lmsg[i]) + ord(rkey[i]) - 2 * ord('а')) % 32) + ord('а')
        if mode == 2:
            ccd = ((ord(lmsg[i]) - ord(rkey[i]) - 2 * ord('а')) % 32) + ord('а')
        cmsg.append(chr(ccd))
    for ind in lspce:
        cmsg.insert(ind, ' ') # возвращаем пробелы
    return ''.join(cmsg) # путевки до неба - ьугчбчи ха мтбс
