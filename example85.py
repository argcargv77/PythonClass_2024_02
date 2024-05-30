while True:
    print("1.New, 2.Load, 3.Save, 4.Exit")
    menu = input("번호 입력 : ")
    if menu == "1":
        print("new");
    elif menu == "2":
        print("Load");
    elif menu == "3":
        print("Save");
    elif menu == "4":
        answer = input("정말로 종료할까요 (y/n) ? ")
        if answer.lower()[0] == "y":
            break



        
