import os

def add_contact(file_name, name, phone):
    with open(file_name, 'a') as f:
        f.write(f"{name},{phone}\n")

def display_contacts(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            name, phone = line.strip().split(',')
            print(f"{name}: {phone}")

def update_contact(file_name, search_name):
    updated_data = []
    with open(file_name, 'r') as f:
        for line in f:
            name, phone = line.strip().split(',')
            if name == search_name:
                new_phone = input(f"Введите новый номер телефона для {name}: ")
                updated_data.append(f"{name},{new_phone}\n")
            else:
                updated_data.append(line)
    
    with open(file_name, 'w') as f:
        f.writelines(updated_data)

def delete_contact(file_name, search_name):
    updated_data = []
    with open(file_name, 'r') as f:
        for line in f:
            name, phone = line.strip().split(',')
            if name != search_name:
                updated_data.append(line)
    
    with open(file_name, 'w') as f:
        f.writelines(updated_data)

def search_contact(file_name, search_name):
    with open(file_name, 'r') as f:
        for line in f:
            name, phone = line.strip().split(',')
            if name == search_name:
                print(f"{name}: {phone}")
                return
        print(f"Контакт с именем {search_name} не найден.")

# Пример использования функций

file_name = "contacts.txt"

while True:
    print("\nТелефонный справочник:")
    print("1. Просмотреть все контакты")
    print("2. Добавить новый контакт")
    print("3. Обновить контакт")
    print("4. Удалить контакт")
    print("5. Найти контакт")
    print("6. Выход")

    choice = input("Введите номер операции: ")

    if choice == '1':
        print("Список контактов:")
        display_contacts(file_name)
    elif choice == '2':
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        add_contact(file_name, name, phone)
        print("Контакт успешно добавлен.")
    elif choice == '3':
        name = input("Введите имя контакта для обновления: ")
        update_contact(file_name, name)
        print("Контакт успешно обновлен.")
    elif choice == '4':
        name = input("Введите имя контакта для удаления: ")
        delete_contact(file_name, name)
        print("Контакт успешно удален.")
    elif choice == '5':
        name = input("Введите имя контакта для поиска: ")
        search_contact(file_name, name)
    elif choice == '6':
        print("Программа завершена.")
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")
