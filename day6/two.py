dirty = """"""

clean = dirty.split('\n\n')

clean = [i.split('\n') for i in clean]

count = 0

for form in clean:
  for individual in form[0]:
    if (sum(individual in s for s in form) == len(form)): count += 1
  
print(count)
