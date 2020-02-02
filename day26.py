class Solution:
    def defangIPaddr(self, address):
        x = address.replace('.', '[.]')
        return x

# Second way of solving the challenge
def souliton2(address):
    result = ''
    # build an empty string
    for i in address:
        if i == ".":
            result = result + "[.]"
        else:
            result = result + i
    return result
