import csv
import os
from models import Book, Member, Loan

# helper: build full path to file
def _path(data_dir, filename):
    return os.path.join(data_dir, filename)

# books (load/save)
def load_books(data_dir):
    books = []
    path = _path(data_dir, "books.csv")
    if not os.path.exists(path):
        return books  # if no file yet, return empty
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(Book(
                BookID=row["BookID"],
                Title=row["Title"],
                Author=row["Author"],
                ISBN=row["ISBN"],
                CopiesAvailable=row["CopiesAvailable"]
            ))
    return books

def save_books(data_dir, books):
    path = _path(data_dir, "books.csv")
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=["BookID", "Title", "Author", "ISBN", "CopiesAvailable"]
        )
        writer.writeheader()
        for b in books:
            writer.writerow({
                "BookID": b.BookID,
                "Title": b.Title,
                "Author": b.Author,
                "ISBN": b.ISBN,
                "CopiesAvailable": b.CopiesAvailable
            })

# members (load/save)
def load_members(data_dir):
    members = []
    path = _path(data_dir, "members.csv")
    if not os.path.exists(path):
        return members
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            role = row.get("Role", "Member")  # fallback if no role field
            members.append(Member(
                MemberID=row["MemberID"],
                Name=row["Name"],
                Email=row["Email"],
                JoinDate=row["JoinDate"],
                PasswordHash=row["PasswordHash"],
                Role=role
            ))
    return members

def save_members(data_dir, members):
    path = _path(data_dir, "members.csv")
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=["MemberID", "Name", "Email", "JoinDate", "PasswordHash", "Role"]
        )
        writer.writeheader()
        for m in members:
            writer.writerow({
                "MemberID": m.MemberID,
                "Name": m.Name,
                "Email": m.Email,
                "JoinDate": m.JoinDate,
                "PasswordHash": m.PasswordHash,
                "Role": m.Role
            })

# loans (load/save)
def load_loans(data_dir):
    loans = []
    path = _path(data_dir, "loans.csv")
    if not os.path.exists(path):
        return loans  # nothing yet
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loans.append(Loan(
                LoanID=row["LoanID"],
                MemberID=row["MemberID"],
                ISBN=row["ISBN"],
                IssueDate=row["IssueDate"],
                DueDate=row["DueDate"],
                ReturnDate=row["ReturnDate"]
            ))
    return loans

def save_loans(data_dir, loans):
    path = _path(data_dir, "loans.csv")
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=["LoanID", "MemberID", "ISBN", "IssueDate", "DueDate", "ReturnDate"]
        )
        writer.writeheader()
        for l in loans:
            writer.writerow({
                "LoanID": l.LoanID,
                "MemberID": l.MemberID,
                "ISBN": l.ISBN,
                "IssueDate": l.IssueDate,
                "DueDate": l.DueDate,
                "ReturnDate": l.ReturnDate
            })
