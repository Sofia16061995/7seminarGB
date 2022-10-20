def find_contact():
    text = input('Введите имя или номер телефона, который Вы хотите найти: ')
    with open('contacts.txt','r', encoding='utf-8') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            count += line.count(text)
        if count>=1:
            for line in lines:
                if text in line:
                    print(line)
        else:
            print('Такого контакта в справочнике не найдено')