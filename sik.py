import random

# مصفوفة تمثل لوحة اللعبة
board = ["عيدان"] * 7

# اللاعبين (يمكن تغيير الأسماء)
players = ["لاعب 1", "لاعب 2", "لاعب 3", "لاعب 4"]

# تابع لطباعة لوحة اللعبة
def print_board():
    print(" | ".join(board))

# تابع للتحقق من الفوز
def check_win():
    # قم بتحقق من الفوز بناءً على قواعد اللعبة
    # يمكنك تخصيص هذا الجزء حسب قواعد السيك الموريتانية
    # مثلاً، يمكنك التحقق من تكوين خط أفقي أو عمودي أو قطري
    pass

# تابع للعب اللعبة
def play_game():
    global board  # Declare board as a global variable
    current_player_index = 0
    while True:
        current_player = players[current_player_index]
        print_board()
        input(f"{current_player}، اضغط على Enter لرمي العيدان...")
        result = random.choice(board)
        print(f"{current_player} ألقى: {result}")
        if result == "حمار":
            print(f"{current_player} خسر كل ما أتى به.")
            board = ["عيدان"] * 7
        else:
            board.remove(result)
        if check_win():
            print_board()
            print(f"تهانينا، {current_player}! لقد فازت.")
            break
        current_player_index = (current_player_index + 1) % len(players)

# ابدأ اللعبة
if __name__ == "__main__":
    play_game()
