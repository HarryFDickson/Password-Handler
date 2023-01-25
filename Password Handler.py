#import random module 
import random 

#ask user for the url of the website
url = input("Please enter the url of the website you wish to save the log-in details for: ")
#ask user for the username/email
email_username = input("Please enter the email or username used to log in: ")
#ask user to input the number of characters they want in their password 
num_chars = int(input("How many characters do you want in your password: ")) 


#create a list of all possible characters that can be used in the password 
possible_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" , "U" , "V" , "W" , "X" , "Y", 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9','0','!','@','#','$','%','&']

 #generate a random password using the list of possible characters and the number of characters specified by the user  
password = ""   #initialize empty string to store generated password  


for i in range(num_chars):    #loop through each character in the password  
    char = random.choice(possible_chars)    #select a random character from the list of possible characters  
    password += char    #add the randomly selected character to the generated password string  

 #print out the generated password  
print(f"Your new password is: {password}")

with open("Details.txt","a+",encoding='utf-8') as file:
    file.write(f"URL: {url}\nUsername: {email_username}\nPassword: {password}\n\n")

print("Data has been written to the file!")