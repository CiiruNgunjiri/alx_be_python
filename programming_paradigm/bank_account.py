class BankAccount:
    """created a class named bank account"""
    
    
    def __init__ (self, initial_balance = 0):
        """
        Initialize the BankAccount with an optional initial balance.

        Parameters:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Parameters:
            amount (float): The amount to deposit.
        """
        

        if amount > 0 :
            
            self.account_balance += amount
                        
        else:
            print('The amount should be a positive integer')
    
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        Parameters:
            amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
                  
        else:
            print("Amount must be less than or equal to the current balance.")
    
    def display_balance(self):
        """
    Prints the current account balance in a user-friendly format.

    Returns:
        None
    """
        print(f"Current Balance: ${self.account_balance:.2f}")

    