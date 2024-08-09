my_dict = {'Denis': 2000, 'Liza': 2006, 'Eva': 2001}
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Kate'))
my_dict['Anton'] = 2009
my_dict['Sasha'] = 1999
a = my_dict.pop('Denis')
print(a)
print(my_dict)

my_set = {1, 2, 4, 6, 1, 7, 2, 6}
print(my_set)
my_set.add('String')
my_set.add('True')
my_set.discard(7)
print(my_set)