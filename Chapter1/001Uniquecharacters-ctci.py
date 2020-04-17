print('Problem:Are all characters in a string unique?')
stringtocheck = 'amazon'
CBLUE   = '\33[34m'
print("Checking string {}{}{}".format(CBLUE,stringtocheck,CBLUE))
allUnique=True
for index in range (0,len(stringtocheck)):
    for innerIndex in range(index+1,len(stringtocheck)):
        if(stringtocheck[index] == stringtocheck[index]):
                allUnique=False
                break #Break inner loop
    break #Break outer loop

if(allUnique):
    print("{}{}{} does contains all unique characters".format(CBLUE,stringtocheck,CBLUE))
else:
    print("{}{}{} does not contain all unique characters".format(CBLUE,stringtocheck,CBLUE))

