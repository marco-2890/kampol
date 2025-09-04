import tkinter as tk
from tkinter import ttk, messagebox

# ใช้ตัวแปร global เพื่อเก็บสถานะการแปลง (True: C -> F, False: F -> C)
is_celsius_to_fahrenheit = True

def convert_temperature():
    """
    ฟังก์ชันสำหรับแปลงอุณหภูมิ
    """
    try:
        if is_celsius_to_fahrenheit:
            # โหมดแปลง เซลเซียส -> ฟาเรนไฮต์
            temp_c = float(entry1.get())
            temp_f = (temp_c * 9/5) + 32
            entry2.delete(0, tk.END)
            entry2.insert(0, f"{temp_f:.2f}")
        else:
            # โหมดแปลง ฟาเรนไฮต์ -> เซลเซียส
            temp_f = float(entry1.get())
            temp_c = (temp_f - 32) * 5/9
            entry2.delete(0, tk.END)
            entry2.insert(0, f"{temp_c:.2f}")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")
    except Exception as e:
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {e}")

def switch_mode():
    """
    ฟังก์ชันสำหรับสลับโหมดการแปลงและอัปเดตป้ายกำกับ
    """
    global is_celsius_to_fahrenheit
    is_celsius_to_fahrenheit = not is_celsius_to_fahrenheit
    
    # ล้างช่องกรอกและอัปเดตป้ายกำกับ
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    
    if is_celsius_to_fahrenheit:
        label1.config(text="องศาเซลเซียส")
        label2.config(text="องศาฟาเรนไฮต์")
        arrow_label.config(text=">>>>>>>>>")
    else:
        label1.config(text="องศาฟาเรนไฮต์")
        label2.config(text="องศาเซลเซียส")
        arrow_label.config(text="<<<<<<<<<")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Form1")
root.geometry("650x300")
root.resizable(False, False)

# ตั้งค่าสไตล์
style = ttk.Style()
style.configure("TLabel", font=("Tahoma", 16))
style.configure("TEntry", font=("Tahoma", 16))
style.configure("TButton", font=("Tahoma", 14))

# สร้างและจัดวางป้ายหัวข้อ
title_label = ttk.Label(root, text="Workshop2 โปรแกรมแปลงอุณหภูมิ",
                        foreground="blue", font=("Tahoma", 16, "bold"))
title_label.pack(pady=20)

# สร้างกรอบสำหรับช่องกรอกและป้ายกำกับ
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(pady=10)

# ช่องกรอกและป้ายกำกับที่ 1 (จะเปลี่ยนไปตามโหมด)
label1 = ttk.Label(input_frame, text="องศาเซลเซียส")
label1.pack(side="left", padx=(0, 10))
entry1 = ttk.Entry(input_frame, width=8)
entry1.pack(side="left")

# ป้ายลูกศร
arrow_label = ttk.Label(input_frame, text=">>>>>>>>>", font=("Tahoma", 16))
arrow_label.pack(side="left", padx=10)

# ช่องกรอกและป้ายกำกับที่ 2 (จะเปลี่ยนไปตามโหมด)
label2 = ttk.Label(input_frame, text="องศาฟาเรนไฮต์")
label2.pack(side="left", padx=(10, 0))
entry2 = ttk.Entry(input_frame, width=8)
entry2.pack(side="left")

# สร้างกรอบสำหรับปุ่ม
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(pady=20)

# ปุ่ม "Convert"
convert_button = ttk.Button(button_frame, text="คำนวณ", command=convert_temperature)
convert_button.pack(side="left", padx=10, ipadx=10, ipady=5)

# ปุ่ม "สลับโหมด"
switch_button = ttk.Button(button_frame, text="สลับโหมด", command=switch_mode)
switch_button.pack(side="left", padx=10, ipadx=10, ipady=5)

# ปุ่ม "Exit"
exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side="left", padx=10, ipadx=10, ipady=5)

# เริ่มการทำงานของ GUI
root.mainloop()