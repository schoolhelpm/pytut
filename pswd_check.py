def pswd_validate(pswd):
    p_not_met = [] #appending all not met criteria
    pass_len = len(pswd)
    p_upper = False
    p_lower = False
    p_digit = False
    
    if pass_len < 8: # checking if password more than 8 alphachar
        p_not_met.append('Password need 8 character or more. ')
        for char in pswd: # loop to check all criteria
            if 'A' <= char <= 'Z':
                p_upper = True
            elif 'a' <= char <= 'z':
                p_lower = True
            elif '0' <= char <= '9':
                p_digit = True
        
        if not p_upper: # using not function to validate upper case letters
            p_not_met.append('Upper character missing.')
        if p_lower == False: # using comparision for same validation
            p_not_met.append('Lower character missing.')
        if p_digit == False:
            p_not_met.append('Digit character missing.')

    return p_not_met #r returning all the validation msg to main file

pswd = input('Enter password : ') # asking user for passcode
pswd_check = pswd_validate(pswd)

if pswd_check: # printing the response
    print(" ".join(pswd_check)) # Joining the string
else:
    print("Password is valid")