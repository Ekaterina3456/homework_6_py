# Напишите модуль с функцией, которая принимает строку и возвращает строку с
# удаленными дублирующимися подряд идущими символами. Например, строка
# "aabbccaa" должна быть преобразована в "abca".


# def change_text(text):
#     text_2 = ''
#     for i in range(len(text) - 1):
#         if text[i] == text[i+1]:
#             text_2 += text[i]
#     return text_2


def change_text(text):
    result = [text[0]]
    for i in text[1:]:
        if i != result[-1]:
            result.append(i)
    return ''.join(result)


if __name__ == '__main__':
    text_1 = 'aabbccaaa'
    print(change_text(text_1))
