user_string = input()
string_max = user_string
string_min = user_string
while user_string != "STOP" and user_string != "stop":
    if len(user_string) > len(string_max):
        string_max = user_string
    if len(user_string) < len(string_min):
        string_min = user_string
    user_string = input()
print(f"{string_max} {string_min}")