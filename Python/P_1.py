# a = [0, 1, 2, 3, 4, 5]
# b = [3, 4, 5]
# c = []
# for item in a:
#    if item in b and item not in c:
#            c.append(item)
# print(c)


# a = [0, 0, 1, 1, 2, 2]
# unique_numbers = list(set(a))

# print(unique_numbers)


# a = [0, 1, 2, 3, 4, 5]
# print(*(x for x in a if not int(x) % 2))


# ВОТ ТУТ РАЗБЕРИСЬ

# a = ['foo', 'bar', 'baz']
#
# def function(a):
#    return {i: j for (i, j) in enumerate(a)}
#
# print(function)


# a = [
# 'John', 'Allison', 'Brian',
# 'Claire', 'Andrew'
# ]
#
# for element in a:
#     print(f'Hi, {element}')
#     print('Hi, %s' %(element))
#     print('Hi, {}'.format(element))


# a = ['foo', 'bar', 'baz', 'egg']
# b = ['bar', 'baz']
#
# c = [element for element in a if element not in b]
# f = ', '.join(c)
# print('отсутствуют {a}'.format(a=f))


# a = [0, 1, 2, 6, 7, 8]
# b = [3, 4, 5]
#
# print(sorted(a + b))


# a = {0: 'foo', 1: 'bar', 2: 'baz'}
#
# items = list(a.items())
# b = {k: v for k, v in reversed(items)}
# print(b)

import requests
response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')

data = response.json()
data_1 = data.get('dataseries')
# json.dumps(json_formatted_text , indent=4)

for element in data_1:
    # element['wind10m']
    print(f'направление: {element["wind10m"]["direction"]}, скорость: {element["wind10m"]["speed"]}')