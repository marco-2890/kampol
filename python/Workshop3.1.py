import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับแปลงค่า Celsius → Fahrenheit
def convert():
    try:
        # 1. อ่านค่าจากช่องกรอก (Entry) txtCelsius
        celsius = float(txtCelsius.get())

        # 2. คำนวณโดยใช้สูตร
        #    Fahrenheit = (Celsius * 9/5) + 32
        fahrenheit = (celsius * 9/5) + 32

        # 3. แสดงผลลัพธ์ในช่อง txtFahrenheit
        txtFahrenheit.delete(0, tk.END)  # ลบค่าที่มีอยู่ก่อน
        txtFahrenheit.insert(0, str(round(fahrenheit, 2)))  # แสดงผล (ปัดทศนิยม 2 หลัก)
    except:
        # ถ้าไม่สามารถแปลงเป็นตัวเลขได้
        messagebox.showerror("Error", "กรุณากรอกค่าเป็นตัวเลข!")

# ฟังก์ชันสำหรับออกจากโปรแกรม
def exit_program():
    root.destroy()

# ----------------- ส่วนสร้างหน้าต่าง GUI -----------------
root = tk.Tk()
root.title("Workshop 3.1 โปรแกรมแปลงองศาเซลเซียสเป็นองศาฟาเรนไฮต์")
root.geometry("500x200")  # กำหนดขนาดหน้าต่าง

# Label หัวข้อ
lblTitle = tk.Label(root, text="โปรแกรมแปลงองศาเซลเซียสเป็นองศาฟาเรนไฮต์", fg="blue", font=("Tahoma", 14))
lblTitle.pack(pady=10)

# Frame สำหรับเก็บช่องกรอกข้อมูล
frame = tk.Frame(root)
frame.pack(pady=10)

# Label และช่องกรอก Celsius
lblCelsius = tk.Label(frame, text="องศาเซลเซียส", font=("Tahoma", 12))
lblCelsius.grid(row=0, column=0, padx=5, pady=5)

txtCelsius = tk.Entry(frame, font=("Tahoma", 12), width=10)
txtCelsius.grid(row=0, column=1, padx=5, pady=5)

# เครื่องหมาย >>>>>
lblArrow = tk.Label(frame, text=" >>>>>> ", font=("Tahoma", 12))
lblArrow.grid(row=0, column=2)

# Label และช่องกรอก Fahrenheit
lblFahrenheit = tk.Label(frame, text="องศาฟาเรนไฮต์", font=("Tahoma", 12))
lblFahrenheit.grid(row=0, column=3, padx=5, pady=5)

txtFahrenheit = tk.Entry(frame, font=("Tahoma", 12), width=10)
txtFahrenheit.grid(row=0, column=4, padx=5, pady=5)

# ปุ่ม Convert
btnConvert = tk.Button(root, text="Convert", font=("Tahoma", 12), command=convert)
btnConvert.pack(side=tk.LEFT, padx=50, pady=20)

# ปุ่ม Exit
btnExit = tk.Button(root, text="Exit", font=("Tahoma", 12), command=exit_program)
btnExit.pack(side=tk.RIGHT, padx=50, pady=20)

# รันโปรแกรม
root.mainloop()
