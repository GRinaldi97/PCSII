def count_substring(string, sub_string):
    counter=0
    for x in range(len(string)):
        for v in range(len(string)):
            if string[x:v+1]==sub_string:
                counter+=1
    return counter