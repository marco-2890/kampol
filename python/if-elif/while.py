# t =int(input("Enter a number: "))
# i=1
# while i <=5:
#     print("Hello",i)

#     i += 1

while True:
    num =int(input("ป้อนตัวเลข: (0 หยุด) "))
    if num < 0:
        print("ทางลบไม่อนุญาต, กรุณาลองใหม่.")
        continue
    elif num == 0:
        print("จบการทำงาน")
        exit()
        continue
