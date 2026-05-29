from ui import print_banner, menu
from modules.scan import run_scan
from modules.animation import run_animation

print_banner("assets/banner.txt")

while True:
    menu()
    choice = input("\n> ")

    if choice == "1":
        run_scan()

    elif choice == "2":
        print("Tool v1.0 — system interface")

    elif choice == "3":
        run_animation()

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option")
