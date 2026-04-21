# library/books.py

# Books list  
books = {
    "B001": {"title": "Introduction to Python",    "author": "Mark Lutz",       "available": True},
    "B002": {"title": "Data Structures in C",       "author": "Reema Thareja",   "available": True},
    "B003": {"title": "Operating Systems",          "author": "Silberschatz",    "available": True},
    "B004": {"title": "Computer Networks",          "author": "Forouzan",        "available": True},
    "B005": {"title": "Ethical Hacking Basics",     "author": "EC-Council",      "available": True},
    "B006": {"title": "Discrete Mathematics",       "author": "Kenneth Rosen",   "available": True},
    "B007": {"title": "Database Management Systems","author": "Ramakrishnan",    "available": True},
}


# Functions 
def display_all_books():
    
    print("\n  ╔══════════════════════════════════════════════════════════════════════╗")
    print("  ║                          BOOK CATALOG                                ║")
    print("  ╠══════╦═══════════════════════════════════╦══════════════════╦════════╣")
    print("  ║  ID  ║  Title                            ║  Author          ║ Status ║")
    print("  ╠══════╬═══════════════════════════════════╬══════════════════╬════════╣")
    for book_id, info in books.items():
        status = "✔ Free " if info["available"] else "✘ Out  "
        print(f"  ║ {book_id} ║ {info['title']:<33} ║ {info['author']:<16} ║ {status}║")
    print("  ╚══════╩═══════════════════════════════════╩══════════════════╩════════╝")


def book_exists(book_id):
    
    return book_id in books


def is_book_available(book_id):
    
    return book_id in books and books[book_id]["available"]


def mark_issued(book_id):
    
    books[book_id]["available"] = False


def mark_returned(book_id):
    
    books[book_id]["available"] = True


def get_book_title(book_id):
    
    return books.get(book_id, {}).get("title", "Unknown Book")