dirty = """"""

clean = dirty.replace('\n\n', 'NEWLINE')

clean = clean.replace('\n', '')

clean = clean.split('NEWLINE')

count = 0

for form in clean:
  while 0 < len(form):
    form = form.replace(form[0], '')
    count += 1
  
print(count)
