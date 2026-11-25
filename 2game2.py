#                (name guessing game)    
import random
word = [
    "Aarav", "Aarti", "Aman", "Ananya", "Amit", 
    "Anjali", "Arjun", "Bhavna", "Akash", "Chhavi", 
    "Dev", "Diya", "Deepak", "Divya", "Ishan", 
    "Isha", "Kabir", "Jyoti", "Kunal", "Kavita", 
    "Manav", "Khushi", "Nitin", "Megha", "Rahul", 
    "Neha", "Rohit", "Pooja", "Rohan", "Priya", 
    "Sachin", "Riya", "Sahil", "Ritu", "Sameer", 
    "Sakshi", "Sanjay", "Shalini", "Vicky", "Shruti", 
    "Vivek", "Sneha", "Yash", "Swati", "Vijay", 
    "Tanvi", "Ravi", "Tanya", "Sonu", "Kiran","rishabh",
    "nitesh","ruhi","hiru","ruhani","sunaina", "rishoo",
    "prabhakar","javani","nikita","nikki","aryan",
    "bobby","dhirendra","jay","raju","sachin"
]
print("="*35)
print("   🎯🎯 name guessing game 🎯🎯        ")
print("="*35)
print("""rule : Even if you write the wrong
      letter, you will get 10
      chances to guess the name.""")
print("-"*35)
print("Let's play the name guessing game.")
print(f"🚀🚀🚀🤩🤩\n{'='*35}")
life = "💖💖💖💖💖💖💖💖💖💖"


print(life)
s_word = (random.choice(word)).lower()
hidden = (list(len(s_word)*"_"))
print(hidden)

while True:
    guess = input("enter your letter : ").lower()
    if guess == s_word:
        print("="*30)
        print(f"right guess✅🥳🎉\nname is : {s_word}") 
        print("="*30)
        break

    elif guess in s_word:
        for i in range(len(s_word)):
            if s_word[i] == guess:
                hidden[i] = guess  
        print(hidden)
        print("="*30)
        if hidden == list(s_word):  
            print("="*21)
            print(f"right guess✅🥳🎉\nname is : {s_word}") 
            print("="*21)
            break

    else:
        life = life.replace("💖","",1)
        print("not in the name ❌ .")
        if life != "":
            print("-"*21)
            print(life)
        if life == "":
            print("="*32)
            print("Sorry, you don’t have any life left.")
            print("       🔍🔍🔍")
            print(f"{"-"*32}\nname is : {s_word}\n{"-"*32}")
            print("you loser : 🤡🤡🤡🤡🤡🤡🤡")
            print(f"            😂😂😂😂😂😂😂\n{"="*32}")
            break