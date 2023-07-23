## Working with Strings

# hello= 12345

# hello=str(hello)

# print(type(hello))

# #print length of string hello

# print(len(hello))

# world = "hello"

# print( hello + world)

# # uppercase string
# print("Hello".upper())

# # lowercase string
# print("HELLO".lower())



# index
# print("Hello"[1])
# print("Hello"[0:4])
# print("Hello".index("e"))
# # only identifies first index of l
# print("Hello".index("l"))
# # string is immutable this will give error
# my_string = "HELLO"
# my_string[1] ="A"


# Working with lists
# my_list = ['a','b','c']
# number_list = ['1','2','3']

# my_list[1]= 7

# print(my_list + number_list)

# my_list.insert(1,'8')

# print(my_list + number_list)

# my_list.remove('c')

# print(my_list + number_list)


# Writing a simple algorithm

"""
    Extract first three characters of an IP address and store them in a list
"""

# IP_list= ["192.567.xxx.xxx", "198.561.xxx.xxx", "167.567.xxx.xxx", "185.xxx.xxx"]
# detection_list=[]

# for address in IP_list:
#     detection_list.append(address[0:3])
    
# print(detection_list)
 
 
"""
Regex
"""

import re

email_log= """email recieved from  dgriffith@verizon.net. email recieved from adhere@verizon.net
. email recieved from ingolfke@optonline.net
. email recieved from mwilson@live.com
. email recieved from xnormal@yahoo.com
. email recieved from maratb@aol.com
. email recieved from skajan@comcast.net
. email recieved from eabrown@yahoo.com
. email recieved from heroine@gmail.com
. email recieved from policies@outlook.com
. email recieved from gemmell@sbcglobal.net
. email recieved from yxing@me.com.
"""
print(re.findall("\w+@\w+\.\w+", email_log))
