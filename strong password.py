#Chapter 7 Practice project
#Strong password
import re

#Regex
#contains more than 8 chars
char8 = re.compile('.{8,}')
#contains more than 1 Uppercase
upper = re.compile('[A-Z]')
#contains more than one lower case
lower = re.compile('[a-z]')
#contains more than 1 digit
digit = re.compile('\d+')



errMes ='Password must includes Minimum '

# input

check = False
while check == False:
    password = (input('Enter password: '))
    if char8.search(password) == None:
        print(errMes +'8 characters')
    elif  upper.search(password) == None:
        print (errMes + '1 Upper case')
    elif lower.search(password) == None:
        print (errMes + '1 lower case')
    elif digit.search(password) == None:
        print (errMes + '1 digit')
    else:
        check = True
        print('perfect password')
    
    
    
    
