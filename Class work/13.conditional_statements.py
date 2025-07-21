#if-elif 
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