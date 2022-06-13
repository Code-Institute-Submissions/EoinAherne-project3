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

class bank(user):
    total_deposits = 0
    total_withdrawals = 0


    def __init__(self, name, age, gender, balance):
        super().__init__(name, age, gender)
        self.balance = balance
    
    def show_info(self):
        return f'User: {self.name}, has a remaining balance of {self.balance}'
        
    def deposit(self):
        dep = float(input(f'{self.name.title}, please enter amount to deposit'))    
        print('Thanks for your deposit')
        self.balance += dep
        self.total_deposits +=1
        return f'Your new balance is {self.balance}'

    def withdraw(self):
        wdraw = float(input(f'{self.name.title}, please enter amount to withdraw'))
        if self.balance < wdraw:
            return f'You do not have sufficient funds'   
        else:
            print('Thank you. Withdrawal processing...')     
        self.balance -= wdraw
        self.total_withdrawals += 1 

