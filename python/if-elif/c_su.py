print("=== ระบบทดสอบความปลอดภัย ===")
print("1. สแกนพอร์ต")
print("2. ทดสอบ SQLi")
print("3. ทดสอบ XSS")

choice = int(input("เลือกการทดสอบ: "))

if choice == 1:
    print("กำลังสแกนพอร์ต... 🔍")
elif choice == 2:
    print("กำลังทดสอบ SQL Injection... ⚠️")
elif choice == 3:
    print("กำลังทดสอบ XSS... ⚠️")
else:
    print("เลือกไม่ถูกต้อง ❌")

