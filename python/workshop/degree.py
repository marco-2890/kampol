import tkinter as tk
from tkinter import ttk, messagebox

# --- ส่วนของฟังก์ชันการทำงาน ---
def convert_temperature():
    """
    ฟังก์ชันสำหรับแปลงอุณหภูมิจากเซลเซียสเป็นฟาเรนไฮต์
    และแสดงผลลัพธ์ในช่องกรอก
    """
    try:
        # ดึงค่าจากช่องกรอกองศาเซลเซียส
        celsius_temp = float(celsius_entry.get())
        
        # คำนวณอุณหภูมิฟาเรนไฮต์จากสูตร: F = (C * 9/5) + 32
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        
        # ล้างค่าเดิมในช่องกรอกองศาฟาเรนไฮต์
        fahrenheit_entry.delete(0, tk.END)
        
        # ใส่ค่าที่คำนวณได้ลงในช่องกรอกองศาฟาเรนไฮต์
        # f"{...:.2f}" ใช้สำหรับจัดรูปแบบทศนิยม 2 ตำแหน่ง
        fahrenheit_entry.insert(0, f"{fahrenheit_temp:.2f}")

    except ValueError:
        # แสดงกล่องข้อความแจ้งเตือนเมื่อผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้องในช่ององศาเซลเซียส")
    except Exception as e:
        # ดักจับข้อผิดพลาดอื่น ๆ ที่อาจเกิดขึ้น
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {e}")

# --- ส่วนของการสร้างหน้าต่าง GUI ---

# สร้างหน้าต่างหลักของโปรแกรม (root window)
root = tk.Tk()
root.title("Form1")
root.geometry("650x300")
root.resizable(False, False) # ไม่อนุญาตให้ย่อ/ขยายขนาดหน้าต่าง

# ตั้งค่าสไตล์ (Theme) ให้กับ Widget ต่างๆ
style = ttk.Style()
style.configure("TLabel", font=("Tahoma", 16))
style.configure("TEntry", font=("Tahoma", 16))
style.configure("TButton", font=("Tahoma", 14))

# สร้างและจัดวางป้ายหัวข้อโปรแกรม
title_label = ttk.Label(root, text="Workshop2 โปรแกรมแปลงองศาเซลเซียสเป็นองศาฟาเรนไฮต์",foreground="blue",font=("Tahoma", 16, "bold"))
title_label.pack(pady=20)

# สร้างกรอบ (Frame) สำหรับจัดกลุ่มช่องกรอกข้อมูลและป้ายกำกับ
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(pady=10)

# ส่วนของช่องกรอกองศาเซลเซียส
celsius_label = ttk.Label(input_frame, text="องศาเซลเซียส")
celsius_label.pack(side="left", padx=(0, 10))

celsius_entry = ttk.Entry(input_frame, width=8)
celsius_entry.pack(side="left")

# ป้ายข้อความลูกศรเพื่อแสดงทิศทางการแปลง
arrow_label = ttk.Label(input_frame, text=">>>>>>>>>", font=("Tahoma", 16))
arrow_label.pack(side="left", padx=10)

# ส่วนของช่องแสดงผลองศาฟาเรนไฮต์
fahrenheit_label = ttk.Label(input_frame, text="องศาฟาเรนไฮต์")
fahrenheit_label.pack(side="left", padx=(10, 0))

fahrenheit_entry = ttk.Entry(input_frame, width=8)
fahrenheit_entry.pack(side="left")

# สร้างกรอบ (Frame) สำหรับปุ่ม Convert และ Exit
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(pady=20)

# ปุ่ม "Convert" สำหรับเรียกใช้ฟังก์ชัน convert_temperature
convert_button = ttk.Button(button_frame, text="คำนวณ", command=convert_temperature)
convert_button.pack(side="left", padx=20, ipadx=10, ipady=5)

# ปุ่ม "Exit" สำหรับปิดโปรแกรม
exit_button = ttk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side="left", padx=20, ipadx=10, ipady=5)

# เริ่มการทำงานของ GUI
root.mainloop()