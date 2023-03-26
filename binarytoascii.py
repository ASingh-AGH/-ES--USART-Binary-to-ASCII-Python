
#redundant may be useful later code
# with open('time.txt', 'r') as j: # time being cummulative frequency
#     time = [float(line.strip()) for line in j.readlines()]
# with open('binaryinput.txt', 'r') as k: # binary input
#     binaryin = [float(line.strip()) for line in k.readlines()]

import matplotlib.pyplot as plt

#read from freqency file into list freq, self explanatory
with open('frequency.txt', 'r') as f:
    freq = [int(line.strip()) for line in f.readlines()]


#populate binary out with frequency alternating 1 0
binaryout = []
for i in range(len(freq)):
    if i % 2 == 0: 
        binaryout += [1] * freq[i] # eg. future me: 1 * 3 = 1 1 1 
    else: 
        binaryout += [0] * freq[i]

plt.figure(figsize=(10,2))
plt.ylim(-0.1, 1.1) # set y-axis limits
# plt.plot(binaryout)
# plt.show()
#print(binaryout) #works scary fast

binarystr = ''.join([str(bit) for bit in binaryout]) #convert binary list to string 
#plot binary data as graph
binarystr = binarystr[1:-1] #remove begin and end bit for every byte slicey slicey
#print(binarystr) 

binaryout = [int(bit) for bit in binarystr]
plt.plot(binaryout)
plt.show()

#print binary string in blocks of 8
formatted_str = ' '.join([binarystr[i:i+8] for i in range(0, len(binarystr), 8)])
print(formatted_str) 

# what am i doing wrong ;-; ascii not worki
##convert binary string to ascii
#ascii_str = ''.join([chr(int(binarystr[i:i+8], 2)) for i in range(0, len(binarystr), 8)])
#print(ascii_str)

