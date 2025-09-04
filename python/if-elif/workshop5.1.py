score = int(input("คะแนนเกรด (0-100): "))

if score < 0 or score > 100:
    print("คะแนนไม่ถูกต้อง, กรุณาลองใหม่.")
else:
    if score >= 80 and score <= 100:
        print("เกรด A")
    elif score >= 75 and score <= 79:
        print("เกรด B+")
    elif score >= 70 and score <= 74:
        print("เกรด B")
    elif score >= 65 and score <= 69:
        print("เกรด C+")
    elif score >= 60 and score <= 64:
        print("เกรด C")
    elif score >= 55 and score <= 59:
        print("เกรด D+")
    elif score >= 50 and score <= 54:
        print("เกรด D")
    else:
        print("เกรด E")

    print("จบการทำงาน")
