import re
# __________________________________________________________
# Caso 1
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
# __________________________________________________________
# __________________________________________________________
# Caso 2
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
# grupo 1
print('Example 1 Phone number found: ' + mo.group(1))
# grupo 2
print('Example 2 Phone number found: ' + mo.group(2))
# grupo 0
print('Example 0 Phone number found: ' + mo.group(0))
# grupo vacio
print('Example vacio Phone number found: ' + mo.group())
# __________________________________________________________
# Obtener Grupos
areaCode, mainNumber =mo.groups()
print("areaCode :",areaCode)
print("mainNumber :",mainNumber)
