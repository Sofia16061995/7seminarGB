
def log_contact(a, b):
    with open('contacts.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n {a} || {b}')