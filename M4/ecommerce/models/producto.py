class Producto:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    # Método para representar el producto como un diccionario Getter
    def get_info(self):
        return {
            "ID": self.product_id,
            "Name": self.name,
            "Description": self.description,
            "Price": self.price,
            "Stock": self.stock,
        }
    
    # Método para actualizar la información del producto Setter
    def set_info(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock