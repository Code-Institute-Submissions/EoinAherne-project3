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
"""
Create a child class for the bank, to inherit attributes from the parent class
"""        
class bank(user):
    total_deposits = 0    #declare variables and set to 0 to call later
    total_withdrawals = 0


    def __init__(self, name, age, balance):
        super().__init__(name, age)          #inherited from parent class  
        self.balance = balance
    
    def show_info(self):         #Function to show balance on account
        return f'User: {self.name}, has a remaining balance of {self.balance}'
        
    def deposit(self):           #Function to create deposit  
        dep = float(input(f'{self.name.title}, please enter amount to deposit: '))    
        print('Thanks for your deposit')
        self.balance += dep      #Adds deposit to balance 
        self.total_deposits +=1          #Iterates variable each time function is called
        return f'Your new balance is {self.balance}'

    def withdraw(self):          #Function to create withdrawal
        wdraw = float(input(f'{self.name.title}, please enter amount to withdraw: '))
        if self.balance < wdraw:     
            return f'You do not have sufficient funds'   
        else:
            print('Thank you. Withdrawal processing...')     
        self.balance -= wdraw
        self.total_withdrawals += 1       #Iterates variable each time function is called
        return f'Your balance is now: {self.balance}'

        
"""
A function which gives the user a list of options to use
"""
def options(user_two):  #Passing user two to see if it contains any info
    print('Thank you for opening a bank account with us')
    print('Please type the number of the option you would like to pick')
    while True:
        option_choice = int(input("1) Display Balance\n2) Make Withdrawal\n3) Deposit\n4) See total withdrawals\n5 See total deposits\n6 Quit\n"))
        if option_choice == 1:
            print(user_one_bank.show_info())   #Get user ones bank data when option 1 is chosen
            if option_choice == 1 and user_two != None:    
                print(user_two_bank.show_info())
        elif option_choice == 2:
            print(user_one_bank.withdraw())    #Activates withdraw method if one user present
            if option_choice == 2 and user_two != None:   
                wdraw = input(f'{user_two.name} Would you like to make a withdrawal? Yes or no?')
                if wdraw.lower() == "yes":
                    print(user_two_bank.withdraw())   #Activates withdraw method if two users data is present
        elif option_choice == 3:
            print(user_one_bank.deposit())  #Activates Deposit method for user ones bank 
            if option_choice == 3 and user_two != None:
                dep = input(f'{user_two.name} Would you like to make a deposit? Yes or No ')
                if dep.lower() == 'yes':
                    print(user_two_bank.deposit())
        elif option_choice == 4:
            print(f'There have been {user_one_bank.total_withdrawals} withdrawals. ')
            if option_choice == 4 and user_two != None:
                print(f'There have been {user_two_bank.total_withdrawals} withdrawals. ')
        elif option_choice == 5:
            print(f'There have been {user_one_bank.total_deposits} deposits. ')
            if option_choice == 5 and user_two != None:
                print(f'Theres have been {user_two_bank.total_deposits} deposits. ')    
        elif option_choice == 6:
            print("Thank you for using EA bank. ")
            return False
            break
        else:
            print("Please choose a number from 1-6. ")                            
                    
"""
Create bank function which will populate the data of the user object when an option is chosen
"""
def create_bank(name):
    balance = float(input(f'{name.title()}, how much money do you have to open account with? '))    #passes in name and logs input as balance 
    return balance

while True:              #Start calling from this while loop when program runs
    print('Welcome to EA bank!! Please proceed to open a new account')    
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    user_one = user(name, age)
    user_two = None
    new_user = input('Would you like to add another user? Type No to continue creating your account. ')
    if new_user.lower() == 'yes':
        name = input('Enter the second users name: ')
        age = int(input('Enter the second users age: '))
        user_two = user(name, age)        #reassign to user 2
        print('Thank you for registering two users. Please create your accounts. ')

        user_one_balance = create_bank(user_one.name)  #Creates user one balance by passing users name into bank creation
        user_two_balance = create_bank(user_two.name)  
        user_one_bank = bank(user_one.name, user_one.age, user_one_balance) # Creates user bank and passes the gathered balance information and users info from parent and child classes
        user_two_bank = bank(user_two.name, user_two.age, user_two_balance)
        marker = options(user_two)
        if marker == False:
            break
    else: 
        user_one_balance = create_bank(user_one.name)
        user_one_bank = bank(user_one.name, user_one.age, user_one_balance)
        marker = options(user_two)
        if marker == False:
            break

            
     

       