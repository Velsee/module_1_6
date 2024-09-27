my_dict = {'Vasya' : 1999, 'Petya' : 2000, 'Yulya' : 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict['Yulya'])
print('Not existing value:', my_dict.get('Ira'))
my_dict.update({'Vanya' : 1998, 'Valya' : 1997})
name = my_dict.pop('Vanya')
print('Deleted value:', name)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 2, True, True, 'apple', '1', '1', 1.234, (1, 3, 5)}
print('Set:', my_set)
my_set.add(5)
my_set.add('coconut')
my_set.remove((1, 3, 5))
print('Modified set:', my_set)