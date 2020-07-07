#File to implement personal pomodoro technique

'''
Algorithm
#Take in 'start' keyword
#Start time
#Wait for stop keyword
#Calculate time
#Ask for category
#Ask for what work was done
#Save it to csv file
'''

from datetime import datetime as d

try:
    file = open('Progress.csv','r')
    file.close()
except:
    file = open('Progress.csv','w')
    header = 'Start, Stop, Duration, Category, Activity\n'
    file.write(header)
    file.close()


print("Hit Enter when you are ready!!")
n = input()
start = d.now()
print("Stop wasting time now!\nHead to work.\n\nHit Enter when you are done with your session.")
n = input()
stop = d.now()
hours = stop.hour - start.hour
minutes = stop.minute - start.minute
duration = str(stop - start)

print("Enter category:")
category = input()
print('Enter the activity:')
activity = input()
#Saving it in the format.
#Start, Stop, Duration, Category, Activity
with open('Progress.csv',"a") as file:
    record = str(start)+','+str(stop)+','+duration+','+category+','+activity+'\n'
    file.write(record)

