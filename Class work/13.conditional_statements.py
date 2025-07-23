'''if-elif 
1)
hr,mins=list(map(int,input("Enter the time:").split(':')))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print("Time to sleep")
    elif hr>=4 and hr<12:
        print("Good morning")
    elif hr>=12 and hr<16:
        print("Good afternoon")
    elif hr>=16 and hr<20:
        print("Good evening")
    elif hr>=20 and hr<24:
        print("Good night")
else:
    print("Enter the proper time")

#2)
seats={
    'L1':True,
    'L2':False,
    'L3':False,
    'L4':True,
    'L5':True
    }
seatno=input("Enter the seat number:")
if seatno in seats:
    if seats[seatno]:
        print("Already seat is booked")
    else:
        print("Seat is availabale. Hurry up")
else:
    print("Enter the correct seat number")

#3)
data={
    'watches':{'discount':10,'brands':['titan','fasttrack']},
    'facewash':{'discount':30,'brands':['biotique','clean&clear']},
    'tops':{'discount':16,'brands':['h&m','zara']},
    'heels':{'discount':25,'brands':['bata','paragon']}
}

print(data.keys())
pro = input("Enter the category: ")

if pro in data:
    print(f"{data[pro]['discount']}% discount is available on these brands: {data[pro]['brands']}")
else:
    print(f"Product is out of stock. Check on the other products: {data}")

#4)
movie_list={
    'salaar':{'kids':True},
    'darling':{"kids":True},
    'masudha':{'kids':False},
    'Arjunreddy':{'kids':False}
}
print("Welcome to hotstar".center(30,"*"))
movies=input("Enter the movie:").title()
if movies in movie_list:
    if movie_list[movies]['kids']:
        print("You can watch with your family {movies}")
    else:
        print("{movies} Movie is an adult movie")
else:
    print("Movie is not available")

#for loop
1)
seats={
    "U1":{'price':1030,'booking_status':True},
    "U2":{'price':1030,'booking_status':False},
    "U3":{'price':1030,'booking_status':False},
    "U4":{'price':1030,'booking_status':True},
    "U5":{'price':1030,'booking_status':False},
    "L1":{'price':1030,'booking_status':True},
    "L2":{'price':1030,'booking_status':False},
    "L3":{'price':1030,'booking_status':False},
    "L4":{'price':1030,'booking_status':True},
    "L5":{'price':1030,'booking_status':False}
}
for i in seats:
    if seats[i]['booking_status']:
        print(f'***{i}***')
    else:
        print(f'{i}-{seats[i]["price"]}')
seatno=input("Enter the seatno: ").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print(f'{seatno} is booked. Go for another one.')
    else:
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        gender=input("Enter gender: ").upper
        if age<=5:
            print(f'Hello {name} your booking is succesfull with free of cost')
        elif age<15:
            print(f'Hello {name} your booking is succesfull with 50% discount\nTotal amount={seats[seatno]["price"]*0.5}')
        else:
            print(f'Hello {name} your seat is booked succesfully. Pay the full amount-{seats[i]["price"]}')
        print(f'{name} {age} {gender}')
else:
    print("Enter correct seatno: ")

#Prime number
n=int(input("Enter a number: "))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c=1
        break
if not c:
    print("Prime number")
else:
    print("Not a prime number")

#Factorial
n=int(input("enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f'{n}!={fact}')

#Sum of n numbers
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
'''