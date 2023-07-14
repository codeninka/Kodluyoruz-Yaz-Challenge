import datetime

birthdate = input('Enter your age in DD/MM/YY format: ')
rawdateinfo = birthdate.split('/')

while len(rawdateinfo) != 3:
    birthdate = input('Enter your age in DD/MM/YY format: ')
    rawdateinfo = birthdate.split('/')

birthday = int(rawdateinfo[0])
birthmonth = int(rawdateinfo[1])
birthyear = int(rawdateinfo[2])

def calculate_age():
    today = datetime.date.today()
    if today.month >= birthmonth:
        age = today.year - birthyear
    else:
        age = today.year - birthyear - 1
    return age

age = calculate_age()

# Print the age
print("Your age is", age)

  
  






