import os
import re
import os.path
# Напишите функцию, которая создает заметку


def build_note(note_text, note_name):
    # Проверьте, существует ли файл, название которого указывает пользователь.
    # Если нет, создайте новый файл. Если да, замените существующий файл на новый.
    try:
        try:
            file = open(f"{note_name}.txt", "r+", encoding="utf-8")
            print("Такой файл существует")
        except IOError:
            file = open(f"{note_name}.txt", "w+", encoding="utf-8")
            print("Файл создан")
        file.write(note_text)
        print(f"Заметка {note_name} создана.")
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая запрашивает название и текст заметки у пользователя, после чего создает заметку

def create_note():
    try:
        note_name = input("Введите название заметки: ")
        forbidden_symbols = "\\|/*<>?:"
        pattern = "[{0}]".format(forbidden_symbols)
        if re.search(pattern, note_name):
            print(
                "Вы ввели недопустимые символы в названии файла. Переименуйте заметку."
            )
        else:
            print("Название заметки создано.")
            note_text = input("Введите текст заметки: ")
            build_note(note_text, note_name)
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


# Напишите функцию, которая выводит заметку по запросу пользователя

def read_note():
    try:
        note_name = input("Введите название заметки: ")
        path = f"{note_name}.txt"
        if os.path.isfile(path):
            print("Файл существует")
            with open(f"{note_name}.txt", "r", encoding="utf-8") as file:
                file.read()
        else:
            print("Заметка не найдена")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Напишите функцию, которая редактирует заметку

def edit_note():
    try:
        note_name = input("Введите название заметки: ")
        path = f"{note_name}.txt"
        if os.path.isfile(path):
            print("Файл существует")
            note_text_new = open(f"{note_name}.txt", "w+", encoding="utf-8")
            new_content = input("Введите новый текст заметки: ")
            note_text_new.write(new_content)
            print("Заметка успешно обновлена.")
        else:
            print("Заметка не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Напишите функцию, которая удаляет заметку


def delete_note():
    try:
        note_name = input("Введите название заметки: ")
        path = f"{note_name}.txt"
        if os.path.isfile(path):
            os.remove(f"{note_name}.txt")
            print("Заметка успешно удалена.")
        else:
            print("Заметка не найдена.")

    except Exception as e:
        print(f"Произошла ошибка при удалении заметки: {e}")

# Напишите функцию, которая управляет работой приложения


# Напишите функцию, которая выводит все заметки пользователя

def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]

        notes_sorted = sorted(notes, key=lambda note: len(open(note, encoding='utf-8').read()))

        for note in notes_sorted:
            with open(note, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"\nСодержимое заметки '{note}':")
                print(content)
    except Exception as e:
        print(f"Произошла ошибка при отображении заметок: {e}")


# Напишите функцию, которая управляет работой приложения

def main():
    while True:
        print('\nМеню')
        print('1. Создать заметку')
        print('2. Прочитать заметку')
        print('3. Отредактировать заметку')
        print('4. Удалить заметку')
        print('5. Демонстрация заметок в упорядоченном виде')

        choice = input('Выберите действие (1/2/3/4/5): ')
        allowed_symbols = '123456n'
        pattern_1 = "[{0}]".format(allowed_symbols)
        if re.search(pattern_1, choice):
            print("Вы ввели корректный запрос. Действие сейчас выполнится.")

            if choice == '1':
                create_note()
            if choice == '2':
                read_note()
            if choice == '3':
                edit_note()
            if choice == '4':
                delete_note()
            if choice == '5':
                display_notes()
            if choice == 'n':
                break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")

        # Предложите пользователю продолжить работу с приложением
        print("Чтобы продолжить работать с заметками, нажмите y/n")
        answer = input()
        if answer != "y":
            break


main()

