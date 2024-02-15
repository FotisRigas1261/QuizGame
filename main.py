import window_types as windows
#In order to make it executable:
#python -m PyInstaller --onefile --windowed --add-data "logo.png;." main.py

def main():
    windows.open_main_menu()

if __name__ == "__main__":
    main()