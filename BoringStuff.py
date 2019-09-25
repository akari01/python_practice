#! python3 practice 1
passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter Password')
userpass = input()
if userpass == secretPassword:
  print('Access granted')
  if userpass == '12345':
    print('That password is one that an idiot outs on their luggage.')
 else:
  print('Access denied')

