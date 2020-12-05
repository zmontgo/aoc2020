dirty = """"""

clean = dirty.splitlines()

ids = []

def createList(r1, r2): 
    return list(range(r1, r2+1))

for line in clean:
  row = createList(0,127)
  column = createList(0,7)
  
  rows = line[0:7]
  columns = line[7:]

  for char in rows:
    if char == 'F':
      row = row[0:(len(row)//2)]
    if char == 'B':
      row = row[(len(row)//2):]

  for char in columns:
    if char == 'L':
      column = column[0:(len(column)//2)]
    if char == 'R':
      column = column[(len(column)//2):]

  ids.append(int((row[0]*8)+column[0]))

ids.sort()

print('Part one: ' + str(ids[-1]))

for idx, bp in enumerate(ids):
  if ((bp+1 in ids) != True) and len(ids)-1 != idx:
    print('Part two: ' + str(bp+1))
