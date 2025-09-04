from auth import register_member, login
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# quick cleanup for testing (reset members.csv each run)
csv_file = os.path.join(DATA_DIR, "members.csv")
if os.path.exists(csv_file):
    os.remove(csv_file)
    print("🧹 wiped old members.csv")

# register some members
try:
    register_member(DATA_DIR, "m001", "Ajay", "ajay123")
except Exception as e:
    print("error:", e)

try:
    register_member(DATA_DIR, "m002", "Steve", "steve123")
except Exception as e:
    print("error:", e)

# login with correct creds
login(DATA_DIR, "m001", "ajay123")
login(DATA_DIR, "m002", "steve123")

# wrong password
login(DATA_DIR, "m001", "wrongpass")

# non existing member
login(DATA_DIR, "ghost", "nopass")
