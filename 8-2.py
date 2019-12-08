# The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

# layers are rendered with the first layer in front and the last layer in back
# if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position



with open('inp8-1.txt', 'r') as file:
    inp = file.read().replace('\n', '')

img_w = 25
img_h = 6
img_size = img_w* img_h

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
	

def get_pixel_by_layer(img, x, y, layer = 0):
	r = img[y * img_w + x + layer * img_size]
	if r==0:
		r = ' '
	if r==1:
		r = 'O'
	if r==2:
		r = get_pixel_by_layer(img, x, y, layer+1)
	return r

	
for y in range(0, img_h):
	line = ''
	for x in range(0, img_w):
		line = line + get_pixel_by_layer(img, x, y)
	print line

#  OO  O   OO  O  OO  O  O
# O  O O   OO  O O  O O  O
# O     O O O  O O  O OOOO
# O      O  O  O OOOO O  O
# O  O   O  O  O O  O O  O
#  OO    O   OO  O  O O  O
#
# CYUAH
