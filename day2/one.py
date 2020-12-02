dirty = """""" // Puzzle input from advent of code

clean = dirty.splitlines()
valid = 0

for password in clean:
    splitpwd = password.replace(' ', '-')
    splitpwd = splitpwd.replace(':', '')
    splitpwd = splitpwd.split('-')
    
    minimum = splitpwd[0]
    maximum = splitpwd[1]
    character = splitpwd[2]
    string = splitpwd[3]
    
    if ((string.count(character) >= int(minimum)) and (string.count(character) <= int(maximum))):
        valid += 1
        
print(valid)

