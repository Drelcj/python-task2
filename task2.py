# a simple program to test user validation
# check password
# store each user and print out a list list at the end

import random
import string

users_list = []
users = {}
while True:

    first_name = input("Tell us yourfirst name: ")
    last_name = input("Tell us your last name: ")
    your_email = input("Tell us your email: ")
    suggest = ""
    new_password = ""
    chosen = ""
    corrected_password = ""
    user = []


    # create random password which should have a maximum length of 9
    def get_password():
        possible_letters = 'Q%@#L123456789abcdefghijklmnopqrstuvwxyz'
        for chars in possible_letters:
            outcome1 = random.sample(possible_letters, 5)
            outcome2 = ''.join(outcome1)

        # fetch first two letters from first name and last 2 letters from last name
        first = first_name[:2]
        last = last_name[-2:]
        first_last_letters = first + last
        password = first_last_letters + outcome2

        return password


    get_password()

    # check for password error
    print("okay with this password?:")
    suggest = get_password()
    print(suggest)
    choosen = input("enter yes to accept and no not to accept: ").upper()
    if choosen == 'YES':
        print("Your password: ", suggest)
        print("registration successful")
    else:
        new_password = input("Enter your password: ")
        if len(new_password) < 7:
            print("password must be minimum of 7 characters.")
            corrected_password = input("enter password again:")
        else:
            print(f"Your choice of password is: {new_password}")


    #
    def data():
        user = []
        for users in range(1):
            user.append(f"first_name: {first_name}")
            user.append(f"last_name: {last_name}")
            user.append(f"email: {your_email}")
            user.append(f"random_password: {suggest}")
            user.append(f"new_password: {new_password}")
            user.append(f"corrected_password: {corrected_password}")

            # stores each user in array users_list
            users_list.append(user)
            return user


    print(data())

    # condition for program termination
    prompt = input("end program? yes or no: ")
    if prompt.lower() == 'yes':
        print("Registration complete")
        users = {'registered': users_list}
        print(users)
        break
    if prompt.lower() == 'no':
        continue
