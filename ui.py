class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def print_banner(path):
    with open(path, "r", encoding="utf-8") as f:
        print(Colors.BLUE + f.read() + Colors.RESET)


def menu():
    print("\n[1] Запуск модуля (SCAN)")
    print("[2] Информация")
    print("[3] Анимация")
    print("[0] Выход")
