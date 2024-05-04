import os
import shutil
import zipfile
import configparser

class FileManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.work_dir = self.config["DEFAULT"]["work_dir"]
        os.chdir('/Users/artemijmosin/Downloads/')  # Переходим в рабочую директорию
    
    def check_user_directory(self, path):
        return os.path.commonpath([os.path.realpath(self.work_dir), os.path.realpath(path)]) == os.path.realpath(self.work_dir)

    def create_user_directory(self, username):
        user_dir = os.path.join(self.work_dir, username)
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
            print(f"Created directory for user '{username}'")
        else:
            print(f"Directory for user '{username}' already exists")

    def register_user(self, username):
        user_dir = os.path.join(self.work_dir, username)
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
            print(f"Registered new user '{username}'")
        else:
            print(f"User '{username}' already exists")

    def create_directory(self, dir_name):
        if not self.check_user_directory(dir_name):
            print("Ошибка: Вы пытаетесь создать директорию за пределами своей рабочей директории.")
            return
        try:
            os.mkdir(dir_name)
            print(f"Директория '{dir_name}' создана.")
        except FileExistsError:
            print(f"Директория '{dir_name}' уже существует.")

    def delete_directory(self, dir_name):
        if not self.check_user_directory(dir_name):
            print("Ошибка: Вы пытаетесь удалить директорию за пределами своей рабочей директории.")
            return
        try:
            os.rmdir(dir_name)
            print(f"Директория '{dir_name}' удалена.")
        except FileNotFoundError:
            print(f"Директория '{dir_name}' не найдена.")
        except OSError:
            print(f"Невозможно удалить директорию '{dir_name}'. Директория не пуста.")

    def list_directory(self):
        print("Содержимое текущей директории:")
        for item in os.listdir():
            print(item)

    def change_directory(self, dir_name):
        try:
            os.chdir(dir_name)
            print(f"Перешли в директорию '{dir_name}'.")
        except FileNotFoundError:
            print(f"Директория '{dir_name}' не найдена.")

    def create_file(self, file_name):
        try:
            with open(file_name, "x"):
                print(f"Файл '{file_name}' создан.")
        except FileExistsError:
            print(f"Файл '{file_name}' уже существует.")

    def read_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                content = file.read()
                print(f"Содержимое файла '{file_name}':")
                print(content)
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

    def write_file(self, file_name, content):
        try:
            with open(file_name, "w") as file:
                file.write(content)
                print(f"Содержимое записано в файл '{file_name}'.")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

    def delete_file(self, file_name):
        try:
            os.remove(file_name)
            print(f"Файл '{file_name}' удален.")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

    def copy_file(self, src_file, dest_file):
        try:
            shutil.copy2(src_file, dest_file)
            print(f"Файл '{src_file}' скопирован в '{dest_file}'.")
        except FileNotFoundError:
            print(f"Файл '{src_file}' не найден.")

    def move_file(self, src_file, dest_file):
        try:
            shutil.move(src_file, dest_file)
            print(f"Файл '{src_file}' перемещен в '{dest_file}'.")
        except FileNotFoundError:
            print(f"Файл '{src_file}' не найден.")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Файл '{old_name}' переименован в '{new_name}'.")
        except FileNotFoundError:
            print(f"Файл '{old_name}' не найден.")
    
    def create_archive(self, source, destination):
        try:
            shutil.make_archive(destination, 'zip', source)
            print(f"Архив создан: {destination}.zip")
        except FileNotFoundError:
            print("Исходный файл/директория не найдены.")

    def extract_archive(self, source, destination):
        if not self.check_user_directory(source) or not self.check_user_directory(destination):
            print("Ошибка: Вы пытаетесь распаковать архив за пределами своей рабочей директории.")
            return
        try:
            with zipfile.ZipFile(source, 'r') as zip_ref:
                zip_ref.extractall(destination)
            print(f"Архив распакован в: {destination}")
        except FileNotFoundError:
            print("Архив не найден.")
        except zipfile.BadZipFile:
            print("Неверный формат zip-архива.")

    def disk_quota(self, username):
        user_dir = os.path.join(self.work_dir, username)
        total, used, free = shutil.disk_usage(user_dir)
        print(f"Всего дискового пространства: {total} байт")
        print(f"Использовано дискового пространства: {used} байт")
        print(f"Свободно дискового пространства: {free} байт")
        if used > total * 0.9:
            print("Предупреждение: вы приближаетесь к лимиту дискового пространства.")

if __name__ == "__main__":
    file_manager = FileManager()
    while True:
        print("\nСписок доступных команд:")
        print("1. Создать директорию")
        print("2. Удалить директорию")
        print("3. Просмотреть содержимое текущей директории")
        print("4. Перейти в другую директорию")
        print("5. Создать файл")
        print("6. Прочитать содержимое файла")
        print("7. Записать в файл")
        print("8. Удалить файл")
        print("9. Скопировать файл")
        print("10. Переместить файл")
        print("11. Переименовать файл")
        print("12. Зарегистрировать нового пользователя")
        print("13. Создать директорию для пользователя")
        print("14. Создать архив")
        print("15. Распаковать архив")
        print("16. Проверить квоту дискового пространства")
        print("17. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            dir_name = input("Введите имя новой директории: ")
            file_manager.create_directory(dir_name)
        elif choice == "2":
            dir_name = input("Введите имя директории для удаления: ")
            file_manager.delete_directory(dir_name)
        elif choice == "3":
            file_manager.list_directory()
        elif choice == "4":
            dir_name = input("Введите имя директории: ")
            file_manager.change_directory(dir_name)
        elif choice == "5":
            file_name = input("Введите имя нового файла: ")
            file_manager.create_file(file_name)
        elif choice == "6":
            file_name = input("Введите имя файла для чтения: ")
            file_manager.read_file(file_name)
        elif choice == "7":
            file_name = input("Введите имя файла для записи: ")
            content = input("Введите содержимое для записи: ")
            file_manager.write_file(file_name, content)
        elif choice == "8":
            file_name = input("Введите имя файла для удаления: ")
            file_manager.delete_file(file_name)
        elif choice == "9":
            src_file = input("Введите имя исходного файла: ")
            dest_file = input("Введите имя файла для копирования: ")
            file_manager.copy_file(src_file, dest_file)
        elif choice == "10":
            src_file = input("Введите имя исходного файла: ")
            dest_file = input("Введите имя файла для перемещения: ")
            file_manager.move_file(src_file, dest_file)
        elif choice == "11":
            old_name = input("Введите старое имя файла: ")
            new_name = input("Введите новое имя файла: ")
            file_manager.rename_file(old_name, new_name)
        elif choice == "12":
            username = input("Введите имя пользователя: ")
            file_manager.register_user(username)
        elif choice == "13":
            username = input("Введите имя пользователя для создания директории: ")
            file_manager.create_user_directory(username)
        elif choice == "14":
            source = input("Введите путь к файлу или директории: ")
            destination = input("Введите путь для сохранения архива: ")
            file_manager.create_archive(source, destination)
        elif choice == "15":
            source = input("Введите путь к архиву: ")
            destination = input("Введите путь для распаковки: ")
            file_manager.extract_archive(source, destination)
        elif choice == "16":
            username = input("Введите имя пользователя: ")
            file_manager.disk_quota(username)
        elif choice == "17":
            print("Выход.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")
