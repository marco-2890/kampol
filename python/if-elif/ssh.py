import hashlib

def check_port(port):
    if port == 22:
        return "🔑 SSH (Secure Shell) - Remote Login"
    elif port == 21:
        return "📂 FTP (File Transfer Protocol)"
    elif port == 23:
        return "📡 Telnet (ไม่ปลอดภัย)"
    elif port == 25:
        return "✉️ SMTP - ส่งอีเมล"
    elif port == 53:
        return "🌐 DNS - แปลงชื่อโดเมนเป็น IP"
    elif port == 80:
        return "🌐 HTTP - เว็บไม่เข้ารหัส"
    elif port == 443:
        return "🔒 HTTPS - เว็บเข้ารหัส SSL/TLS"
    elif port == 3306:
        return "🐬 MySQL - ฐานข้อมูล"
    elif port == 3389:
        return "🖥️ RDP - Remote Desktop (Windows)"
    else:
        if 0 <= port <= 1023:
            return f"⚠️ Well-Known Port ({port})"
        elif 1024 <= port <= 49151:
            return f"ℹ️ Registered Port ({port})"
        elif 49152 <= port <= 65535:
            return f"🔹 Dynamic/Private Port ({port})"
        else:
            return "❌ Invalid Port"

def password_strength(password):
    length = len(password)
    if length < 6:
        return "❌ รหัสผ่านอ่อน"
    elif 6 <= length < 10:
        return "⚠️ รหัสผ่านปานกลาง"
    else:
        return "✅ รหัสผ่านแข็งแรง"

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# โปรแกรมหลัก
while True:
    print("\n=== Mini Cyber Security Lab ===")
    print("1. ตรวจสอบพอร์ต")
    print("2. ทดสอบความแข็งแรงของรหัสผ่าน")
    print("3. แปลงข้อความเป็น SHA256")
    print("0. ออกโปรแกรม")
    
    choice = input("เลือกเมนู: ")
    
    if choice == "1":
        try:
            port = int(input("กรอกหมายเลขพอร์ต: "))
            print(check_port(port))
        except ValueError:
            print("❌ กรุณากรอกตัวเลขพอร์ตที่ถูกต้อง")
    
    elif choice == "2":
        pwd = input("ใส่รหัสผ่านเพื่อทดสอบ: ")
        print(password_strength(pwd))
    
    elif choice == "3":
        text = input("ใส่ข้อความเพื่อแปลงเป็น SHA256: ")
        print("SHA256:", sha256_hash(text))
    
    elif choice == "0":
        print("ออกจากโปรแกรม ✅")
        break
    
    else:
        print("❌ เลือกเมนูไม่ถูกต้อง")
