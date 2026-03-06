#Take input of a word
string = input("PLease enter your own word : ")
#Take inpu tof a character
char = input("Please enter your own Character : ")
i = 0
count = 0
#loop will to find the occurence of the character 
while(i < len (string)):#string operation
    
    if (string[i] ==  char): #Condition 1
        count = count + 1
    i = i + 1
    
#Display the result
print("The total NUmber of times ", char, "has Occured =", count)