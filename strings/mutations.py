def mutate_string(string, position, character):
    string2 = string[:position] + character + string[position+1:] 
    return string2