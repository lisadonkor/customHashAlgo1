def hash(astring):
    #astring = 'c'

    sum = 0
    for pos in range(len(astring)):
        for x in range(pos + 1):
            sum = sum + ord(astring[pos]) 
        print(sum) 
    #return sum
        
hash('cat')
