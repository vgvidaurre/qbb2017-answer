#!/usr/bin/env python

import random 

r = random.randint(1,100)

#print r

nums = range(0, 100, 10)
print nums

key = 80

lo = 0
hi = len(nums)

## main loop: keep going while there are options available
while lo < hi:
    # find middle item
    midpoint = (lo + hi) / 2
    mid = nums[midpoint]
    
    print "checking in the range [%d, %d] mididx[%d] = %d" % (lo, hi, midpoint, mid)
    
    # compare middle item to the list
    if (mid == key):
        print "hooray! found %d = %d at %d" % (key, mid, midpoint)
        break
    elif (key > mid):
        lo = midpoint + 1
    else:
        hi = midpoint 
        
        
        
        
    
            
            
    
    
    
            
            
    





#for i in xrange(len(nums)):
    #v = nums[i]
    #while v > 4 == True:
        
    #print "scanning the %dth number is %d" % (i,v)
    #if (v == key):
        #print "Found it at positiion %d" % (i)