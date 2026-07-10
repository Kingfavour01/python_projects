# this is a practice trial to validate user input

user_name = str(input("input your user name: "))

r1 = len(user_name)
r2= user_name.find(" ")
r3= user_name.isalpha()

if r1 > 12:
    print(f"This user name [{user_name}] is invalid, it is more than 13 characters ")
elif r2 > -1:                                                                # the teacher made use of elif not r2 == -1
    print(f"This user name [{user_name}] is invalid, it contains space")
elif  r3 == False :                                                          # he also made use of elif not r3
    print(f"This user name [{user_name}] is invalid, it contains numbers")
else:
    print(f"This user name is valid, Thank you")
    print(f"Welcome {user_name}")

# he made use of logical operators but seeing as to how this is just a refresher for me, I didn't utilize them