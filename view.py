import text

def show_mein_menu() ->int: #возвращает тип инт
    for i, item in enumerate(text.main_menu):
        if i != 0: #если это не нулевой элемент
            print(f'\t{i}.{item}')
        else:
            print(item)   
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int (choice) < len (text.main_menu):
            return int(choice) #если цифра и попадает в цифры от меню, то возвращаем choice
        print(text.choice_main_menu_error)

def show_contacts(phone_book: dict[int:[str]], error_messege: str):  #принимает словарь, где ключи int, а в качестве значения список строк
    if phone_book: #если она не пустая
        print('\n'+'=' * 71)
        for u_id, contact in phone_book.items():
            print(f'{u_id:>3}. {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}')
            #u_id:<3  - этой конструкцией задаем количество символов, которые занимает u_id, чтоб выровнять вывод
        print('=' * 71 + '\n')
    else:
        show_message(error_messege)

    
def show_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('=' * len(message) + '\n')

def input_data(message) -> list[str] | str: #будет возвращать список строк либо строка
    if isinstance(message, str): #если message строка 
        return input('\n'+message)#если это не строка, то возвращаем список
    return [input(mes) for mes in message] #сработает три раза


