def user_name_and_password(user_name, password):
    data = input()

    while not data == password:
        data = input()

    print(f"Welcome {user_name}!")


user_name_arg = input()
password_arg = input()

user_name_and_password(user_name_arg, password_arg)