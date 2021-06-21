import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
#df = pd.read_csv('parkinglot.csv')
#df1 = pd.read_csv('parkinglot1.csv')
#df2=pd.read_csv('parkinglot_transaction.csv')
df = pd.read_json('parkinglot.json')
df1 = pd.read_json('parkinglot1.json')
df2=pd.read_json('parkinglot_transaction.json')
df3=pd.read_json('test1.json')

def  write_json(data,filename='test1.json'):
    with open(filename,"w") as f:
        json.dump(data,f)

def goto(linenum):
    global line
    line = linenum

def checkifempty(spot_no):
    if df.loc[spot_no-1,'CarType']=='Na' and df.loc[spot_no-1,'Numberplate']=='Na':
        print("Your spot is free")
        catalyst1=1
    else:
        print("your spot is occupied")
        catalyst1=0
    return catalyst1


def car_input():
    cartype=input("Enter the car type ")
    carnumber=input("Enter the car plate number ")
    return cartype,carnumber 

def clearValues():
    print("please pay 10 dollars")
    [cartype,carnumber] = df.loc[spot_no-1,['CarType','Numberplate']]
    df.loc[spot_no-1,['CarType','Numberplate']] = ['Na','Na']
    cost=df2.loc[spot_no-1,['transaction']]+10
    df1.loc[spot_no-1,['Status']] = ['free']
    df2.loc[spot_no-1,['transaction']] = [cost]
    time=date()
    #dict1={"Time": time, "Spot": spot_no, "Reservation Status": "free", "Car Information": cartype+' '+carnumber, "Revenue": 10}
    with open('test1.json') as file:
        data=json.load(file)
        temp=data["data"]
        entry={"Time": time, "Spot": spot_no, "Reservation Status": "free", "Car Information": cartype+' '+carnumber, "Revenue": 10}
        temp.append(entry)
    write_json(data)
    
    df.to_json("parkinglot.json")
    df1.to_json("parkinglot1.json") 
    df2.to_json("parkinglot_transaction.json")
   

def updateValues():
    df.loc[spot_no-1,['CarType','Numberplate']] = [cartype,carnumber]
    count_of_cars=df2.loc[spot_no-1,['number_of_times_parked']]+1
    df1.loc[spot_no-1,['Status']] = ['occupied']
    df2.loc[spot_no-1,['number_of_times_parked']] = [count_of_cars]
    time=date()
    #dict1={"Time": time, "Spot": spot_no, "Reservation Status": "occupied", "Car Information": cartype+' '+carnumber, "Revenue": 0}
    with open('test1.json') as file:
        data=json.load(file)
        temp=data["data"]
        entry={"Time": time, "Spot": spot_no, "Reservation Status": "occupied", "Car Information": cartype+' '+carnumber, "Revenue": 0}
        temp.append(entry)
    write_json(data)
    df.to_json("parkinglot.json")
    df1.to_json("parkinglot1.json")
    df2.to_json("parkinglot_transaction.json")
    
    

def freeSpots(free_list):
    free_list=[]
    #print("The free spots are: ")
    for row in range(10):
        if df.loc[row,'CarType']=='Na' and df.loc[row,'Numberplate']=='Na':
            free_spots=df.loc[row,'spots']
            free_spots_no=df.loc[row,'s.no']
            free_list.append(free_spots_no)
            #print(free_spots)
    return(free_list)

def reserved_spots(Reserved_list):
    Reserved_list=[]
    #print("The reserved spots are: ")
    for row in range(10):
        if df.loc[row,'CarType']!='Na' and df.loc[row,'Numberplate']!='Na':
            reserved_spots=df.loc[row,'spots']
            reserved_spots_no=df.loc[row,'s.no']
            Reserved_list.append(reserved_spots_no)
            #print(reserved_spots)
    return(Reserved_list)

def reserved_spots_print():
    print("The reserved spots are: ")
    for row in range(10):
        if df.loc[row,'CarType']!='Na' and df.loc[row,'Numberplate']!='Na':
            reserved_spots=df.loc[row,'spots']
            Reserved_list.append(reserved_spots)
            print(reserved_spots)
    return Reserved_list

def free_spots_print():
    print("The free spots are: ")
    for row in range(10):
        if df.loc[row,'CarType']=='Na' and df.loc[row,'Numberplate']=='Na':
            free_spots=df.loc[row,'spots']
            print(free_spots)

def mainmenu():
    print ("""
        Main Menu
        1.Reserve
        2.Unreserve
        3.Find your car
        4.Data Management
        5.Map of the parking lot
        6.Quit
          """)

def mainmenu2():
    print ("""
        Data
        1.Free spots
        2.Reserved spots
        3.Total number of cars inside the parking lot
        4.total transaction done
        5.Analysis graph of Transaction
        6.back to main menu
          """)


def find_car_input():
    findnumber=input("Enter the car plate number ")
    return findnumber

def find_car(findnumber):
    index=df[df['Numberplate']==findnumber].index.values
    return index

def graph():
    df2=pd.read_json('parkinglot_transaction.json')
    spot = df2['spot']
    price = df2['transaction']
    fig = plt.figure(figsize =(16, 9))
    plt.bar(spot, price)
    plt.xlabel("Spots")
    plt.ylabel("Revenue")
    plt.title("Transaction")
    plt.show()

def date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

global spot_no
Reserved_list=[]
free_list=[]

line=0
while True:
    if line==0:
        mainmenu()
        user_input1=input("Enter the corresponding option of the action u would like to do : ")
        try:
            menuoption = int(user_input1)
        except ValueError:
            print("That's not an int!")
            goto(0)
            continue

        if menuoption>=1 and menuoption<=6:        
            goto(menuoption)
        else:
            print("Invalid menu option.")
            goto(0)
            continue

    elif line ==1:
        free_list=freeSpots(free_list)
        user_input2=input("Enter the spot number u want to reserve: in the range 1 to 10:")
        try:
            spot_no = int(user_input2)
        except ValueError:
            print("That's not an int!")
            goto(1)
            continue

        if (spot_no in free_list):
            goto(7)
        else:
            print("That spot is occupied. Please enter another spot number.")
            user_input6=input("do u want the list of free spots? (y/n)")
            if user_input6=='n':
                goto(1)
                continue
            else:
                free_spots_print()
                goto(1)
                continue

    elif line==2:
        Reserved_list=reserved_spots(Reserved_list)
        user_input3=input("Enter the spot number u want to unreserve: ")
        try:
            spot_no = int(user_input3)
        except ValueError:
            print("That's not an int!")
            goto(2)
            continue

        if (spot_no in Reserved_list):
            goto(7)
        else:
            print("please enter the correct spot number.")
            user_input5=input("do u want the list of reserved spots? (y/n)")
            if user_input5=='n':
                goto(2)
                continue
            else:
                reserved_spots_print()
                goto(2)
                continue

    elif line==3:
        findnumber = find_car_input()
        index=find_car(findnumber)
        #Foundspot=df.loc[index, 's.no']
        if index.size>0:
            print("your car is parked in the spot ",index+1)
            goto(0)
            continue
        else:
            print("your car is not parked.")
            goto(0)
            continue
    
    elif line==4:
        mainmenu2()
        user_input4=input("Enter the corresponding option of the action u would like to do : ")
        try:
            menuoption2 = int(user_input4)
        except ValueError:
            print("That's not an int!")
            goto(4)
            continue

        menuoption_2=menuoption2+7

        if menuoption_2>=8 and menuoption_2<=13:        
            goto(menuoption_2)
        else:
            print("Invalid menu option.")
            goto(4)
            continue
        

    elif line==5:
        print("The map of the parking lot:")
        print(df1)
        goto(0)
        continue
    
    elif line==6:
        goto(14)
        continue

    elif line==7:
        catalyst1 = checkifempty(spot_no)
        if bool(catalyst1)==True:
            cartype , carnumber = car_input()
            updateValues()
            print("Process successful")
            goto(0)
            continue
        else:
            clearOption=input("Do you want to unoccupy? \npress y for yes and n for no ")
            if clearOption=='n':
                print("Thank you")
                goto(0)
                continue
            else:
                clearValues()
                print("Process successful")
                goto(0)
                continue

    elif line==8:
        free_spots_print()
        goto(4)
        continue
    
    elif line==9:
        reserved_spots_print()
        goto(4)
        continue

    elif line==10:
        Reserved_list=reserved_spots(Reserved_list)
        print("The number of cars inside the parking lot = ",len(Reserved_list))
        goto(4)
        continue
    
    elif line==11:
        print(df2[['spot', 'transaction']])
        total = df2['transaction'].sum() 
        print("The total transaction = ",total)
        goto(4)
        continue

    elif line==12:
        graph()
        goto(4)
        continue

    elif line==13:
        goto(0)
        continue

    elif line==14:
        print("quitting program.")
        break
    
    else:
        print("quitting program.")
        break