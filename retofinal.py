def check_access(user):
    if user.get("role") == "admin" and user.get("active") == True:
        return ["ALLOW_ACCESS"]
    else:
        return ["DENY_ACCESS"]


user1 = {"role": "admin", "active": True}
user2 = {"role": "admin", "active": False}
user3 = {"role": "user", "active": True}

try:
    print(check_access(user0))
except Exception as e:
    print(f"Error: {e}")
print(check_access(user2))
print(check_access(user3))
print(check_access(user3))