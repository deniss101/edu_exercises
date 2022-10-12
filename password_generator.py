from random import sample

DIGITS = '0123456789'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''
count = int(input('Количество паролей для генерации: '))
lenght = int(input('Длина пароля: '))

nums = input('Использовать цифры? ')
upper = input('Использовать прописные буквы? ')
lower = input('Использовать строчные буквы? ')
symbols = input('Использовать символы? ')
remove_sym = input('Исключить символы i/l/0 ? ')

symbols_set = ['да', 'д', '1', 'yes', 'y']
if nums in symbols_set:
    chars += DIGITS
    if lenght > 10:
        chars += DIGITS * (lenght // 9)
if upper in symbols_set:
    chars += UPPERCASE_LETTERS
if lower in symbols_set:
    chars += LOWERCASE_LETTERS
if symbols in symbols_set:
    chars += PUNCTUATION
if remove_sym in symbols_set:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(lenght, chars):
    return sample(chars, lenght)


for i in range(count):
    print(''.join(generate_password(lenght, chars)))
