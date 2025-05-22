class Product:
    """
        The Product class represents a specific type of product available in the store
        (For example, MacBook Air M2). It encapsulates information about the product,
        including its name and price.

        Additionally, the Product class includes an attribute to keep track of the
        total quantity of items of that product currently available in the store.
        When someone will purchase it, the amount will be modified accordingly.
        """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.

        Args:
            name: Product name
            price: Product price  
            quantity: Available quantity

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative
        """
        if not name:
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name.strip()
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Getter function for quantity. Returns the quantity (int).

        Returns:
            Current quantity of the product
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.

        Args:
            quantity: New quantity value

        Raises:
            ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Getter function for active. Returns True if the product is active, otherwise False.

        Returns:
            True if product is active, False otherwise
        """
        return self.active

    def activate(self) -> None:
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string that represents the product.

        Returns:
            String representation like "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.

        Args:
            quantity: Quantity to purchase

        Returns:
            Total price of the purchase

        Raises:
            Exception: If trying to buy more than available quantity or if product is inactive
        """
        if quantity <= 0:
            raise Exception("Cannot buy zero or negative quantity")

        if not self.active:
            raise Exception(f"Product {self.name} is not active")

        if quantity > self.quantity:
            raise Exception(f"Not enough {self.name} in stock. Available: {self.quantity}, Requested: {quantity}")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds ", price=250, quantity=500)
    mac = Product("MacBook Air M2  ", price=1450, quantity=100)

    print(bose.buy(50))  # Should print 12500.0
    print(mac.buy(100))  # Should print 145000.0
    print(mac.is_active())  # Should print False (quantity became 0)

    print(bose.show())  # Should show updated quantity
    print(mac.show())  # Should show quantity 0

    bose.set_quantity(1000)
    print(bose.show())  # Should show quantity 1000