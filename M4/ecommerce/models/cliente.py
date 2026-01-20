from .usuario import Usuario


class Cliente(Usuario):
    def __init__(self, name, age, email, customer_id):
        super().__init__(name, age, email)
        self.customer_id = customer_id
        self.purchase_history = []