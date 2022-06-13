#Create a Parent Class for the account holder
#Stores user details
#function which calls the information in the class, eg account holder

#Create a child class for the bank
#Holds info about account balances
#functions which allow to withdraw, deposit, view balance



"""
Create Parent class for User
"""
class user():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        print('User Details: ')
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)




