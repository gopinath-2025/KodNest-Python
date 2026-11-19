percentage = int(input("enter perscentage: "))
active_backlog = int(input("enter perscentage: "))
if percentage >= 60 and active_backlog == 0:
    print("eligible")
else:
    print("not eligible")
