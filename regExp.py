import re

'''
str = "How are yop.How is everythig"
matches = re.findall("How",str,re.IGNORECASE)
print(matches)
print(type(matches))

pincode = input("Enyter pincode")
pattern = r'\d\d\d \d\d\d'
matchobj= re.match(pattern,pincode)
print(matchobj)
print(type(matchobj))
'''

line = "At TTT, we teach you to perform data manipilation."\
    "file processing ."

found = re.search("AT",line,re.IGNORECASE)
if found:
    print("String found")

print(re.search('^regular','regular expression search test'))
print(re.search('^regular','test regular expression search test'))

Phone="2245-6789689-67868-88"
num= re.sub('-','',Phone)
print(num)