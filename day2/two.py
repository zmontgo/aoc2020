dirty = """""" // Puzzle input from advent of code

clean = dirty.splitlines()
valid = 0

def logical_xor(a, b):
    return bool(a) ^ bool(b)

for password in clean:
    splitpwd = password.replace(' ', '-')
    splitpwd = splitpwd.replace(':', '')
    splitpwd = splitpwd.split('-')
    
    pos1 = int(splitpwd[0])
    pos2 = int(splitpwd[1])
    character = splitpwd[2]
    string = splitpwd[3]
    
    if (logical_xor(string[pos1-1] == character, string[pos2-1] == character)):
        valid += 1
        
print(valid)
