

# Handler interface
class PurchaseApprover:
    def set_next(self, next_approver):
        pass

    def approve(self, purchase):
        pass

# Concrete Handlers
class Manager(PurchaseApprover):
    def set_next(self, next_approver):
        self.next_approver = next_approver

    def approve(self, purchase):
        if purchase.amount <= 1000:
            print(f"Manager approved the purchase of ${purchase.amount}")
        elif self.next_approver:
            print(f"Manager cannot approve. Escalating to {type(self.next_approver).__name__}.")
            self.next_approver.approve(purchase)
        else:
            print("No one can approve this purchase.")

class Director(PurchaseApprover):
    def set_next(self, next_approver):
        self.next_approver = next_approver

    def approve(self, purchase):
        if purchase.amount <= 5000:
            print(f"Director approved the purchase of ${purchase.amount}")
        elif self.next_approver:
            print(f"Director cannot approve. Escalating to {type(self.next_approver).__name__}.")
            self.next_approver.approve(purchase)
        else:
            print("No one can approve this purchase.")

class CEO(PurchaseApprover):
    def approve(self, purchase):
        if purchase.amount <= 10000:
            print(f"CEO approved the purchase of ${purchase.amount}")
        else:
            print("CEO cannot approve. Purchase rejected.")

# Purchase class
class Purchase:
    def __init__(self, amount):
        self.amount = amount

if __name__ == "__main__":
    manager = Manager()
    director = Director()
    ceo = CEO()

    manager.set_next(director)
    director.set_next(ceo)

    purchase1 = Purchase(800)  # Manager can approve
    purchase2 = Purchase(4500)  # Director can approve
    purchase3 = Purchase(12000)  # CEO cannot approve

    manager.approve(purchase1)
    manager.approve(purchase2)
    manager.approve(purchase3)
