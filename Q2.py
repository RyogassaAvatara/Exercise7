def accept_login(users, username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False


if __name__ == "__main__":
    user_dict = {"Jack": "pikachu123", "Harlow": "hello123", "John": "123456789"}
    print("Please insert your Username and Password.")
    u_input = input("Username: ")
    p_input = input("Password: ")
    print(accept_login(user_dict, u_input, p_input))
