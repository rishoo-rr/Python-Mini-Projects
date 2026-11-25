#                                          (number guessing game)
import random
print("="*39)
print("    🎯🎯 number guessing game 🎯🎯")
print("="*39)
print("you have 7 chances to guess the number.")
print("-"*39)
print("Let's play the number guessing game.")
print("🚀🚀🚀🤩🤩")
print("="*39)
life = "💖💖💖💖💖💖💖"
print(life)
secret_num = random.randint(1 ,100)


while True :
    num = (input("guess the num-->> "))
    if not num.isdigit():
        print(" ❌wrong input ! please enter a vailid numbert (1-100).")
        continue 
    num = int(num)

    if num == secret_num:   
        print("="*40)
        print(f"right guess✅🥳🎉\nnumber is : {secret_num}")
        print("-"*40)
        break

    elif (num > secret_num):
        life = life.replace("💖","",1)
        print("Lower ⬇️")
        if life != "":
            print("-"*20)
            print(life)

    elif (num < secret_num):
        life = life.replace("💖","",1)
        print("higher ⬆️")
        if life != "":
            print("-"*20)
            print(life)
             
    if life == "":
        print("🟰"*39)
        print("Sorry, you don’t have any life left.")
        print(f"{"-"*39}\nnumber is : {secret_num}\n{"-"*39}")
        print("you loser : 🤡🤡🤡🤡🤡🤡🤡\n          😂😂😂😂😂😂😂")
        print("-"*39)
        break
