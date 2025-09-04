import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณราคาก่อน VAT
def calculate():
    try:
        sum_price = float(entry_sum_price.get())
        price = sum_price / 1.07
        entry_price.delete(0, tk.END)
        entry_price.insert(0, f"{price:.2f}")  # ปัดทศนิยม 2 หลัก
    except:
        messagebox.showerror("Error", "กรุณากรอกราคาที่เป็นตัวเลข!")

# ฟังก์ชันออกจากโปรแกรม
def exit_program():
    root.destroy()

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("คำนวณราคาสินค้าก่อน VAT 7%")
root.geometry("450x350")

# Label สำหรับราคาหลัง VAT
lbl_sum_price = tk.Label(root, text="กรอกราคาสินค้าหลังรวม VAT 7%:", font=("Tahoma", 12))
lbl_sum_price.pack(pady=5)

# Entry สำหรับราคาหลัง VAT
entry_sum_price = tk.Entry(root, font=("Tahoma", 12), width=20)
entry_sum_price.pack(pady=5)

# Label สำหรับผลลัพธ์
lbl_price = tk.Label(root, text="ราคาสินค้าก่อนรวม VAT 7%:", font=("Tahoma", 12))
lbl_price.pack(pady=5)

# Entry สำหรับแสดงผลลัพธ์ (ราคาก่อน VAT)
entry_price = tk.Entry(root, font=("Tahoma", 12), width=20)
entry_price.pack(pady=5)

# ปุ่มคำนวณและออก
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="คำนวณ", font=("Tahoma", 12), command=calculate)
btn_calculate.grid(row=0, column=0, padx=10)

btn_exit = tk.Button(frame_buttons, text="ออก", font=("Tahoma", 12), command=exit_program)
btn_exit.grid(row=0, column=1, padx=10)

root.mainloop()
