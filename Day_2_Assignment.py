'''
Assignment: Take a input1 input and print the number of occurrences of each character.
'''
input1 = "Atul Kashyap"
counting = {} 
  
for z in input1: 
   if z in counting: 
      counting[z] += 1
   else: 
      counting[z] = 1

print ("The number of occurence: in '{}' is:\n {}".format(input1, str(counting)))