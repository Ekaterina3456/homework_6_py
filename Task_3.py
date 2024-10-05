# Создайте модуль с функцией, которая принимает два списка и возвращает
# список, содержащий только элементы, которые уникальны для обоих списков


def join_lists(list_1, list_2):
    joins = (set(list_1) - set(list_2)) | (set(list_2) - set(list_1))
    return joins


if __name__ == '__main__':
    list_one = [2,5,1,4,2,4,76,3,1]
    list_two = [1,3,6,8,65,3,24,2,54]
    print(join_lists(list_one, list_two))