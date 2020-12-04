dirty = """"""
 
clean = dirty.replace('\n \n','NEWLINE') # I've found this to be dubious - it sometimes needs the space, and sometimes it does not
 
clean = clean.replace('\n',' ')
 
clean = clean.split('NEWLINE')
 
valid = 0
 
for verification in clean:
    values = verification.split()
    res = dict()
  
    # using loop to reform dictionary with splits 
    for ele in values:
        dictionaryvals = ele.split(':')
        res[dictionaryvals[0]] = dictionaryvals[1]
        
    try:
        height = int(res['hgt'][0:-2])
        
        haircolor = int(res['hcl'][1:],16) # This will throw the program into the except block if this is invalid
        
        eyecolor = res['ecl']
        passport = int(res['pid'])
        issued = int(res['iyr'])
        birth = int(res['byr'])
        expiration = int(res['eyr'])
 
        if (issued >= 2010 and issued <= 2020):
            
            if (birth >= 1920 and birth <= 2002):
                if (expiration >= 2020 and expiration <= 2030):
                    if (
                        (res['hgt'][-2:] == 'cm' and height >= 150 and height <= 193)
                        or
                        (res['hgt'][-2:] == 'in' and height >= 59 and height <= 76)
                    ):
                        if (eyecolor == "amb" or eyecolor == "blu" or eyecolor == "brn" or eyecolor == "gry" or eyecolor == "grn" or eyecolor == "hzl" or eyecolor == "oth"):
                            if (len(res['pid']) == 9):
                                if (len(res['hcl']) == 7):
                                    valid += 1
    except:
        pass
        
print(valid)
