class Member:
    def __init__(self, MemberID, Name, Email, JoinDate, PasswordHash, Role="Member"):
        self.MemberID = MemberID
        self.Name = Name
        self.Email = Email
        self.JoinDate = JoinDate
        self.PasswordHash = PasswordHash
        self.Role = Role  # "Librarian" or "Member"


class Book:
    def __init__(self, BookID, Title, Author, ISBN, CopiesAvailable):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.CopiesAvailable = int(CopiesAvailable)


class Loan:
    def __init__(self, LoanID, MemberID, ISBN, IssueDate, DueDate, ReturnDate):
        self.LoanID = LoanID
        self.MemberID = MemberID
        self.ISBN = ISBN
        self.IssueDate = IssueDate
        self.DueDate = DueDate
        self.ReturnDate = ReturnDate
