H24121078_quiz7.pydef display_menu():
    print("\nMenu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Get book information")
    print("4. List all books")
    print("5. List books by genre")
    print("6. Quit")

def list_all_books(library):
    if library:
        for title in sorted(library.keys()):
            print(f"{title}: {library[title]['genre']} - ${library[title]['price']:.2f}")
    else:
        print("No books in the library.")

def main():
    library = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            get_book_info(library)
        elif choice == '4':
            list_all_books(library)
        elif choice == '5':
            list_books_by_genre(library)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()