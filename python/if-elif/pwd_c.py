password = input("กรอกรหัสผ่าน: ")

if len(password) < 6:
    print("รหัสผ่านอ่อนมาก ❌")
elif password.isdigit():
    print("รหัสผ่านอ่อน ❗")
elif password.isalnum():
    print("รหัสผ่านปานกลาง ✔")
else:
    print("รหัสผ่านแข็งแรง 🔒")

