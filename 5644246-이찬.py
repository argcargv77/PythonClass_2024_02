import random

def up_down_game():
    secret_number = random.randint(1, 99)
    attempts = 5
    print("업다운 숫자 맞추기 게임에 오신 것을 환영합니다!")
    
    for attempt in range(attempts):
        guess = int(input(f"추측 {attempt + 1}: 추측한 수를 입력하세요(1~99): "))
        if guess > secret_number:
            print("너무 높습니다. DOWN!")
        elif guess < secret_number:
            print("너무 낮습니다. UP!")
        else:
            print("축하합니다! 정답을 맞히셨습니다.")
            return

    print(f"죄송합니다. 모든 기회를 사용하셨습니다. 정답은 {secret_number}였습니다.")

def rock_paper_scissors_game():
    options = {1: "가위", 2: "바위", 3: "보"}
    print("가위바위보 게임에 오신 것을 환영합니다!")
    
    while True:
        computer_choice = random.randint(1, 3)
        user_choice = int(input("선택 항목 입력(1: 가위, 2: 바위, 3: 종이, 4: 종료): "))
        
        if user_choice == 4:
            print("게임을 종료합니다. 플레이해 주셔서 감사합니다.")
            break
        
        if user_choice not in options:
            print("잘못된 선택입니다. 다시 선택해 주세요.")
            continue

        print(f"YOU : {options[user_choice]}, COMPUTER : {options[computer_choice]}.")

        if user_choice == computer_choice:
            print("비겼습니다!")
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")

def generate_lotto_numbers():
    print("로또 번호 생성 중...")
    for _ in range(5):
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()
        print(lotto_numbers)

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Up Down 숫자 맞추기 게임")
        print("2. 가위 바위 보 게임")
        print("3. 로또 번호 생성하기")
        print("4. Exit")

        choice = int(input("Select an option (1-4): "))
        
        if choice == 1:
            up_down_game()
        elif choice == 2:
            rock_paper_scissors_game()
        elif choice == 3:
            generate_lotto_numbers()
        elif choice == 4:
            print("프로그램 종료. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()
