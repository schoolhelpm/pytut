def pswd_validate(pswd):
    p_not_met = [] #appending all not met criteria
    pass_len = len(pswd)
    p_upper = False
    p_lower = False
    p_digit = False
    
    if pass_len <= 8: # checking if password more than 8 alphachar
        p_not_met.append('Password need 8 character or more. ')
        for char in pswd:
            if 'A' <= char <= 'Z':
                p_upper = True
            elif 'a' <= char <= 'z':
                p_lower = True
            elif '0' <= char <= '9':
                p_digit = True
        
        if not p_upper:
            p_not_met.append('Upper character missing.')
        if p_lower == False:
            p_not_met.append('Lower character missing.')
        if p_digit == False:
            p_not_met.append('Digit character missing.')

    return p_not_met

pswd = input('Enter password : ')
pswd_check = pswd_validate(pswd)
print(" ".join(pswd_check))