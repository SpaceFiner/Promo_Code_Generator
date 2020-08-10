import random

def PromoCode(num_chars,num_code):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    for i in range(num_code):
    	code = ''
    	for j in range(0, num_chars):
        	slice_start = random.randint(0, len(chars) - 1)
        	code += chars[slice_start: slice_start + 1]
    	print(code) 

num_code = int(input("No. of codes u want: "))
num_chars = int(input("No. of characters in the code: "))

PromoCode(num_chars,num_code)
