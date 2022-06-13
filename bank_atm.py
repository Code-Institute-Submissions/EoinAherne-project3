"""
Create Parent class for User
"""
class user():
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        
    def user_details(self):
        print('User Details: ')
        print('Name: ', self.name)
        print('Age: ', self.age)
        
class bank(user):
    total_deposits = 0
    total_withdrawals = 0


    def __init__(self, name, age, balance):
        super().__init__(name, age)
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


"""
Create bank function which will populate the data of the user object
"""
def create_bank(name):
    balance = float(input(f'{name.name.title()}, how much money do you have to open account with? '))
    return balance

while True:    
    print('Welcome to EA bank')    
    name = input('Enter your name')
    age = int(input('Enter your age'))
    user_one = user(name, age)
    user_two = None
    new_user = input('Would you like to add another user? Type No to continue creating your account. ')
    if new_user.lower() == 'yes':
        name = input('Enter the second users name: ')
        age = input('Enter the second users age: ')
        user_two = user(name, age)
        print('Thank you for registering two users. Please create your accounts. ')
        