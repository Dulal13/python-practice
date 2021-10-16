def removeSplit(string , word):
    newString = string.replace(word,"")
    return newString.strip()

name = "    Md.Dulal Miah"
word = "Dulal"
print(removeSplit(name,word))