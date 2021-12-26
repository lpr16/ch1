### Exercise 1
### Create a program that displays your name and complete mailing address

# name = 'Leon Pessoa Ribas'
# mail_address = 'Rua Lincoln Feliciano, 85. Ilhabela - SP, 11630-000'
#
# print('**************************************************************')
# print('Name: ', name)
# print('Address: ', mail_address)
# print('**************************************************************')


### Exercise 2
### Write a program that asks the user to enter his or her name

# print('This program prints the username')
# user_name = input('Please, write your name: ')
#
# print('**************************************************************')
# print('User name: ',user_name)
# print('**************************************************************')


### Exercise 3
### Write a program that asks the user to enter the width and length of a room. Once
### these values have been read, your program should compute and display the area of the room

# print('This program prints the area of a square; the square dimensions are given by the user')
# width = float(input('Please, enter the width: '))
# length = float(input('And now the length: '))
#
# area = width * length
#
# print('**************************************************************')
# print('The area is ', area, ' (square units)')
# print('**************************************************************')


### Exercise 4
### reads the length and width of a farmer’s field from the user in feet and display the area of the field in acres

# print("This program converts the area of field from feet to acres.")
#
# width = float(input('Please insert the width: '))
# length = float(input('And now the length: '))
#
# area = width * length
# area_in_acres = area / 43560
#
# print('**************************************************************')
# print('The area in acres is: ', area_in_acres)
# print('**************************************************************')


### Exercise 5
### In many jurisdictions a small deposit is added to drink containers to encourage people
### to recycle them. In one particular jurisdiction, drink containers holding one liter or
### less have a $0.10 deposit, and drink containers holding more than one liter have a
### $0.25 deposit.
### Write a program that reads the number of containers of each size from the user.
### Your program should continue by computing and displaying the refund that will be
### received for returning those containers. Format the output so that it includes a dollar
### sign and two digits to the right of the decimal point.

# print('Return a container for recycling.')
# container1 = 0
# container2 = 0
# money = 0
#
# finish = False
#
# while (finish != True):
#     flag = input('Do you want to return a container? ')
#     if (flag == 'yes'):
#         size = input('Is your container bigger than 1L? ')
#         if (size == 'yes'):
#             container2 += 1
#             money += 0.25
#         else:
#             container1 += 1
#             money += 0.10
#         print('Containers returnerd: ', container1 + container2)
#         print('Money recieved: ', money)
#     else:
#         finish = True
#         print('Thank you!')

