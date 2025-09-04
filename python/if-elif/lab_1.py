username = input("กรอกชื่อผู้ใช้: ")
password = input("กรอกรหัสผ่าน: ")

# ตรวจสอบ role จาก username
if username == "admin":
    role = "admin"
elif username == "user":
    role = "user"
elif username == "guest":
    role = "guest"
else:
    role = "unknown"

# ตรวจสอบความแข็งแรงของรหัสผ่าน
if len(password) < 6:
    strength = "รหัสผ่านอ่อนมาก ❌"
elif password.isdigit():
    strength = "รหัสผ่านอ่อน ❗"
elif password.isalnum():
    strength = "รหัสผ่านปานกลาง ✔"
else:
    strength = "รหัสผ่านแข็งแรง 🔒"

# แสดงผลการตรวจสอบ
print(f"\n👤 ผู้ใช้: {username}")
print(f"📌 สิทธิ์: {role}")
print(f"🔐 ความปลอดภัย: {strength}")
