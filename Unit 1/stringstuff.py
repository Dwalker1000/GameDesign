strvar = "my name is D"
print(strvar)
#prints lenght of string
print(len(strvar))
#prints last character
print(strvar[len(strvar)-1])
#finds and prints when name starts
indexNum = strvar.find("name")
print(indexNum)
#prints from start of name to end of name
print(strvar[indexNum: indexNum+4])
#prints from start of name to end of name
print(strvar[indexNum: ])
#prints the first second and third character
print(strvar[ :indexNum])
#prints the first, second, third, and fourth character
print(strvar[ :indexNum+1])
#replaces name with initial
print(strvar.replace('name', 'initial'))
#dosent change permentelty because we only printed it
print(strvar)
#changes it permentelty
strvar=strvar.replace('name', 'initial')
print(strvar)
#prints everything upercase
print(strvar.upper())
#prints severthing lowercase
print(strvar.lower())
#doesnt change varuable
print(strvar)
#changes it to all upercase
strvar=strvar.upper()
print(strvar)
#finds how many time something is used
print(strvar.count('I'))
