n=int(input("Enter no of msgs:"))
chat={}
for i in range(n):
    name,msg=input().split(":")
    if name in chat:
        chat[name].append((i,msg.strip()))
    else:
        chat[name]=[(i,msg.strip())]
while True:
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("0-Exit")
    ch=int(input("Enter your choice:"))
    if ch==0:
        break
    elif 1<=ch<=18:
        if ch==1:
            total_msgs=0
            for i in chat:
                total_msgs=len(chat[i])
            print(f'Total number of messages:{total_msgs}')
        elif ch==2:
            
