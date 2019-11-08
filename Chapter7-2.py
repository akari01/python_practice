#Chapter7 -2
#Project - Phone number and email extractor

import pyperclip, re

#Create phone regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  #area code
    (\s|-|\.)?                          #separater optional?
    (\d{3})                             #first digit
    (\s|-|\.)                           #separater
    (\d{4})                             #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      #extension optional
    )''',re.VERBOSE)                    #Verbose passing thr variable re.verbose as second argument

#Create Email regex
emailRegex = re.compile(r'''(
    [A-Za-z0-9._%+-]+
    @
    [A-Za-z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)

#finds matched in the clip boared

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum =+ ' x'+groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TO DO 3:Copy result to the clip board

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')

