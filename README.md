# 📚 Library Management System  

A simple **Library Management System** built in Python as part of my learning journey at Masai.  
This project helped me practice **OOP concepts, file handling, authentication, and testing** while simulating a real-life library workflow.  

---

## 🚀 Features  

### 👑 Librarian  
- Add / Delete Books  
- Register Members (assign role: Librarian or Member)  
- Issue & Return Books  
- View Overdue Loans  

### 👤 Member  
- Search Catalogue (by Title, Author, or ISBN)  
- Check Book Availability  
- View Own Loan History  

---

## 🛠️ Tech & Concepts Used  
- **Python 3** (classes, functions, file handling, error handling)  
- **CSV storage** (books, members, loans)  
- **bcrypt** for password hashing  
- **Datetime** for due dates & overdue detection  
- **pytest** for automated testing  

---
## ▶️ How to Run  
1. Clone or download this repo.  
2. Install dependencies:  
   ```bash
   pip install bcrypt pytest
3. Run the system
   ```bash
   python main.py --data-dir data
4. Default Librarian login <br>
   **ID:** lib001 <br>
   **Password:** admin123  

## ✅ Testing  

   Run automated tests with:  

  ***pytest -q***
 Green means everything is working! 🎉

## 📖 Sample Data
  The data/ folder includes sample books.csv, members.csv, and loans.csv for quick demo.

## 🙋 About
  This was my first major Python project, built as part of Masai curriculum.
I faced challenges with authentication, CSV order mismatches, and overdue calculation — but fixing them taught me debugging and clean coding.
   

  
