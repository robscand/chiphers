#!/usr/bin/python3
# -*- coding: utf-8 -*-

import des.tabs as tab

# обновление словарей
def upDict(d, key, val):
    d[key] = val


# преобразование сообщения и ключа в битовое представление
def textToBits(text, encoding='utf-8', errors='surrogatepass'):
    # для текста в кодировке Unicode получаем последовательность битов
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    # в каждом байте должно быть 8 бит, если нет битов, чтобы собрать байт, добавляем 0-биты в начало последовательности
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# преобразование битового представления в сообщение
def bitsToText(bits, encoding='utf-8', errors='surrogatepass'):
    # делаем из последовательности число, путем ее перевода из двоичной в десятичную систему счисления
    n = int(bits, 2)
    # (n.bit_length() + 7) // 8 - вместе биты должны образовывать определенное количество байтов, в зависимости от кодировки и длины сообщения
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


# Генерация ключа
def keyGen(key_round, text):
    if key_round == 0:
        key_bit = textToBits(text)
        # Начальная перестановка
        keyG = ''
        for ind in tab.prepG:
            keyG += key_bit[ind - 1]  # ind - 1, т.к. индексация идет с 0

        # Преобразование ключа разбивается на два 28-битовых блока
        global halfC  # --------- nonlocal
        global halfD  # --------- nonlocal
        halfC = keyG[0:28]
        halfD = keyG[28:56]
    # Циклический сдвиг ключа влево в зависимости от итерации
    # выделение с 2 до конца + выделение с начала до 2
    halfC = halfC[tab.vshift[key_round]:] + halfC[:tab.vshift[key_round]]
    halfD = halfD[tab.vshift[key_round]:] + halfD[:tab.vshift[key_round]]
    # print(halfC, halfD, sep=' | ')
    # Объединение частей ключа
    union_key = halfC + halfD
    # Завершающее преобразование ключа
    fin_key = ''
    for ind in tab.endH:
        fin_key += union_key[ind - 1]  # ind - 1, т.к. индексация идет с 0
    return fin_key


def roundDES(bit, fin_key):
    # Используем расширение для правого полублока начальной перестановки
    extend_bit = ''
    for ind in tab.extendE:
        extend_bit += bit[ind - 1]  # ind - 1, т.к. индексация идет с 0

    # К расширенному перечислению и сгенерированному ключу применяем операцию XOR
    crypt_bit = ''
    for i in range(len(extend_bit)):
        crypt_bit += str(int(extend_bit[i]) ^ int(fin_key[i]))

    # Разбиваем закодированное перечисление на блоки
    block_size = 6
    count_blocks = 8
    # Колучаем восемь шестибитовых блоков. 6-битовый блок B(j) = b1b2b3b4b5b6
    # i*block_size - cмещение по размеру блока
    blocks = [crypt_bit[i * block_size:(i * block_size) + block_size] for i in range(count_blocks)]

    # Количество строк в одной функции преобразования
    cbits = ''
    row_in_s = 4
    # Применяем к каждому блоку функцию преобразования
    for i in range(count_blocks):
        # Двухбитовое число b1b6 - номер строки функции
        row = int(blocks[i][0] + blocks[i][5], 2)
        # Число b2b3b4b5 - номер столбца функции
        col = int(blocks[i][1:5], 2)
        # В столбце col строки row задано значение sval
        # i*(row_in_s) - смещение по строкам функции преобразования
        sval = tab.sm[row + i * (row_in_s)][col]
        # Переводим значение в двоичный формат и записываем в результирующую переменную
        bits = bin(sval)[2:]
        # Длина одного s-блока - 4 бита
        if len(bits) < 4: bits = '0' * (4 - len(bits)) + bits
        cbits += bits
    # print(cbits, len(cbits))
    # Применение функции перестановки
    reverse_cbits = ''
    for ind in tab.reverseP:
        reverse_cbits += cbits[ind - 1]  # ind - 1, т.к. индексация идет с 0
    return reverse_cbits

# Кодирование сообщения
def encodeDES(inp_text, key_text):
    count_rounds = 16 # Количество раундов преобразования
    keys_dct = {} # Словарь ключей
    # Проходим раунды
    for text_round in range(count_rounds):
        if text_round == 0:
            # Начальная перестановка
            text_bit = textToBits(inp_text)
            textIP = ''
            for ind in tab.startIP:
                textIP += text_bit[ind - 1] # ind - 1, т.к. индексация идет с 0
            # разделяем последовательность полам на левую последовательность и правую последовательность
            left_bit = textIP[0:32]
            right_bit = textIP[32:64]
        # Генерация ключа раунда
        key_bits = keyGen(text_round, key_text)
        # Сохраняем ключ раунда в словаре
        upDict(keys_dct, text_round, key_bits)
        # Используем функцию шифрования
        сrypt_bits = roundDES(right_bit, key_bits)
        # К левому полублоку и результату функции шифрования применяем операцию XOR
        right_bit_new = ''
        for i in range(len(left_bit)):
            right_bit_new += str(int(left_bit[i]) ^ int(сrypt_bits[i]))
        # Осуществляем перестановку полублоков для следующего раунда
        left_bit = right_bit
        right_bit = right_bit_new
    # Объединяем получившиеся полублоки, сначала правый R(16), потом левый L(16)
    union_text = right_bit + left_bit
    # Применяем конечную функцию перестановки
    fin_text = ''
    for ind in tab.endIP:
        fin_text += union_text[ind - 1] # ind - 1, т.к. индексация идет с 0
    return textIP, fin_text, keys_dct

# Декодирование сообщения
def decodeDES(inp_text, keys_dct):
    count_rounds = 16 # Количество раундов преобразования
    rkeys_dct = {} # Перевернутый словарь ключей
    # Процесс декодирования осуществляется в обратном порядке
    # Меняем все местами, кроме функции шифрования, IP и IP-1, ключ берем из словаря
    # Проходим раунды
    for text_round in range(count_rounds):
        if text_round == 0:
            # Начальная перестановка
            textIP = ''
            for ind in tab.startIP:
                textIP += inp_text[ind - 1] # ind - 1, т.к. индексация идет с 0
            # разделяем последовательность полам на левую последовательность и правую последовательность
            # теперь левый полублок станет правым, а правый - левым
            right_bit = textIP[0:32]
            left_bit = textIP[32:64]
            # Сохраняем левый и правый полублок начальной перестановки в словаре
        # Подгружаем сохраненный ключ при кодировании. Загрузка начинается с последнего ключа
        key_bits = keys_dct[count_rounds - text_round - 1]
        # Сохраняем ключ раунда в словаре
        upDict(rkeys_dct, text_round, key_bits)
        # Используем функцию шифрования, только уже с левым ключом
        сrypt_bits = roundDES(left_bit, key_bits)
        # К левому полублоку и результату функции шифрования применяем операцию XOR
        left_bit_new = ''
        for i in range(len(right_bit)):
            left_bit_new += str(int(right_bit[i]) ^ int(сrypt_bits[i]))
        # Осуществляем перестановку полублоков для следующего раунда
        right_bit = left_bit
        left_bit = left_bit_new
    # Объединяем получившиеся полублоки, сначала левый L(0), потом правый R(0)
    union_text = left_bit + right_bit
    # Применяем конечную функцию перестановки
    fin_text = ''
    for ind in tab.endIP:
        fin_text += union_text[ind - 1] # ind - 1, т.к. индексация идет с 0
    return textIP, fin_text, bitsToText(fin_text), rkeys_dct

# Конвертирование из одной системы счисления в другую
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
