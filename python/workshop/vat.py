import tkinter as tk
from tkinter import ttk, messagebox

# ฟังก์ชันสำหรับคำนวณ VAT
def calculate_vat(is_vat_included):
    """
    คำนวณ VAT และอัปเดตค่าที่แสดงบนหน้าจอ
    :param is_vat_included: True ถ้าเป็นการคำนวณแบบ Vat ใน, False ถ้าเป็นการคำนวณแบบ Vat นอก
    """
    try:
        price = float(price_entry.get())
        vat_rate = 0.07
        
        if is_vat_included:  # Vat ใน (ภาษีรวมในราคาแล้ว)
            final_price = price
            price_before_vat = final_price / (1 + vat_rate)
            vat_amount = final_price - price_before_vat
        else:  # Vat นอก (ภาษีไม่ได้รวมในราคา)
            price_before_vat = price
            vat_amount = price_before_vat * vat_rate
            final_price = price_before_vat + vat_amount

        # อัปเดตข้อความบนป้ายแสดงผล
        price_label.config(text=f"ราคาสินค้า (ไม่รวม Vat) : {price_before_vat:,.2f}")
        vat_label.config(text=f"Vat : {vat_amount:,.2f}")
        total_price_label.config(text=f"ราคาสินค้า (รวม Vat) : {final_price:,.2f}")

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้องในช่องราคาสินค้า")
    except Exception as e:
        messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {e}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Form1")
root.geometry("400x350")
root.resizable(False, False)

# ตั้งค่าสไตล์
style = ttk.Style()
style.configure("TLabel", foreground="blue", font=("Tahoma", 16))
style.configure("TButton", font=("Tahoma", 14))

# ส่วนของช่องกรอกราคา
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(pady=15)

price_label_text = ttk.Label(input_frame, text="ราคาสินค้า", foreground="black", font=("Tahoma", 16))
price_label_text.pack(side="left", padx=(0, 10))

price_entry = ttk.Entry(input_frame, width=15, font=("Tahoma", 14))
price_entry.pack(side="left")

# ส่วนของปุ่ม "Vat นอก" และ "Vat ใน"
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(pady=5)

vat_outside_button = ttk.Button(button_frame, text="Vat นอก", command=lambda: calculate_vat(False))
vat_outside_button.pack(side="left", padx=10)

vat_inside_button = ttk.Button(button_frame, text="Vat ใน", command=lambda: calculate_vat(True))
vat_inside_button.pack(side="left", padx=10)

# ส่วนของป้ายแสดงผลลัพธ์
result_frame = ttk.Frame(root, padding=10)
result_frame.pack(pady=10)

price_label = ttk.Label(result_frame, text="ราคาสินค้า (ไม่รวม Vat) : 0.00")
price_label.pack(anchor="w", pady=5)

vat_label = ttk.Label(result_frame, text="Vat : 0.00")
vat_label.pack(anchor="w", pady=5)

total_price_label = ttk.Label(result_frame, text="ราคาสินค้า (รวม Vat) : 0.00")
total_price_label.pack(anchor="w", pady=5)

# ส่วนของปุ่ม "Exit"
exit_button_frame = ttk.Frame(root, padding=(0, 20))
exit_button_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

exit_button = ttk.Button(exit_button_frame, text="Exit", command=root.quit)
exit_button.pack()

# เริ่มการทำงานของ GUI
root.mainloop()