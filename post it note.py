#post it note web app
#userlogin
#use an if statement to confirm password and username
#input note
#create categories
#select note category; #select note category by input category and the adding inputed category into the value of the category key
#create alarm for reminder 

#if add note input != select category

Username = 'Teezy'
password = 'oluwatoyin'
username_1 = input('Username : ')
password_1 = input('Password : ')
if Username == username_1 and password == password_1:
    print('login successful')
    add_note = input('what would you like to pin: ')
    select_category = input('Select note category :')
    categories ={
        'Business': [],                        
        'To do' : [],
        'Fun' : [],
        'Work' : []
        }
    category = ['Business', 'To Do', 'Fun', 'Work']    
    if select_category not in categories:
        print('pick a category')
    else:
        select_category == categories.keys()
        if select_category == category[0]:
            categories['Business'].append(add_note)
        elif select_category == category[1]:
            categories['To Do'].append(add_note)
        elif select_category == category[2]:
            categories['Fun'].append(add_note)
        else:
            categories['Work'].append(add_note)
        print (f'The category of the note is {select_category}')
        

    given_time = input('Remind me of task by: ')
   # time = 12
else:
    print('Try again')


def reminder():
    #if given_time == time:
        print('Alarm ringing: Press 1 to confirm task completed')
        return 'done'
    #else:
        pass


#code to check prime numbers

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
    print(prime_num)
