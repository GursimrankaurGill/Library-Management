# main.py  —  Library Management System

from library.books   import (display_all_books, book_exists,
                              is_book_available, mark_issued,
                              mark_returned, get_book_title)
from library.members import issue_book, return_book, view_issued_books
1

def main():
    print("\n  ╔════════════════════════════════════════╗")
    print("  ║    WELCOME TO Library SYSTEM           ║")
    print("  ╚════════════════════════════════════════╝")

    while True:
        print("\n  ┌──────────────────────────────────────┐")
        print("  │         LIBRARY MAIN MENU            │")
        print("  ├──────────────────────────────────────┤")
        print("  │  1.  View All Books                  │")
        print("  │  2.  Issue a Book                    │")
        print("  │  3.  Return a Book                   │")
        print("  │  4.  View Issued Books               │")
        print("  │  5.  Exit                            │")
        print("  └──────────────────────────────────────┘")

        choice = input("  Choose an option (1–5): ").strip()

        if choice == "1":
            display_all_books()

        elif choice == "2":
            display_all_books()
            book_id = input("\n  Enter Book ID to issue (e.g. B001): ").strip().upper()

            if not book_exists(book_id):
                print(f"  ✘  Book ID '{book_id}' does not exist in the catalog.")
            elif not is_book_available(book_id):
                print(f"  ✘  Book '{get_book_title(book_id)}' is currently issued to someone else.")
            else:
                title   = get_book_title(book_id)
                success = issue_book(book_id, title)
                if success:
                    mark_issued(book_id)     

        elif choice == "3":
            view_issued_books()
            book_id = input("\n  Enter Book ID to return (e.g. B001): ").strip().upper()

            if not book_exists(book_id):
                print(f"  ✘  Book ID '{book_id}' does not exist.")
            else:
                title   = get_book_title(book_id)
                success = return_book(book_id, title)
                if success:
                    mark_returned(book_id)   

        elif choice == "4":
            view_issued_books()

        elif choice == "5":
            print("\n  Thank you.! Have a Great Day.\n")
            break

        else:
            print("  ✘  Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()