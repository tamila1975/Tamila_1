text = str(input("Введите текст"))
text = list(text)
my_dict = {symbol: text.count(symbol) for symbol in text}
print(my_dict)
