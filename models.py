class Account:
    

    def __init__(self, account_no, owner_name, balance=0):
        self.account_no = account_no      
        self.owner_name = owner_name      
        self.balance = balance           
        self.transactions = []            

    def deposit(self, amount):
        
        if amount <= 0:
            raise ValueError("Yatırılacak tutar 0'dan büyük olmalıdır.")

        self.balance += amount
        self.transactions.append({
            "tur": "yatirma",
            "tutar": amount,
            "bakiye": self.balance
        })

    def withdraw(self, amount):
        
        if amount <= 0:
            raise ValueError("Çekilecek tutar 0'dan büyük olmalıdır.")
        if amount > self.balance:
            raise ValueError("Yetersiz bakiye.")

        self.balance -= amount
        self.transactions.append({
            "tur": "cekme",
            "tutar": amount,
            "bakiye": self.balance
        })

    def get_transaction_count(self):
        
        return len(self.transactions)

    def __str__(self):
       
        return (f"[{self.account_no}] {self.owner_name} - "
                f"Bakiye: {self.balance:.2f} TL")