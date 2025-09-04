# tests/test_issue_return.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tempfile, shutil
from storage import save_books, save_members, load_books
from models import Book, Member
from rules import issue_book, return_book

def setup_temp_dir():
    # temp dir with 1 book + 1 member for testing
    tmpdir = tempfile.mkdtemp()
    books = [Book("b001", "Test Book", "Tester", "12345", 1)]
    members = [Member("m001", "Ajay", "ajay@test", "2025-09-04", "dummyhash", "Member")]
    save_books(tmpdir, books)
    save_members(tmpdir, members)
    return tmpdir

def test_issue_then_return_restores_availability():
    data_dir = setup_temp_dir()
    try:
        books = load_books(data_dir)
        assert books[0].CopiesAvailable == 1  # start with 1

        loan = issue_book(data_dir, "m001", "12345")
        books = load_books(data_dir)
        assert books[0].CopiesAvailable == 0  # issued -> now 0

        return_book(data_dir, loan.LoanID)
        books = load_books(data_dir)
        assert books[0].CopiesAvailable == 1  # returned -> back to 1

    finally:
        shutil.rmtree(data_dir)  # cleanup
