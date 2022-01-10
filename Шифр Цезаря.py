print("Введите слово для шифрования")
message = input("Слово: ")

print("Введите шаг шифрования")
step = int(input("Шаг: "))

answer = ""

for i in message:
    dec = ord(i) + step
    if ord(i) == 32:
        dec = 32
    elif dec>122:
       dec = dec - 26
    answer = answer + chr(dec)

print("Зашифрованное сообщение: " + answer)

print("Расшифровать сообщение? Ответьте 'Yes' или 'No'")
ok = input()
if ok == 'Yes' or ok == 'yes':
    print(message)
