import os
import csv


def log_in(user_data):
    while True:
        os.system('clear')
        print("Login\n-----\nLeave username blank to quit")
        un_input = input("Username: ")
        if un_input == '':
            return un_input
        pw_input = input("Password: ")
        if un_input not in user_data or user_data[un_input][0] != pw_input:
            os.system('clear')
            print("Login failed")
            input()
        else:
            os.system('clear')
            print("Welcome,", user_data[un_input][1], '\n')
            return un_input


def print_info(user_data, un):
    print("Username:", un)
    print("Password:", '*' * len(user_data[un][0]))
    print("Name:", user_data[un][1])
    print("Other:", user_data[un][2], '\n')


def add_user_to_user_data(user_data):
    while True:
        try:
            user_in = input("Add new user or type 'L' to log out.\n")[0].lower()
            if user_in != 'l':
                os.system('clear')
                un = input("Enter new username: ")
                if un not in user_data:
                    pw = input("Enter password: ")
                    name = input("Enter name: ")
                    other = input("Enter some other thing: ")
                    os.system('clear')
                    print("New user added")
                    input()
                    user_data[un] = [pw, name, other]
                    return user_data
                else:
                    print("User already exists.")
            else:
                return 'logout'
        except IndexError:
            print("Try again.")


def add_more_users():
    return input("Add another user? ")[0].lower() == 'y'


def get_user_data(user_data, f):
        reader = csv.reader(f)
        for row in reader:
            user_data[row[0]] = [row[1], row[2], row[3]]
        return user_data


def save_data(user_data, f):
    for un in user_data:
        f.write(un + ',' + user_data[un][0] + ',' + user_data[un][1] + ',' + user_data[un][2] + '\n')


def main():
    user_data = {}
    f = open('data.txt', 'r+')
    user_data = get_user_data(user_data, f)
    f.close()
    un = log_in(user_data)
    print_info(user_data, un)
    input()
    while True:
        os.system('clear')
        add_user_input = add_user_to_user_data(user_data)
        if add_user_input != 'logout':
            user_data = add_user_input
        else:
            with open('data.txt', 'w') as f:
                save_data(user_data, f)
            un = log_in(user_data)
            if un == '':
                break
            print_info(user_data, un)
            input()


if __name__ == '__main__':
    main()
