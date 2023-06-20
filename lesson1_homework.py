def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input()
print(palindrom(string))