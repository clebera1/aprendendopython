'''def make_some_eggs(quantity, egg_type):
    print(f'make {quantity} {egg_type} eggs')

make_some_eggs('30', 'hosted')'''

'''def counter_loop(start, end):
    counter = start
    while counter < end:
        counter = counter * 2
        print(counter)

counter_loop(1, 1000)'''

'''def counter_loop(start, end):
    counter = start
    while True:
        counter = counter * 2
        print(counter)
        if counter > end:
            break
        
counter_loop(2, 1000)'''

def numbers_under_ten(list_of_numbers):
    new_numbers = []
    for number in list_of_numbers:
        if number < 10:
            new_numbers.append(number)
            
    print(new_numbers)   


def numbers_under_100(list_of_numbers):
    new_list = []
    for number in list_of_numbers:
        if number < 100:
            new_list.append(number)
    print(new_list)

numbers_under_ten([10, 100, 2000, 39, 3949, 32, 1])
numbers_under_100([10, 100, 2000, 39, 3949, 32, 1])

    