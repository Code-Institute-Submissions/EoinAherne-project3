"""
Create Parent class for User
Use initialiser to create object of user, taking self, name and age parameters
"""


class user():
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def user_details(self):  # Creates method to show users details
        print('User Details: ')
        print('Name: ', self.name)
        print('Age: ', self.age)
"""
Create a child class for the bank, to inherit attributes from the parent class
The banks class will contain the functions of the bank application
"""


class bank(user):
    total_deposits = 0  # declare variables and set to 0 to call later
    total_withdrawals = 0

    def __init__(self, name, age, balance):  # Create object in class with constructor
        super().__init__(name, age)  # Takes name and age and gives it to the Bank
        self.balance = balance  # Creates balance variable

    def show_info(self):  # Function to show balance on account
        return f'User: {self.name}, has a remaining balance of {self.balance}'

    def deposit(self):  # Function to create deposit
        dep = float(input(f'{self.name.title()}, please enter amount to deposit: '))
        print('Thanks for your deposit')
        self.balance += dep  # Adds deposit to balance
        self.total_deposits += 1  # Iterates variable each time function is called
        return f'Your new balance is {self.balance}'  # Prints users updated balance

    def withdraw(self):  # Function to create withdrawal
        wdraw = float(input(f'{self.name.title()}, please enter amount to withdraw: '))  # stores withdrawal amount from input
        if self.balance < wdraw:  # Checks if balance is higher than requested withdrawal
            return f'You do not have sufficient funds'
        else:
            print('Thank you. Withdrawal processing...')
        self.balance -= wdraw  # Subtracts requested withdrawal amount from balance
        self.total_withdrawals += 1  # Iterates variable each time function is called
        return f'Your balance is now: {self.balance}'  # Returns new balance minus withdrawal


"""
A function which gives the user a list of options to use
The body of the programs functions will be called from here
"""


def option(user_two):  # Passing user two to see if it contains any info
    print('Thank you for opening a bank account with us')
    print('Please type the number of the option you would like to pick')
    while True:
        option_choice = int(input("1) Display Balance\n2) Make Withdrawal\n3) Deposit\n4) See total withdrawals\n5 See total deposits\n6 Quit\n"))
        if option_choice == 1:
            print(user_one_bank.show_info())  # Get user ones bank data when option 1 is chosen
            if option_choice == 1 and user_two is not None:
                print(user_two_bank.show_info())  # If user_two is present it will display their bank data
        elif option_choice == 2:
            print(user_one_bank.withdraw())  # Activates withdraw method if one user present
            if option_choice == 2 and user_two is not None:
                wdraw = input(f'{user_two.name} Would you like to make a withdrawal? Yes or no?\n')
                if wdraw.lower() == "yes":
                    print(user_two_bank.withdraw())  # Activates withdraw method if two users data is present
        elif option_choice == 3:
            print(user_one_bank.deposit())  # Activates Deposit method for user ones bank
            if option_choice == 3 and user_two is not None:
                dep = input(f'{user_two.name} Would you like to make a deposit? Yes or No\n ')
                if dep.lower() == 'yes':
                    print(user_two_bank.deposit())
        elif option_choice == 4:
            print(f'There have been {user_one_bank.total_withdrawals} withdrawals. ')  # Displays user ones bank info and total withdrawls number
            if option_choice == 4 and user_two is not None:
                print(f'There have been {user_two_bank.total_withdrawals} withdrawals. ')
        elif option_choice == 5:
            print(f'There have been {user_one_bank.total_deposits} deposits. ')  # Displays user ones bank info and total deposits
            if option_choice == 5 and user_two is not None:
                print(f'Theres have been {user_two_bank.total_deposits} deposits. ')
        elif option_choice == 6:
            print("Thank you for using EA bank. ")
            return False
            break
        else:
            print("Please choose a number from 1-6. ")


"""
Create bank function
Will populate the data of the user object when program is started, data input request for name and age
"""


def create_bank(name):
    balance = float(input(f'{name.title()}, how much money do you have to open account with?\n '))    # Passes in name and logs input as balance
    return balance

while True:  # Start calling from this while loop when program runs
    print('Welcome to EA bank!! Please proceed to open a new account')
    name = input('Enter your name:\n ')  # Takes input and stores as name
    age = int(input('Enter your age:\n '))  # Takes input and stores as age
    user_one = user(name, age)  # Creates user one variable and passes name and age
    user_two = None  # Creates empty variable to activate while loop in options function
    new_user = input('Would you like to add another user? Type No to continue creating your account.\n ')
    if new_user.lower() == 'yes':
        name = input('Enter the second users name:\n ')
        age = int(input('Enter the second users age:\n '))
        user_two = user(name, age)  # Creates user two variable and passes second inputted users name and age
        print('Thank you for registering two users. Please create your accounts. ')

        user_one_balance = create_bank(user_one.name)  # Creates user one balance by passing users name into bank creation function
        user_two_balance = create_bank(user_two.name)
        user_one_bank = bank(user_one.name, user_one.age, user_one_balance)  # Creates user bank and passes the gathered balance information and users info from parent and child classes
        user_two_bank = bank(user_two.name, user_two.age, user_two_balance)  # Creates user two bank and passes gathered data
        marker = option(user_two)
        if marker is False:  # When false is entered on create second user qustion break out of while loop here
            break
    else:
        user_one_balance = create_bank(user_one.name)  # When user two is created store user one balance here
        user_one_bank = bank(user_one.name, user_one.age, user_one_balance)  # When user two is created store user one bank here
        marker = option(user_two)
        if marker is False:  # Exits while loop with both users information stored and banks created
            break
