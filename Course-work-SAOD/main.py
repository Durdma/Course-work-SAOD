import interface as gui
import check_funcs as check

from os import system


def main():
    len_of_options = None

    while True:
        fl = False
        option = None

        while fl is False:
            gui.MainMenuCLS.name_app()
            len_of_options = gui.MainMenuCLS.main_menu()

            option = input("Введите номер действия: ")

            option, fl = check.check_choice(option, len_of_options)

            if fl is False:
                input('Нажмите "Enter", чтобы повторить ввод!')
                system("cls")

        if option == 0:
            break
        elif option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass
        elif option == 11:
            pass
        elif option == 12:
            pass
        elif option == 13:
            pass
        elif option == 14:
            pass


if __name__ == "__main__":
    main()
