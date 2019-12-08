with open('inp8-1.txt', 'r') as file:
    inp = file.read().replace('\n', '')

img_w = 25
img_h = 6

# The image you received is 25 pixels wide and 6 pixels tall
# For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:
# 
# Layer 1: 123
#          456
# 
# Layer 2: 789
#          012
img = []
for i in range(0, len(inp)):
	img.append( int(inp[i]) )
	
import numpy as np
i = 0
img_size = img_w * img_h
max = []
while i<len(img):
	y =  np.array( img[i:i+img_size] )
	num_0 = np.count_nonzero(y == 0)
	num_1 = np.count_nonzero(y == 1)
	num_2 = np.count_nonzero(y == 2)
	cur = [ int(i/img_size), num_0, num_1*num_2 ]
	if max ==[]:
		max = cur
	if max[1] > cur[1]:
		max = cur
		
	i = i + img_size
	
print max
# To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
# 


# [12, 5, 2500] 
# 2500