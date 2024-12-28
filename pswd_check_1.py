def v_pswd(pswd):
    p_upper = False
    p_lower = False
    p_digit = False
    p_len = len(pswd)
    p_not_valid = []

    if p_len < 8:
        p_not_valid.append("password needs more than 8 characters.")
    
    for char in pswd:
        if 'A' <= char <= 'Z':
            p_upper =True
        elif 'a' <= char <= 'z':
            p_lower =True
        elif '0' <= char <= '9':
            p_digit = True
    
    if p_upper == False:
        p_not_valid.append("atleast one Uppercase character required.")
    if p_lower == False:
        p_not_valid.append("atleast one lowercase character required. ")
    if p_digit == False:
        p_not_valid.append("atleast one digit required.")

    return p_not_valid


pswd = input("enter password: ")
valid_password = v_pswd(pswd)
print("".join(valid_password))
