class Warehouse:
    def __init__(self, position, products):
        self.products = products
        self.position = position


class Order:
    def __init__(self, position, products):
        self.position = position
        self.products = products


class ProductType:
    def __init__(self, weight):
        self.weight = weight

class Drone:
    """
    - temps_occup
    - position
    """
    
    def __init__(self, position, temps_occup):
        self.position = position
        self.temps_occup = temps_occup
        
