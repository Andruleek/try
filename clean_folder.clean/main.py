import sys

def clean_folder_logic(args):
    # Реалізуйте вашу логіку для обробки аргументів командного рядка тут
    print(f"Обробка аргументів: {args}")

def main():
    args = sys.argv[1:]  # Отримуємо аргументи командного рядка, пропускаючи перший аргумент, який є назвою скрипта
    clean_folder_logic(args)

if __name__ == "__main__":
    main()