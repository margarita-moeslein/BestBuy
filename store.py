from typing import List, Tuple
from products import Product


class Store:
    """
    A Store that will hold all of these Product instances,
    and will allow the user to make a purchase of multiple products at once.

    This design concept is called composition - where a class holds reference
    to one or more objects of other classes. This is also called a "has-a" relation.
    """

    def __init__(self, products: List[Product]) -> None:
        """
        Initialize store with a list of products.

        Args:
            products: List of Product instances
        """
        self.products = products if products else []

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the store.

        Args:
            product: Product instance to add
        """
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from store.

        Args:
            product: Product instance to remove
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.

        Returns:
            Total quantity of all products combined
        """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> List[Product]:
        """
        Returns all products in the store that are active.

        Returns:
            List of active Product instances
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items: Product (Product class)
        and quantity (int). Buys the products and returns the total price of the order.

        Args:
            shopping_list: List of tuples (Product, quantity)

        Returns:
            Total price of the order

        Raises:
            Exception: If any product purchase fails
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


if __name__ == "__main__":
    import products

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_in_store = best_buy.get_all_products()
    print(best_buy.get_total_quantity())  # Should print total quantity
    print(best_buy.order([(products_in_store[0], 1), (products_in_store[1], 2)]))  # Should print total price