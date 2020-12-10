#Username = input('What is your name?')
#Password = input('what is your password?')

#Password_length = len(Password)
#hidden_password = '*' * Password_length


#print(f'{Username}, your password, {hidden_password}, {len(Password_length)} letters long')

lower = int(input('Enter lower range: '))
upper = int(input('Enter upper range: '))
prime_num = []

for num in range(lower, upper+1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_num.append(num)
            
#print(prime_num)

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


import random
lower = int(input('enter lower num:'))
upper = int(input('enter upper num:'))

number = random.randrange(lower,upper)
guesscheck = 'wrong'
print('welcome to number guess')

if guesscheck == 'wrong':
    response = int(input(f'Please input a number between {lower} and {upper}: '))
    #print(response)
    try:
        val = int(response)
    except ValueError:
        print('This is not a valid integer. Please try again')
        #break
    val = int(response)
    if val<number:
        print('This is lower than actual number. Please try again')
    elif val>number:
        print('This is higher than actual number. Please try again')
    else:
        print('This is the correct number')
        guesscheck = 'correct'
 

print('Thank you for playing Number Guess. SEE YOU NEXT TIME!!!')