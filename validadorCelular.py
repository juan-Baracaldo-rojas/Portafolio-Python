def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,12):
        if i==3 or i==7:
                if (text[3] and text[7]) != '-':
                    return False
        else:
            if not text[i].isdecimal():
                return False
    return True

#Buscador de Numeros telefonicos
# __________________________________________________________________________ 
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
# ___________________________________________________________________________