
# Making Greeting Text Simulator


import time
Name = input("Tell Me Your Name: ")
hours = int(time.strftime("%H"))

if(hours >=4 and hours <=12):
    print("Good Morning,",Name)
elif(hours >=12 and hours <= 16):
    print("Good Afternoon,",Name)
elif(hours >=16 and hours<= 19):
    print("Good Evening,",Name)
else:
    print("Good Night,",Name)




