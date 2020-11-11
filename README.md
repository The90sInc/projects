# projects
compilation of personal exercises and projects done since i started this dev journey
#1. PASSWORD CHECKER
Username = input('What is your name?')
Password = input('what is your password?')

Password_length = len(Password)
hidden_password = '*' * Password_length

print(f'{Username}, your password, {hidden_password}, {len(Password_length)} letters long')

