
data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    result = int()
    for i in data_structure:
        if isinstance(i, int):
            result += i
        elif isinstance(i, str):
            result += len(i)
        elif isinstance(i, dict):
            result += calculate_structure_sum(i.items())
        elif isinstance(i, tuple):
            result += calculate_structure_sum(i)
        elif isinstance(i, list):
            result += calculate_structure_sum(i)
        elif isinstance(i, set):
            result += calculate_structure_sum(i)
    return result

result=calculate_structure_sum(data_structure)
print(result)