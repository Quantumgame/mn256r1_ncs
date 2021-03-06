import mapper_wrap
import mapper
import time
import numpy as np

def init_mappings(offsetchip0,offset_usb,offsetadcs, offsetadcs1, offsetadcs2):

    offset_first_chip = offsetchip0

    for i in range(8):
        mapper_wrap.programAddressRange(int(i),(2**32)-1)
        mapper_wrap.programOffset(i,0)
        #mapper_wrap.programBulkSpec(i,2**1)

    #registers
    mapper_wrap.programDetailMapping(0) # remove detailed mapping

    #memory
    print 'clear all mapper memory'
    mapper_wrap.programMemoryRange(0,(2**15)-1,0,0)

    time.sleep(0.5)	

    ## bulk mapping 
    mapper_wrap.programBulkSpec(1,2**0) #usb to chip0 
    mapper_wrap.programBulkSpec(0,2**1) #chip0 to usb
	#mapper_wrap.programBulkSpec(3,2**1) #adcs to usb
    mapper_wrap.programBulkSpec(3,2**1) #adcs to usb
    mapper_wrap.programBulkSpec(4,2**1) #adcs to usb
    mapper_wrap.programBulkSpec(5,2**1) #adcs to usb

    #usb offset and negative shifted input from usb
    mapper_wrap.programOffset(0,offset_first_chip)
    mapper_wrap.programMemory(offset_first_chip+0,0,0)

    #cio che entra dall'usb (con il bit 29 a uno) deve essere sottratto 2**31	
    mapper_wrap.programOffset(1,offset_usb)
    mapper_wrap.programMemory(offset_usb+0,0,0)

    mapper_wrap.programOffset(4,offsetadcs)
    mapper_wrap.programMemory(offsetadcs+1,305,1)

    mapper_wrap.programOffset(3,offsetadcs1)
    mapper_wrap.programMemory(offsetadcs1+1,300,1)

    mapper_wrap.programOffset(5,offsetadcs2)
    mapper_wrap.programMemory(offsetadcs2+1,310,1)

    #usb to 0 and 3 address range
    mapper_wrap.programAddressRange(0,(2**32)-1)
    mapper_wrap.programAddressRange(1,(2**32)-1)
    mapper_wrap.programAddressRange(3,(2**32)-1)
    mapper_wrap.programAddressRange(4,(2**32)-1)
    mapper_wrap.programAddressRange(5,(2**32)-1)

def program_multicast(pre,post,memoffset,memoffset_interface,last4bits):
    ''' single pre to multi post with memory offset'''

   
    if(np.size(pre) > 1):
        print 'this function map only one pre to multiple post neurons'
        return 
    if(len(post) < 2):
        print 'this function map only one pre to multiple post neurons'
        return 

    memory_loc_one_to_many = memoffset
    fan_out = len(post) #one irregular neuron
    
    #print 'programming multicast mapping'
    mapper_wrap.programMemory(int(memory_loc_one_to_many),int(fan_out),0) ## zero if for multicast
    #print 'init at mem location ', int(memory_loc_one_to_many), ' with fan out ', int(fan_out), ' with last 4 bits ', int(last4bits) 

    counter = 1
    for this_post in range(0,fan_out):
        mapper_wrap.programMemory(int(memory_loc_one_to_many+counter),int(post[this_post]),last4bits) ## (1<<3)+interface number
        #print 'at mem location ', int(memory_loc_one_to_many+counter), ' dest ', int(post[this_post])
        counter = counter+1

    mapper_wrap.programMemory(int(memoffset_interface+8+pre),int(memory_loc_one_to_many),0);
    #print 'now map input neuron ', int(memoffset_interface+8+pre)-int(memoffset_interface+8), ' to memory location ', int(memory_loc_one_to_many)

    memorypointer = memory_loc_one_to_many+counter

    return memorypointer

def enable_detail_mapping(mask):
    ''' mask is 2**interface+2**interface '''

    mapper_wrap.programDetailMapping(mask) 
    print 'enabled detailed mapping with mask (2**interface0)+(2**interface1).. ', str(mask)
    return

