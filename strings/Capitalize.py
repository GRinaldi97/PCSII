def capitalize(string):
    b=""
    for z in string:
        if z.isalnum():
            b+=z
        if z==" ":
             b+="-"
    return ' '.join([word.capitalize() for word in b.split('-')])