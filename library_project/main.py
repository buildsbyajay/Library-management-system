import argparse
import os
from auth import ensure_default_admin, register_member, login
from rules import (
    issue_book, return_book, overdue_loans, delete_book,
    search_books, check_availability, member_loan_history
)
from storage import load_books, save_books
from models import Book

# arg parser (lets me pass --data-dir if I want custom folder)
parser = argparse.ArgumentParser()
parser.add_argument("--data-dir", default="data", help="Path to data folder")
args = parser.parse_args()
DATA_DIR = args.data_dir

# menu for librarian
def librarian_menu():
    print("\n=== Librarian Menu ===")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Register Member")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Overdue Loans")
    print("7. Logout")

# menu for member
def member_menu():
    print("\n=== Member Menu ===")
    print("1. Search Catalogue")
    print("2. Check Availability by ISBN")
    print("3. View My Loan History")
    print("4. Logout")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    ensure_default_admin(DATA_DIR)

    current_user = None
    while True:
        if not current_user:
            print("\n====================================")
            print("📚 Masai Library Management System")
            print("====================================")
            print("1. Login")
            print("2. Exit")
            choice = input("Choose: ").strip()
            if choice == "1":
                mid = input("Member ID: ")
                pwd = input("Password: ")
                current_user = login(DATA_DIR, mid, pwd)
            elif choice == "2":
                print("👋 bye bye")
                break
            else:
                print("❌ wrong choice, try again 🙂")
            continue

        # librarian dashboard
        if current_user.Role == "Librarian":
            librarian_menu()
            c = input("Choose: ").strip()
            if c == "1":
                books = load_books(DATA_DIR)
                book_id = f"b{len(books)+1:03}"
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                try:
                    copies = int(input("Copies Available: "))
                except ValueError:
                    print("❌ please enter number only")
                    continue
                if copies <= 0:
                    print("❌ Copies must be > 0")
                else:
                    books.append(Book(book_id, title, author, isbn, copies))
                    save_books(DATA_DIR, books)
                    print(f"✅ Added '{title}' (ISBN {isbn})")
            elif c == "2":
                isbn = input("ISBN to delete: ")
                delete_book(DATA_DIR, isbn)
            elif c == "3":
                mem_id = input("New Member ID: ")
                name = input("Name: ")
                pwd = input("Password: ")
                role = input("Role (Librarian/Member) [default Member]: ").strip() or "Member"
                try:
                    register_member(DATA_DIR, mem_id, name, pwd, role)
                except ValueError as e:
                    print(e)
            elif c == "4":
                isbn = input("ISBN to issue: ")
                member_id = input("Issue to Member ID: ")
                issue_book(DATA_DIR, member_id, isbn)
            elif c == "5":
                loan_id = input("Loan ID to return: ")
                return_book(DATA_DIR, loan_id)
            elif c == "6":
                overdue_loans(DATA_DIR)
            elif c == "7":
                current_user = None
                print("🔓 logged out")
            else:
                print("❌ invalid option")

        # member dashboard
        else:
            member_menu()
            c = input("Choose: ").strip()
            if c == "1":
                q = input("Search text (title/author/isbn): ")
                search_books(DATA_DIR, q)
            elif c == "2":
                isbn = input("ISBN: ")
                check_availability(DATA_DIR, isbn)
            elif c == "3":
                member_loan_history(DATA_DIR, current_user.MemberID)
            elif c == "4":
                current_user = None
                print("🔓 logged out")
            else:
                print("❌ invalid option")

if __name__ == "__main__":
    main()
