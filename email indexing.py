user = str(input("input your email: "))
index = user.index("@")


user_name = user[:index]
domain = user[index+1:]
print(f"your user name is {user_name} and your domain is {domain}")


