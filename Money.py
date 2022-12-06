def Money(country):
    def spain():
        print("euro")
    def japan():
        print("Yen")   
    def eeuu():
        print("dollar")  
    functomoney={'es':spain(),
                 'jp':japan(),
                 "us":eeuu()}   
    return functomoney

f=Money("us")
#print(type(Money('us')))
print(Money('us'))

print(type(f))

print(Money('jp'))
print(type(f))