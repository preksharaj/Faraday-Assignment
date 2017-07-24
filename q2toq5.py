print "#####Q2: string as input and output type#######"

def convert(s):
    if s.count(".") == 1:
        if s.replace(".", "").isdigit():
            return float(s)
    if s[0] in ('-', '+'):
        if s[1:].isdigit():
                return int(s)
    if s.isdigit():
        return int(s)
    if isinstance(s,str):
        return s


print type(convert("hello"))
print type(convert("-10"))
print type(convert("10.34"))


print "#####Q3: Reformat the list code ###########"

def ani(a):
        return a[1]+" the "+a[0]+" is "+a[2]+" years old."

list = ["dog","fido","10"]

print ani(list)


print "#####Q4: function to find the min of 3 numbers########"

def minimum(a, y, z):
    min = a
    if y < min:
        min = y
    if z < min:
        min = z
        if y < z:
            min = y
    return min

print minimum(10,3,15)


print "#####Q5: Reformat the operators code ############"

apply_operation=lambda a,b,c: a+b if c=='+' else a-b if c=='-' else a*b if c=='*' else a/b if c=='/' else -1
print apply_operation(10,20,'*')
