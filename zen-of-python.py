def main():
    math = int(input("請輸入數學成積"))
    ispass(math)
    en = int(input("請輸入英文成積"))
    ispass(en)
    ch = int(input("請輸入國文成積"))
    ispass(ch)

    sum = math + en + ch
    average = sum/3
    print("總成績",average)
    ispass(average)



def ispass(score):
    if score>=60
        print("及格")
        return True
    elif score <60
        print("不及格")
        return False

main()


