#time.sleep() 

import time
print(4)
time.sleep(3) # it will wait for 3 seconds and then execute the next line of code
print("This is printed after 3 seconds")


#time.strftime() - it is used to format date and time in a specific way

t= time.localtime() 
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)