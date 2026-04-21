# library/members.py

from datetime import datetime, timedelta
from library.fines import calculate_fine, display_fine_table

# list of currently issued books
issued_records = {}

# Issue a Book 
def issue_book(book_id, title):
    
    print(f"\n  ── Issuing Book: [{book_id}] {title} ──")
    print()

    student_name = input("  Student Name    : ").strip()
    if not student_name:
        print("  ✘  Student name cannot be empty.")
        return False

    try:
        days = int(input("  Issued for (days): "))
        if days <= 0:
            raise ValueError
    except ValueError:
        print("  ✘  Please enter a valid positive number for days.")
        return False

    issue_date = datetime.now()
    due_date   = issue_date + timedelta(days=days)

    # Save the record
    issued_records[book_id] = {
        "student_name" : student_name,
        "issue_date"   : issue_date.strftime("%d-%m-%Y"),
        "days_allotted": days,
        "due_date_str" : due_date.strftime("%d-%m-%Y"),
        "due_date_obj" : due_date,
    }

    # Confirmation
    print("\n  ╔════════════════════════════════════════╗")
    print("  ║         ISSUE CONFIRMATION             ║")
    print("  ╠════════════════════════════════════════╣")
    print(f"  ║  Book     : {title[:28]:<28}  ║")
    print(f"  ║  Student  : {student_name[:28]:<28}  ║")
    print(f"  ║  Issued On: {issue_date.strftime('%d-%m-%Y'):<28}  ║")
    print(f"  ║  Due Date : {due_date.strftime('%d-%m-%Y'):<28}  ║")
    print("  ╚════════════════════════════════════════╝")

    # fine warning
    print("\n  ⚠  LATE RETURN FINE NOTICE:")
    display_fine_table()

    return True


# Return a Book 
def return_book(book_id, title):
    
    if book_id not in issued_records:
        print(f"\n  ✘  No issue record found for Book ID '{book_id}'.")
        print("  Cannot process return for a book that was not issued.")
        return False

    record      = issued_records[book_id]
    today       = datetime.now()
    due_date    = record["due_date_obj"]
    days_late   = (today - due_date).days   # negative means early return

    print("\n  ╔════════════════════════════════════════╗")
    print("  ║           RETURN PROCESSING            ║")
    print("  ╠════════════════════════════════════════╣")
    print(f"  ║  Book       : {title[:26]:<26}  ║")
    print(f"  ║  Issued To  : {record['student_name'][:26]:<26}  ║")
    print(f"  ║  Issue Date : {record['issue_date']:<26}  ║")
    print(f"  ║  Due Date   : {record['due_date_str']:<26}  ║")
    print(f"  ║  Return Date: {today.strftime('%d-%m-%Y'):<26}  ║")
    print("  ╠════════════════════════════════════════╣")

    if days_late > 0:
        fine = calculate_fine(days_late)
        print(f"  ║  ⚠  Overdue by {days_late} day(s)              ║")
        print(f"  ║  Fine Amount : Rs. {fine:<22}  ║")
    else:
        print(f"  ║  ✔  Returned on time — No fine!        ║")

    print("  ╚════════════════════════════════════════╝")

    # Remove the record (book is returned)
    del issued_records[book_id]
    return True


# View Issued Books 
def view_issued_books():
    
    print("\n  ════════════ CURRENTLY ISSUED BOOKS ════════════")
    if not issued_records:
        print("  No books are currently issued.")
    else:
        for book_id, rec in issued_records.items():
            print(f"\n  Book ID     : {book_id}")
            print(f"  Student     : {rec['student_name']}")
            print(f"  Issued On   : {rec['issue_date']}")
            print(f"  Due Date    : {rec['due_date_str']}")
            print(f"  Days Allowed: {rec['days_allotted']}")
            print("  " + "─" * 40)
    print("  ════════════════════════════════════════════════")