# print("Hello World!")

# print(10<4)

# # print a list
# print(["dtanaka", "mabadi", "aestrada"])

# # Dictionary
# print({1: "East", 2: "West"})

# #Set
# print({"jlanksy", "drosas", "nmason"})

#assignment and data types

# device_id = "h32rb17"

# print(device_id)

# device_data_type=type(device_id)

# print(device_data_type)

# conditional
# failed_attempts = 5

# if failed_attempts > 5:
#   print("Account has been locked")
# elif failed_attempts < 5:
#     print("login is success")
# else:
#   print("You have one more chance")

#iterative
# for i in range(10,0,-1):
#     print(i,"Cannot Connect")
    
# computer_assets = ["laptop1", "desktop20", "smartphone03"]
# for asset in computer_assets:
#     print(asset)

# time=10
# while time >= 0:
#     print(time, "wait")
#     time=time-1
    
#breaks the loop and stops execution printing the current asset
# computer_assets = ["laptop1", "desktop20", "smartphone03"]
# for asset in computer_assets:
#     if asset == "desktop20":
#         break
#     print(asset)
    
#continues in the loop bypassing the print statement
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)