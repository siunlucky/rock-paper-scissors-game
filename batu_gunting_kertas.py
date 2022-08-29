from ast import If
from cmath import inf
import random

user_wins = 0
computer_wins = 0
draw = 0
options = ["batu" , "gunting", "kertas"]

while True:
    user_input = input("Masukkan Gunting/Batu/Kertas atau q untuk keluar q: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # 0 = batu, 1 = gunting, 2 = kertas
    computer_pick = options[random_number]
    print("Computer memilih", computer_pick + ".")
    
    if user_input == "batu" and computer_pick == "gunting":
        user_wins += 1
        print("Kamu Menang")
        continue
    
    elif user_input == "gunting" and computer_pick == "kertas":
        user_wins += 1
        print("Kamu Menang")
        continue
    
    elif user_input == "kertas" and computer_pick == "batu":
        user_wins += 1
        print("Kamu Menang")
        continue
    
    elif user_input == computer_pick:
        draw += 1
        print("Draw")
        continue
    
    else:
        computer_wins += 1
        print("Kamu Kalah")
        continue
    
    
print("Kamu Menang Sebanyak" , user_wins, "kali")
print("Computer Menang Sebanyak" , computer_wins, "kali")
print("Kalian Draw Sebanyak" , draw, "kali")
print("GoodBye!!")