#открываем телефонную книгу, копируем ее в памяти, работаем с этой копией. И если хотим в результате выхода сохранить изменения,
# то записываем их, а если не хотим записывать изменения,то просто выходим из программы

SEPARATOR = ';'

phone_book = {}
path = 'phones.txt'

def open_phone_book():
    global phone_book #рекомендуется использовать крайне редко  global
    with open (path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
        for u_id, contact in enumerate(data,1):
            phone_book[u_id] = contact.strip().split(SEPARATOR) #sprip очищает от переходов на новую строку;

def save_phone_book():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def _next_id(): # _ - означает,что эта ф-я работает только в этом модуле и не предназначена, чтоб ее тащиили в другие модуля
    global phone_book
    return max(phone_book) + 1 if phone_book else 1 #проходит по ключам, которые являются айдишниками
    

def add_new_contact(new_contact: list[str]): #ничего возвращать не будем
   global phone_book
   phone_book[_next_id()] = new_contact 
    

def find_contact(search_word: str) -> dict[int, list[str]]: #указывать -> не обязательно, но работает как подсказка для читающего код
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():#contact это список (имя, тел , комментарий),делаем поиск по всему contact
        if search_word.lower() in ' '.join(contact).lower():#соеденяем весь contact через пробел
            result[u_id] = contact
    return result

def edit_contact(u_id: int, edited_contact: list[str]): #возвращаться ничего не будет
    global phone_book
    current_contact = phone_book[u_id]
    for i in range (len(current_contact)):
        current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]   
        '''мы передаем измененный контакт current_contact и меняем на измененный контакт, если внесли изменения=то есть оно не пустое'''
    phone_book[u_id] = current_contact #записываем в phone_book измененный контакт
    return current_contact[0]

def delete_contact(u_id: int) -> str:
    global phone_book
    return phone_book.pop(u_id)[0]
