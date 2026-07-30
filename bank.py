from models import Account


class Bank:
  

    def __init__(self, name="Python Bank"):
        self.name = name
        self.accounts = {}          
        self.next_account_no = 1000  

    def create_account(self, owner_name, initial_balance=0):
        
        account_no = self.next_account_no
        self.next_account_no += 1

        new_account = Account(account_no, owner_name, initial_balance)
        self.accounts[account_no] = new_account
        return new_account

    def get_account(self, account_no):
      
        return self.accounts.get(account_no)

    def deposit(self, account_no, amount):
        account = self.get_account(account_no)
        if account is None:
            raise ValueError("Hesap bulunamadı.")
        account.deposit(amount)

    def withdraw(self, account_no, amount):
        account = self.get_account(account_no)
        if account is None:
            raise ValueError("Hesap bulunamadı.")
        account.withdraw(amount)

    def transfer(self, from_no, to_no, amount):
        
        from_account = self.get_account(from_no)
        to_account = self.get_account(to_no)

        if from_account is None or to_account is None:
            raise ValueError("Gönderen veya alıcı hesap bulunamadı.")

        
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def list_accounts(self):
        
        if len(self.accounts) == 0:
            print("Hiç hesap bulunmuyor.")
            return

        
        for account in self.accounts.values():
            print(account)

    def total_balance(self):
        
        total = 0
        for account in self.accounts.values():
            total += account.balance
        return total
