import os
from pathlib import Path


def create_symlink():
    target_file = input("Enter the path of the file to create a symbolic link: ")
    link_name = input("Enter the name for the symbolic link: ")
    desktop_path = Path.home() / 'Desktop'
    link_path = desktop_path / link_name

    try:
        os.startfile(target_file)
        link_path.touch()
        print("Symbolic link created successfully.")
    except Exception as e:
        print(f"Failed to create symbolic link: {e}")


def delete_symlink():
    link_name = input("Enter the name of the symbolic link to delete: ")
    desktop_path = Path.home() / 'Desktop'
    link_path = desktop_path / link_name

    try:
        link_path.unlink()
        print("Symbolic link deleted successfully.")
    except Exception as e:
        print(f"Failed to delete symbolic link: {e}")


def generate_report():
    desktop_path = Path.home() / 'Desktop'
    links = [f.name for f in desktop_path.iterdir() if f.is_file()]

    if not links:
        print("No symbolic links found on the desktop.")
    else:
        print("Symbolic links on the desktop:")
        for link in links:
            print(link)


def main():
    while True:
        print("\nMenu:")
        print("1. Create a symbolic link")
        print("2. Delete a symbolic link")
        print("3. Generate a report of symbolic links")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_symlink()
        elif choice == '2':
            delete_symlink()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("Exiting the script.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
