#            (Student Report Card generator)   
print("="*26)
print("  STUDENT REPORT MANAGER ")
print("="*26)
print("1. Add student\n2. View report card")
print("3. View one student report card.")
print("="*26)   
def stu_rep():

    choice = (input("Apni choice chune 1/2/3 : ")) 
    print("-"*26)   
    if choice == "1":
        while True:  
            name = input("enter your name : ")
            while True:
                roll = input("enter your roll num : ")
                if roll.isdigit():
                    break

                
                print("❌ Invailid input ! please enter a vailid number.")
            def check(subject):
                while True:          
                    mark = input(f"enter your {subject} mark : ")
                    if mark.isdigit():
                        return int(mark)
                    print("❌ Invailid input ! please enter a vailid number.")

            phy_m = check("phy")
            chem_m = check("chem")
            math_m = check("math")

            print("-"*26)
            percentage = (phy_m + chem_m + math_m)//3
            spaces = " " * (len(name) + 1)
            if percentage < 33:   
                grade = "Fail"
            elif percentage < 50:
                grade = "D"
            elif percentage < 70:
                grade = "C"
            elif   percentage < 90:
                grade = "B"  
            else:
                grade = "A+"

            with open("student.txt","a+") as f: 
                f.write(f"{'-'*25}\n")
                f.write(f"{name}_\n")
                f.write(f"{spaces}roll : {roll}\n")
                f.write(f"{spaces}phy_m : {phy_m}\n")
                f.write(f"{spaces}chem_m : {chem_m}\n")
                f.write(f"{spaces}math_m : {math_m}\n")
                f.write(f"{spaces}percentage : {percentage}%\n")
                f.write(f"{spaces}Grade : {grade}\n")

            print("Data saved successfully.✅")
            print("-"*26)     
            while True:
                yes_or_no = input("Do you want to save more data ?? (Yes/no) : ").lower()
                print("-"*48)
                if yes_or_no == "yes":
                    break
                elif yes_or_no== "no":
                    break 
                else: 
                    print("please write yes or no only.")
            if yes_or_no == "no":
                break  


    elif choice == "2":        
        with open("student.txt","a+") as f:
            f.seek(0)     
            data = f.read()
            if data != "":
                print(" ====APNA REPORT CARD====")
                print(data)
            else:
                print("Your file is empty.🫗 🫗")
                print("-"*26)


    elif choice == "3":
        with open("student.txt", "a+") as f:
            f.seek(0)
            data = f.read()
            if data != "":
                f.seek(0)
                name = input(("enter your name : ").lower()).strip() 
                if name in data:

                    print("="*26)
                    lines = f.readlines()
                    for line_n,line in enumerate(lines):
                        if name in line:    
                            start = line_n - 1
                            end = line_n + 7

                            print(f" Report card of {name}📃")
                            for i in range(start,end):
                                print(lines[i],end = "")
                            break

                else:
                    print("❌ Not in the report card.") 
            else:
                print("Your file is empty.🫗 🫗")
                print("-"*26)
    else:
        print("please write integer 1,2 or 3 only.")
        stu_rep()
stu_rep()
