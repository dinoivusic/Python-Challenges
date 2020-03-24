#Create a function that return the output of letters multiplied by the int following them
import re
def multi(arr):
    chars = re.findall('[A-Z]', arr)
    digits = re.findall('[0-9]+', arr)
    final= ''.join([chars[i]* int(digits[i]) for i in range(0,len(chars)-1)]) + chars[-1]
    return final
print(multi('A4B5C2'))

def chars(arr):
    extra =''
    for char in arr:
        if char.isdigit():
            extra += extra[-1]* (int(char)-1)
        else:
            extra += char
    return extra
print(chars('A4B5C2'))
