#initialized the total
total = 0 
num = []

#created a list of days
day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#for loop
for i in range(0,7):
    bugs = int(input("How many bugs were collected on day " + day[i] + " ?: "))
    num += [bugs]
    total += bugs

#print toal for week
print("You collected a total of ", total , " bugs for the week.")

#for loop to get a certain day number 
for i in range(0,100000000000000000000000000000000000000000000000000000000000000000000000000000000000): 
    certainDay = int(input("Would you like to see a certain day (Sunday = 0 - Saturday = 6)?: "))
    
    #if else statement 
    if certainDay < 7 and certainDay >= 0:
        print("A total of number of ",num[certainDay]," bugs were collected on ",day[certainDay],".")
    else:
        print("Your request is invalid, please try again.")
        certainDay











    

    

