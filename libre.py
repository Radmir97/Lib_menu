import json
import os
DATA_FILE = "library_data.json"

# Загрузка данных из файла
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Сохранение данных в DATA_FILE
def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Данные успешно сохранены в файл {DATA_FILE}.")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


# Генерируем уникальных ID 
def id_generator(data):
    if not isinstance(data, list):
        raise TypeError("data должно быть списком словарей")
    return max([book.get('id', 0) for book in data], default=0) + 1


# Функция для добавления книги
def add_data(data):
    title = input('Введите название книги: ')
    author = input('Введите имя автора: ')
    year = input('Введите год издания книги: ')
    if not year.isdigit():
        print('Ошибка: Год издания должен быть числом.')
        return

    book = {
        "id": id_generator(data),
        "title": title,
        "author": author,
        "year": int(year),
        'status': 'в наличии'
    }
    data.append(book)
    print('Книга успешно добавлена.')
    save_data(data)


# Функция для удаления книги
def delete(data):
    try:
        book_id = int(input("Введите ID книги для удаления:" ))
        for x in data:
            if x['id'] == book_id:
                book = x
                break
        if book:
            data.remove(book)
            save_data(data)
            print('Книга удалена')
        else:
            print('Книга с таким ID не обнаружена')    
    except ValueError:
        print('ID должен быть числом')        


# Функция для поиска книг
def search(data):
    query = input("Введите название, автора или год издания для поиска: ").strip().lower()
    results = [
        book for book in data
        if query in str(book['title']).lower()
        or query in str(book['author']).lower()
        or query in str(book['year'])
    ]

    if results:
        print("Результаты поиска:")
        print_book(results)

    else:
        print('Книга не найдена')

#отображение всех книг            
def print_book(data):
    if not data:
        print("Библиотека пуста.")
        return
    
    # Вывод заголовка
    headers = ['ID', 'Название', 'Автор', 'Год', 'Статус']
    print('\t'.join(headers))
    print("-" * 50)

    # Вывод информации о каждой книге
    for book in data:
        print(f"{book['id']}\t{book['title']}\t{book['author']}\t{book['year']}\t{book['status']}")


# Функция для изменения статуса книги
def change_info(data):
    try:
        book_id = int(input('Введите ID книги'))
        new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
        if new_status not in ['в наличии', 'выдана']:
            print("Некорректный статус.")
            return
    
        book = None
        for x in data:
            if x['id'] == book_id:
                book = x
                break

        if book:
            book['status'] = new_status
            save_data(data)
            print("Статус книги обновлён.")
        else:
            print("Ошибка: Книга с указанным ID не найдена.")
    except ValueError:
        print("Ошибка: ID должен быть числом.")


def main():
    data = load_data()

    while True:
        print('Требуется выбирать по числу')
        print('Меню:')   
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Найти книгу')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выход')
        querry = int(input('Введите число:'))

        if querry == 1:
            add_data(data)
        elif querry == 2:
            delete(data)
        elif querry == 3:
            search(data)
        elif querry == 4:
            print_book(data)
        elif querry == 5:
            change_info(data)
        elif querry == 6:
            print('Выход из меню')
            break

        else:
            print('Что-то пошло не так, повторите попытку')


if __name__ == "__main__":
    main()
    

print("Текущая рабочая директория:", os.getcwd())    