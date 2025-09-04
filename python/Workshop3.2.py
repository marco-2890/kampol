import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันแปลง Celsius → Fahrenheit
def c_to_f():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลข")

# ฟังก์ชันแปลง Fahrenheit → Celsius
def f_to_c():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f} °F = {celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลข")

# ====== ส่วนของ GUI ======
root = tk.Tk()
root.title("โปรแกรมแปลงอุณหภูมิ")

# ช่องกรอกค่า
tk.Label(root, text="กรอกค่าอุณหภูมิ:").pack(pady=5)
entry = tk.Entry(root, width=15, font=("Arial", 14))
entry.pack(pady=5)

# ปุ่มแปลงค่า
tk.Button(root, text="Celsius ➝ Fahrenheit", command=c_to_f).pack(pady=5)
tk.Button(root, text="Fahrenheit ➝ Celsius", command=f_to_c).pack(pady=5)

# แสดงผลลัพธ์
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()
