a=input('enter a character')
if a<=chr(90) and a>=chr(65):
    print('character is in uppercase')
elif a<=chr(122) and a>=chr(96):
    print('character is in lowercase')
elif a>='0' and a<='9':
    print('character is a digit')
else:
    print('character is a special character')


    
