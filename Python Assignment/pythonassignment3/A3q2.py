string = raw_input("Enter any string:")
a = 0
b = 0
for i in string:
      if(i.islower()):
            a=a+1
      elif(i.isupper()):
            b=b+1
print("The number of lowercase characters is:")
print(a)
print("The number of uppercase characters is:")
print(b)



