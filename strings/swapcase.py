def mystring(s):
    new=""
    for a in s:
        if a.islower():
          new+=a.upper()
        elif a.isupper():
            new+=a.lower()
        if a.isalpha()==False:
            new+=a
    return new

