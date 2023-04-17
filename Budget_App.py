# This is the boilerplate for the Budget App project.
# Instructions for building your project can be found at 
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

from decimal import Decimal
class Category:
    def __init__(self,category:str):
        self.category=category
        self.ledger = []
        self.incomes=0
        self.outcomes=0

    def deposit(self,amount=0,description=""):
        self.ledger.append({"amount":amount,"description":description})
        self.incomes+=amount

    def check_funds(self,amount):
        return self.incomes-self.outcomes>=amount


    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append(({"amount":-amount,"description":description}))
            self.outcomes+=amount
            return True
        return False
    
    def get_balance(self):
        return self.incomes-self.outcomes
    
    def transfer(self,amount, other_budget):
        is_possible=self.withdraw(amount=amount,description=f"Transfer to {other_budget.category}")
        if is_possible:
            other_budget.deposit(amount=amount,description=f"Transfer from {self.category}")
        return is_possible

    def __str__(self) -> str:
        o=self.category.center(30,"*")+'\n'
        for elem in self.ledger:
            a=str(Decimal(elem["amount"]).quantize(Decimal('1.00')))
            oo=" "*(7-len(a))+a
            d:str=elem["description"]
            
            o+=d+" "*(23-len(d)) if len(d)<24 else d[:23]
            o+=oo+"\n"
        o+=f"Total: {str(Decimal(self.get_balance()).quantize(Decimal('1.00')))}"
        return o


    

def create_spend_chart(categories):
    percents=[i.outcomes for i in categories]
    total=sum(percents)
    percents=list(map(lambda x: (x/total)*100,percents))

    o="Percentage spent by category\n"
    for i in range(100,-1,-10):
        if i<100:o+=" "
        if i==0:o+=" "
        o+=str(i)+"| "
        for perc in percents:
            if perc>=i:
                o+="o"
            else:
                o+=" "    
            o+="  "
        o+="\n"
    o+="    "+"-"*(len(percents)*3+1)+"\n"

    l=max(len(i.category) for i in categories)
    current=[i.category+" "*(l-len(i.category)) for i in categories]
    for i in range(l):
        o+="     "
        for c in current:
            o+=c[i]+"  "
        o+="\n"    

    return o[:-1]

