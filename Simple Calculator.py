#Create Variables
Option=0
Num=0
Count=0
Decision=0
Avg=0
Low=0
High=0
Temp=0
Value=0

#Create Lists of Variables
List=[]
EvenNumber=[]

#Print the main menu
print('''
                WOUNDER CALCULATOR
                ==================
                
                    Main Menu

            1.Enter positive integer number
            2.Display Highest value
            3.Display Lowest value
            4.Display Average value
            5.Display Even numbers

            6.Exit

            ''')

#Input
Option=int(input("Please indicate your option:"))
if(Option==1):
    Num=int(input("How many numbers do you want to input?"))
    if(Num<11):
        Count=Num  
    else:print("Error! we can't continue our programmed,PLEASE CHECK PROPERLY")
else:print("Error! we can't continue our programmed,PLEASE DON'T INPUT MORE THAN 10")

while(Count>=1):
    Value=int(input("Enter a number"))
    List.append(Value)
    Count=Count-1
    if(Value>0):
        for Value in List:
            if (Value>High):
                High=Value
                Temp=High
             
        for Value in List:
            if(Value<Temp):
                Low=Value
                Temp=Low
             
        if(Value%2==0):
            EvenNumber.append(Value)

        Avg=Avg+(Value/Num)
        

    else:print("Error!,PLEASE INPUT ONLY POSTIVE INTEGERS")

Decision=str(input("Do you want to continue this further?(YES/NO)..."))
while(Decision=="YES"):
    Option=int(input("Please indicate your option"))
    if(Option==1):
        print("Error!Please recheck ,If you want to enter numbers,RESTART")
    if(Option==2):
        print("The Highest Value is...",High)
    if(Option==3):
        print("The Lowest Value is...",Low)
    if(Option==4):
        print("The Average is...",Avg)
    if(Option==5):
        print("The Even Number is...",EvenNumber)
    if(Option==6):
        print("THANK YOU! & Come Again")
        exit()
    if(Option>6):
        print("Error! Wrong Inputs,PLEASE INPUT ONLY 1 - 10 NUMBERS")
    Decision=str(input("Do you want to continue this further?(YES/NO)..."))
else:exit()
