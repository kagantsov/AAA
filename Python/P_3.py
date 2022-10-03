a = ('qwert')
b = (111111)
c = ('qwweertty')
d = (592271)
e = ('qwerty')
f = ('defxyz')

# Функция переворода списка
def reverse_list(a_list: list) -> list:
    if not isinstance(a_list, list):
        print('Not list')
        return []
    b = []
    for a, i in enumerate(a_list):
        b.append(a_list[-a-1])
    return b

# Убрать дубликаты в исходном объекте
def drop_dups(array):
    try:
        unice_elements = []
        for elem in array:
            if elem not in unice_elements:
                unice_elements.append(elem)
        return (unice_elements)
    except TypeError:
        print('Is not iterrible')

#Подсчитать кол-во элементов, которые встречаются более 1 раза в исходном объекте
# A = {}
# B = []
# for i in range(len(a)):
#     if A.get(a[i]) == None:
#         A[a[i]] = 0
#     A[a[i]] += 1
# for j in A:
#     if A[j]>1:
#         B.append(j)
# print(B)

#Разбить исходное число на разряды
def razryad(number):
    list_reversed=[]
    while number != 0:
        ostatok = int(number%10)
        list_reversed.append(ostatok)
        number=(number-ostatok)/10
    list_m = list_reversed[::-1]
    return list_m

#Подсчитать кол-во чётных и нечётных цифр исходного числа.
# def count_odds_evens(val: int) -> dict:
#     if val < 0 or not isinstance(val, int):
#         print('Error')
#     else:
#     even = 0
#     odd = 0
#     for i in val:
#         if int(i) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     result = {'odds': odd, 'evens': even}
#     result result

#Найти разницу множеств
def substract_lists(array_uno, array_dos) -> list:
    try:
        result = [elt for elt in array_uno if elt not in array_dos]
        return result
    except TypeError:
        print('Error')
        return []

#Вывести, какие точки заданы некорректно с сообщением-ошибкой
def check_points(*args):
    list_of_coords = []
    for i in args:
        lat, lng = gen_mist(i[0], i[1])
       # print(f'{lat},{lng}')
        coords = {'coord1': i[0],'coord2': i[1],'error':f'{lat},{lng}'}
        list_of_coords.append(coords)
    return list_of_coords

def gen_mist(lat, lng):
    lng_error, lat_error = '', ''
    if lat < -90 or lat > 90:
        lat_error = f'Неверно задана широта: {lat}'
    if lng < -180 or lat > 180:
        lng_error = f'Неверно задана долгота: {lng}'
    return lng_error, lat_error

# def coordinates(*params):
#     for i in params:
#         print(f"lat:{i[0]}, lng{i[1]}")
#         if (i[0]<-90.0 or i[0]>90.0):
#             print('Неверно задана широта:', i[0])
#         if (i[1]<-180.0 or i[0]>180.0):
#             print('Неверно задана долгота:', i[1])


#Подсчитать, сколько раз каждое слово встречается в текстe
def count_words(text: str) -> dict:
    try:
        has_words = False
        d = dict()
        for word in text.split():
            has_words = True
            word = word.lower()
            if not d.get(word):
                d[word] = 1
            else:
                d[word] += 1
        if has_words:
            return d
        else:
            print('Пусто')
            return {}
    except TypeError:
        print('Беда')
        return {}

# Найти неверную закрывающую скобку
# есть скрин

# Написать генератор паролей


if __name__ == '__main__':
    print(check_points((0.0, 1.0)