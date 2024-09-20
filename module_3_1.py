from xmlrpc.client import boolean
calls=0
def count_calls():
    global calls
    calls+=1
    return calls
def string_info(string):
    string=(len(string), string.upper(), string.lower())
    count_calls()
    return string
def is_contains(string, list_to_search):
    fl=bool
    for elem in list_to_search:
        if elem.lower() == string.lower():
            fl=True
        else:
            fl=False
    count_calls()
    return  fl
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)