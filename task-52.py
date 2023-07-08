my_list = [1, 2, 3, 2, 1]

my_list_copy = my_list.copy()
my_list_copy.reverse()

if my_list == my_list_copy:
    print('Это палиндром')
else:
    print('Это не палиндром')