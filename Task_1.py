# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.


def count_words(text: str):
    list_1 = text.split()
    dict_1 = {}
    for item in set(list_1):
        dict_1[item] = list_1.count(item)
    return dict_1


if __name__ == '__main__':
    text_1 = input('введите строку с повторяющимися словами')
    print(count_words(text_1))