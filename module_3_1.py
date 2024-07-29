calls = 0


def count_calls():
    global calls
    calls += 1


print(f'Количество вызова функции: {calls} раз(а)')


def string_info(string):
    global calls
    count_calls()
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return (length, lower_string, upper_string)
    string_info('Capybara')
    string_info('Armageddon')


print(string_info('Capybara'))
print(string_info('Armageddon'))

print(f'Количество вызова функции: {calls} раз(а)')


def is_contains(string, list_to_search):
    global calls
    count_calls()
    lower_string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return lower_string in list_to_search
    is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
    is_contains('cycle', ['recycling', 'cyclic'])


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(f'Количество вызова функции: {calls} раз(а)')
