
def find_missed_letter(your_list):
    current_letter_code = ord(your_list[0])
    for next_letter in your_list[1:]:
        next_letter_code = ord(next_letter)
        if next_letter_code - current_letter_code == 2:
            return chr(current_letter_code + 1)
        current_letter_code = next_letter_code
    return None


print('Ця програма шукає одну пропущену літеру у вашій послідовності за алфавітом')
user_input = input('ВВедіть послідовність літер:')
your_list = list(user_input)
result = find_missed_letter(your_list)
if result:
    print(f'Пропущена літера: {result}')
else:
    print('Пропущеної літери немає')
my_tuple = (1, 2)
print(my_tuple[1])
students = {'name': 'Ivan', 'age': 19}
students.get('name')
