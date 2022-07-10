with open ('test2.csv') as f:
    lines = f.read().split(',')
    
    
with open ('test2.txt','w') as filehandle:
    for listitem in lines:
        filehandle.write('%s\n' % listitem)