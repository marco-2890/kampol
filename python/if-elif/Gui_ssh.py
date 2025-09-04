import tkinter as tk
from tkinter import ttk
import hashlib

# ---------------- ฟังก์ชัน ----------------
def check_port(port):
    ports = {
        22: "🔑 SSH (Secure Shell) - Remote Login",
        21: "📂 FTP (File Transfer Protocol)",
        23: "📡 Telnet (ไม่ปลอดภัย)",
        25: "✉️ SMTP - ส่งอีเมล",
        53: "🌐 DNS - แปลงชื่อโดเมนเป็น IP",
        80: "🌐 HTTP - เว็บไม่เข้ารหัส",
        443: "🔒 HTTPS - เว็บเข้ารหัส SSL/TLS",
        3306: "🐬 MySQL - ฐานข้อมูล",
        3389: "🖥️ RDP - Remote Desktop (Windows)"
    }
    if port in ports:
        return ports[port]
    elif 0 <= port <= 1023:
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

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Mini Cyber Security Lab")
root.geometry("600x500")
root.configure(bg="#f0f2f5")

def update_result(text):
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, text)
    result_text.config(state='disabled')

# --- Port Frame ---
port_frame = ttk.LabelFrame(root, text="ตรวจสอบพอร์ต", padding=15)
port_frame.pack(fill="x", padx=20, pady=10)

port_entry = ttk.Entry(port_frame)
port_entry.pack(side="left", expand=True, fill="x", padx=5)
ttk.Button(port_frame, text="ตรวจสอบ", command=lambda: update_result(check_port(int(port_entry.get()) if port_entry.get().isdigit() else "0"))).pack(side="left", padx=5)

# --- Password Frame ---
pwd_frame = ttk.LabelFrame(root, text="ทดสอบความแข็งแรงของรหัสผ่าน", padding=15)
pwd_frame.pack(fill="x", padx=20, pady=10)

password_entry = ttk.Entry(pwd_frame, show="*")
password_entry.pack(side="left", expand=True, fill="x", padx=5)

# Checkbox แสดง/ซ่อนรหัสผ่าน
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_var = tk.BooleanVar()
show_check = tk.Checkbutton(pwd_frame, text="แสดงรหัสผ่าน", variable=show_var, command=toggle_password)
show_check.pack(side="left", padx=5)

ttk.Button(pwd_frame, text="ทดสอบ", command=lambda: update_result(password_strength(password_entry.get()))).pack(side="left", padx=5)

# --- SHA256 Frame ---
sha_frame = ttk.LabelFrame(root, text="แปลงข้อความเป็น SHA256", padding=15)
sha_frame.pack(fill="x", padx=20, pady=10)

sha_entry = ttk.Entry(sha_frame)
sha_entry.pack(side="left", expand=True, fill="x", padx=5)
ttk.Button(sha_frame, text="แปลง", command=lambda: update_result(f"SHA256: {sha256_hash(sha_entry.get())}")).pack(side="left", padx=5)

# --- Result Frame ---
result_frame = ttk.LabelFrame(root, text="ผลลัพธ์", padding=15)
result_frame.pack(fill="both", expand=True, padx=20, pady=10)

result_text = tk.Text(result_frame, height=10, wrap="word", state="disabled")
result_text.pack(fill="both", expand=True)

# --- Exit Button ---
exit_btn = tk.Button(root, text="ออกจากโปรแกรม", bg="#e74c3c", fg="white", font=("Arial", 12), command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
