alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = input('Введите текст: ').lower()
length = len(text)
message = list(text)
for i in alphabet:
    print(i , '-', round((message.count(i) / length * 100), 2), '%')