import random
import string

#generate list of password characters
lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)
digit_list = list(string.digits)
char_list = list(string.punctuation)
pwd_list = []

'''
def char_func(x, y, lst=char_list):
  for i in range(x,y+1):
    lst.append(chr(i))

char_func(33,47)
char_func(58,64)
char_func(91,96)
char_func(123,126)'''

#random password generator
print("-----------------Password generator-------------------")
print("**Minimum 8 characters for password**")
length = int(input('Enter length of password:'))


def rand_generator(itr, y, lst, x=1):
  while itr>0:
    i = random.randrange(x,y)
    pwd_list.append(lst[i])
    itr -= 1

if length>=8:
  print("Including LOWER,UPPER(CASE),DIGIT,SPECIAL CHARACTER")
  lower = int(input('Enter number of lowercase:'))
  upper = int(input('Enter number of uppercase:'))
  digit = int(input('Enter number of digit:'))
  char = int(input('Enter number of special character:'))
  if length == lower + upper + digit + char:
    rand_generator(lower,len(lower_list)-1, lower_list)
    rand_generator(upper,len(upper_list)-1, upper_list)
    rand_generator(digit,len(digit_list)-1, digit_list)
    rand_generator(char,len(char_list)-1, char_list)
    random.shuffle(pwd_list)
    print("Password: ", *pwd_list)
  else:
    print("Invalid input. Please try again.")
else:
  print("Make sure length of password >= 8. Please try again.")




