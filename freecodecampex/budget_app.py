class Category :
    def __init__(self,name) :
        self.name = name
        self.ledger = []
    
    def deposit(self,amount, description ="") :
        self.ledger.append({'amount':amount,
        'description':description})

    def withdraw(self,amount, description ="") :
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,
        'description':description})
            return True
        return False

    def get_balance(self) :
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount,category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self) :
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    withdrawals = []
    total_spent = 0
    # calc total withdrawals
    for category in categories :
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        withdrawals.append(spent)
        total_spent += spent
    # round up percentage
    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in withdrawals]

    # title
    chart = "Percentage spent by category\n"
    # chart bars
    for percent in range(100, -1, -10):
        chart += f"{percent:>3}| "
        for p in percentages:
            chart += "o" if p >= percent else " "
            chart += "  "
        chart += "\n"
    # bottom line
    # chart += "   " + "-" * (3 * len(categories) + 2) + "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    # vertical cat name
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i]
            else:
                chart += " "
            chart += "  "
        if i < max_len - 1:
            chart += "\n"

    return chart
       

    
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
entertainment = Category('Entertainment')
entertainment.deposit(500,'initial deposit')
entertainment.withdraw(50, 'girlfiend')
print(food)
print(create_spend_chart([food, clothing, entertainment]))