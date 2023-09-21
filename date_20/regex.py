# # RegEx can be used to check if a string contains the specified search pattern.
# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")
import re
user_name=r'^[A-Z][a-z\d_]{3,16}$'
pass_word=r'^[a-zA-Z\d_]{6,16}$'
def validate_username(username):
    return re.match(user_name, username)

def validate_password(password):
    return re.match(pass_word, password)

def main():
    print("Login Validation")
    while True:
        username=input("Input your username: ")
        if validate_username(username):
            break
        else:
            print('Invalid')
    while True:
        password=input("Input your password: ")
        if validate_password(password):
            break
        else:
            print('Invalid')
    print('Login Successful')

if __name__ == "__main__":
    main()