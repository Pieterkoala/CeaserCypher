
key = input("Enter a key (0 - 26) ")

# Use a while loop to make sure he encrypts or decrypts
while True:
    mode = input("Do you want to encrypt or decrypt? ")

    # Small if-else statement for a right presentation
    if mode == "encrypt":
        message = input("What do you want to encrypt? ")
        break

    elif mode == "decrypt":
        message = input("What do you want to decrypt? ")
        break
    
    else:
        print("Please enter 'encrypt' or 'decrypt'")

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Make sure the input is upper case
message = message.upper()


# Loop through alfabat
for letter in message:
    
    # Find a collab between message and alfabet
    if letter in alfabet:
        
        if mode == "encrypt":
            
            # Finding our index of the solution in alfabet
            indexresult = alfabet.find(letter) + int(key)
        
        elif mode == "decrypt":
            indexresult = alfabet.find(letter) - int(key)
        
        # With our index of the solution, we can print the value of that index
        translation = alfabet[indexresult]
        
        print(translation)
        