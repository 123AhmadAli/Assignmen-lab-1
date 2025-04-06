
# # Ahmad Ali
# # SP25-BBD-085



#          # QUESTION -01


animals=["dog","cat","rabbit"]
for animal in animals:
     print(animal)
     print(f" {animal} would make a great pet!")

print("Any of the animal would make a great pet!")




#          # QUESTION  -02


multiple_of_3=range(3,31,3)
for numbers in multiple_of_3:
    print(numbers) 

# list comprehansion

l = [i**3 for i in range(1,10) if i%3]

print(l)

     # Question - 03

simple_food=("chicken","vagetables","korma","chapati","kheer")
for food in simple_food:
     print(food)     
     #now we want to change the tuple list


     #simple_food[0]="piza"
     #simple_food[1]="pasta"
    # print(simple_food)   "here we try to change the tuple but tuple did not be change "hance proved")                                               
new_menu=("piza","pasta","korma","chapati","kheer")
for food in new_menu:
     print(food)

     # QUESTION - 04


     user_names=["admin","ahmad","asad","haris","mujtaba"]
for name in user_names:
    if name=="admin":
     print("Hello Admin!,would you like to see a status report?")
    else:
     print(f"Hello {name} thank you for logging in again")

        # QUESTION - 05

current_users=["ali","abid","zahra","afzal","rohan"]
new_users=["kashif","zainab","afzal","zubair","abid"]
for new_user  in new_users:
 if new_user in current_users:
    print(f"{new_user} has already been used , you need to create new one")
 else:
    print( f"{new_user} is avalible" )
    