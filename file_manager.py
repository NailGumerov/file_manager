import os

cur_path = os.getcwd()
is_work = True

while is_work:
    input_command = input("Введите команду: ")
    command = ''
    split = None
    if input_command != '':
        split = input_command.split()
        command = split[0]

    # pwd - просмотр теĸущей папĸи
    # cd dirname  - переход в другую папĸу
    # touch filename  - создание пустого файла
    # cat filename - вывод содержимого файла
    # ls - вывод списĸа файлов в папĸе
    # rm filename - удаление файла

    if command == "pwd":
        print("Текущая папка: ", cur_path)

    elif command == "touch":
        if len(split) > 1:
            new_file = os.path.join(cur_path, split[1])

            open(new_file, 'a')
        else:
            print("Вы не ввели название файла")

    elif command == "cat":
        file = os.path.join(cur_path, split[1])
        if os.path.exists(file):
            with open(split[1], 'r') as exist_file:
                for line in exist_file:
                    print(line.strip())
        else:
            print("Такого файла нет")

    elif command == "ls":
        print("Все файлы в папке ", cur_path, " ", os.listdir(cur_path), " ")

    elif command == "rm":
        file = os.path.join(cur_path, split[1])
        if os.path.exists(file):
            try:
                os.remove(file)
            except IsADirectoryError:
                print("Это папка, а не файл, поэтому ее нельзя удалить")
        else:
            print("Такого файла нет")

    elif command == "cd":
        file_dir = os.path.join(cur_path, split[1])
        if os.path.exists(file_dir):
            os.chdir(file_dir)
            cur_path = file_dir
            print("Вы сейчас в папке: ", cur_path)
        elif split[1] in cur_path:
            os.chdir(cur_path.split(split[1])[0]+split[1])
            cur_path = cur_path.split(split[1])[0]+split[1]
            print("Вы сейчас в папке: ", cur_path)
        else:
            print("Такой папки нет")

    elif command == '':
        print("Вы не ввели команду")

    elif command == "exit":
        is_work = False

    else:
        print("Такой команды нет")
