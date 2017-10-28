from string import ascii_lowercase as low
def print_rangoli(size):
    a= low[:size][::-1] #reverse of the alphabet from the "size" word to "a"
    for i in range(1, size+1):
        string=a[:i]
        fstring = '-'.join(string).rjust(size*2) #outputs the first part of the first half of the rangoli
        fstring +=fstring[::-1][1:] #adds the second part
        print fstring.replace(" ", '-')[1:-1] #replaces the spaces outside the word with "-"
    for t in range(1, size):
        string=a[:-t]
        fstring = '-'.join(string).rjust(size*2)
        fstring +=fstring[::-1][1:]
        print fstring.replace(" ", '-')[1:-1]
        
        