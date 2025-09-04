import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณ VAT
def calculate():
    try:
        product = float(entry_product.get())
        vat = product * 7 / 100
        total = product + vat
        # แสดงผลแบบปัดทศนิยม 2 ตำแหน่ง
        entry_vat.delete(0, tk.END)
        entry_vat.insert(0, f"{vat:.2f}")
        entry_total.delete(0, tk.END)
        entry_total.insert(0, f"{total:.2f}")
    except:
        messagebox.showerror("Error", "กรุณากรอกราคาที่เป็นตัวเลข!")

# ฟังก์ชันออกจากโปรแกรม
def exit_program():
    root.destroy()

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("คำนวณ VAT 7%")
root.geometry("450x350")

# Label และ Entry สำหรับราคาสินค้าก่อน VAT
lbl_product = tk.Label(root, text="กรอกราคาสินค้าก่อนรวม VAT 7%:", font=("Tahoma", 12))
lbl_product.pack(pady=5)
entry_product = tk.Entry(root, font=("Tahoma", 12), width=20)
entry_product.pack(pady=5)

# Label และ Entry สำหรับ VAT
lbl_vat = tk.Label(root, text="VAT 7%:", font=("Tahoma", 12))
lbl_vat.pack(pady=5)
entry_vat = tk.Entry(root, font=("Tahoma", 12), width=20)
entry_vat.pack(pady=5)

# Label และ Entry สำหรับราคาหลังรวม VAT
lbl_total = tk.Label(root, text="ราคาสินค้าหลังรวม VAT 7%:", font=("Tahoma", 12))
lbl_total.pack(pady=5)
entry_total = tk.Entry(root, font=("Tahoma", 12), width=20)
entry_total.pack(pady=5)

# ปุ่มคำนวณและออก
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="คำนวณ", font=("Tahoma", 12), command=calculate)
btn_calculate.grid(row=0, column=0, padx=10)

btn_exit = tk.Button(frame_buttons, text="ออก", font=("Tahoma", 12), command=exit_program)
btn_exit.grid(row=0, column=1, padx=10)

root.mainloop()
