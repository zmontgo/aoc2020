dirty = """""" # Input from Advent of Code

clean = dirty.replace('\n\n','NEWLINE') # Kinda janky but it works

clean = clean.replace('\n','')

clean = clean.split('NEWLINE')

valid = 0

for verification in clean:
    if verification.count(':') == 8:
        valid += 1
    elif verification.count('cid') == 0 and verification.count(':') == 7:
        valid += 1
        
print(valid)
