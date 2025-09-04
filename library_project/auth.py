import bcrypt
from datetime import date
from models import Member
from storage import load_members, save_members

# makes sure we have at least 1 librarian account
def ensure_default_admin(data_dir):
    members = load_members(data_dir)
    if any(m.MemberID == "lib001" for m in members):
        return
    hashed = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
    admin = Member(
        MemberID="lib001",
        Name="Librarian",
        Email="admin@library",
        JoinDate=date.today().isoformat(),
        PasswordHash=hashed,
        Role="Librarian"
    )
    members.append(admin)
    save_members(data_dir, members)
    print("👑 Default librarian ready (id=lib001 / pass=admin123)")

# register a new member (default role = Member)
def register_member(data_dir, member_id, name, password, role="Member"):
    members = load_members(data_dir)
    if any(m.MemberID == member_id for m in members):
        raise ValueError("❌ Member ID already exists")
    email = input("Enter Email: ")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    join_date = date.today().isoformat()
    m = Member(member_id, name, email, join_date, hashed, role)
    members.append(m)
    save_members(data_dir, members)
    print(f"✅ Added new member -> {member_id} ({role})")

# login function (checks bcrypt hashed password)
def login(data_dir, member_id, password):
    members = load_members(data_dir)
    member = next((m for m in members if m.MemberID == member_id), None)
    if not member:
        print("❌ No such member id, try again")
        return None
    if bcrypt.checkpw(password.encode(), member.PasswordHash.encode()):
        print(f"✅ Login ok: {member.Name} ({member.Role})")
        return member
    else:
        print("❌ Wrong password, oops!")
        return None
