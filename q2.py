
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

user_string = input()
string_max = user_string
string_min = user_string
while user_string != "Stop" and user_string != "stop":
    if len(user_string) > len(string_max):
        string_max = user_string
    if len(user_string) < len(string_min):
        string_min = user_string
    user_string = input()

print(f"{string_max} {string_min}")