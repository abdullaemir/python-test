str1 = 'a'
str2 = 'a.b'
str3 = "a.b.c"

o1 = dict()
o2 = dict()

def transform(obj, value):
    print(obj, value)

    if (value.count('.') > 0):
        key, val = value.split('.', 1)
        if key not in obj:
            obj[key] = {}
            
        transform(obj[key], val)
    else:
        obj[value] = 1
    
    return obj

print(transform(o1, str2))
print(transform(o2, str3))