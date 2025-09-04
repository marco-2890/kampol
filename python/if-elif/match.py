from calendar import Day


match Day:
    case "Monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday!")
    case "Wednesday":
        print("It's Wednesday!")
    case "Thursday":
        print("It's Thursday!")
    case "Friday":
        print("It's Friday!")
    case "Saturday":
        print("It's Saturday!")     
    case "Sunday":
        print("It's Sunday!")
    case _:
        print("Invalid day!")