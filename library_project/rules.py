import datetime
from storage import load_books, save_books, load_loans, save_loans
from models import Loan

ISSUE_DAYS = 14  # 2 weeks deadline

# issue book (librarian only)
def issue_book(data_dir, member_id, isbn):
    books = load_books(data_dir)
    loans = load_loans(data_dir)
    book = next((b for b in books if b.ISBN == isbn), None)
    if not book:
        print("❌ Oops, wrong ISBN"); return None
    if book.CopiesAvailable <= 0:
        print("❌ No copies left, all taken"); return None
    book.CopiesAvailable -= 1
    today = datetime.date.today()
    loan_id = str(len(loans) + 1)
    loan = Loan(
        LoanID=loan_id,
        MemberID=member_id,
        ISBN=isbn,
        IssueDate=today.isoformat(),
        DueDate=(today + datetime.timedelta(days=ISSUE_DAYS)).isoformat(),
        ReturnDate=""
    )
    loans.append(loan)
    save_books(data_dir, books)
    save_loans(data_dir, loans)
    print(f"✅ Book {isbn} issued to Member {member_id}. Due {loan.DueDate}")
    return loan

# return book (librarian)
def return_book(data_dir, loan_id):
    books = load_books(data_dir)
    loans = load_loans(data_dir)
    loan = next((l for l in loans if l.LoanID == loan_id), None)
    if not loan:
        print("❌ Loan ID not found"); return None
    if loan.ReturnDate != "":
        print("❌ Already returned"); return None
    loan.ReturnDate = datetime.date.today().isoformat()
    book = next((b for b in books if b.ISBN == loan.ISBN), None)
    if book:
        book.CopiesAvailable += 1
    save_books(data_dir, books)
    save_loans(data_dir, loans)
    print(f"✅ Loan {loan_id} closed. Book returned.")
    return loan

# delete book (blocked if active loans exist)
def delete_book(data_dir, isbn):
    books = load_books(data_dir)
    loans = load_loans(data_dir)
    if any(l.ISBN == isbn and l.ReturnDate == "" for l in loans):
        print("❌ Can't delete, book is on loan")
        return False
    before = len(books)
    books = [b for b in books if b.ISBN != isbn]
    if len(books) == before:
        print("❌ ISBN not found in list")
        return False
    save_books(data_dir, books)
    print(f"🗑️ Deleted book {isbn}")
    return True

# search catalogue (member)
def search_books(data_dir, query):
    q = query.strip().lower()
    books = load_books(data_dir)
    results = [
        b for b in books
        if q in b.Title.lower() or q in b.Author.lower() or q in b.ISBN.lower()
    ]
    if not results:
        print("🔎 nothing found")
    else:
        print("🔎 Search results:")
        for b in results:
            print(f"- {b.Title} by {b.Author} (ISBN {b.ISBN}) | Avail: {b.CopiesAvailable}")
    return results

# check if book available (member)
def check_availability(data_dir, isbn):
    books = load_books(data_dir)
    b = next((x for x in books if x.ISBN == isbn), None)
    if not b:
        print("❌ ISBN not found"); return None
    print(f"📦 '{b.Title}' copies left: {b.CopiesAvailable}")
    return b.CopiesAvailable

# member's own loan history
def member_loan_history(data_dir, member_id):
    loans = load_loans(data_dir)
    mine = [l for l in loans if l.MemberID == member_id]
    if not mine:
        print("🗂️ You have no loans yet.")
    else:
        print("🗂️ Your loans:")
        for l in mine:
            status = "Returned" if l.ReturnDate else f"Due {l.DueDate}"
            print(f"- Loan {l.LoanID} | ISBN {l.ISBN} | Issued {l.IssueDate} | {status}")
    return mine

# overdue loans (anyone can view)
def overdue_loans(data_dir):
    loans = load_loans(data_dir)
    today = datetime.date.today()
    overdue = [
        l for l in loans
        if l.ReturnDate == "" and datetime.date.fromisoformat(l.DueDate) < today
    ]
    if not overdue:
        print("✅ No overdue loans")
    else:
        print("⚠️ Overdue list:")
        for l in overdue:
            print(f"LoanID {l.LoanID}, Member {l.MemberID}, Book {l.ISBN}, Due {l.DueDate}")
    return overdue
