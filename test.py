countryName = "CountryCode,CountryName,Currency,TimeZone"
countryName1 = "KOR,Korea,KRW,NULL"
print(countryName[0:11]== "CountryCode")
print(countryName.find("Currency") >0)
def isNotHeader(l:str):
    return not (l[0:11] == "CountryCode" and l.find("Currency")>0)

print(isNotHeader(countryName))
print(isNotHeader(countryName1))