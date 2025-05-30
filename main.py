from typing import List, Tuple
import products
import store


MENU = '''
STORE MENU
----------
1. List all products in the store
2. Show total amount in the store
3. Make an order
4. Quit
'''


def show_all_products(products_list: List[products.Product]) -> None:
    """
    Display all products in a numbered list.

    Args:
        products_list: List of Product instances to display
    """
    print("\n------")
    for i, product in enumerate(products_list, 1):
        print(f"{i}. {product.show()}")
    print("------")


def start(store_instance: store.Store) -> None:
    """
    Main function that shows the user menu and handles user interactions.

    Args:
        store_instance: Store object to interact with
    """
    while True:
        # Display menu
        try:
            print(MENU)
            choice = int(input("Please choose a number: "))
        except ValueError:
            print("Error with your choice! Try again!")
            continue

        if choice == 1:
            # List all products
            active_products = store_instance.get_all_products()
            if active_products:
                show_all_products(active_products)
            else:
                print("\nNo active products in store.")

        elif choice == 2:
            # Show total amount
            total = store_instance.get_total_quantity()
            print(f"\nTotal of {total} items in store")

        elif choice == 3:
            # Make an order
            active_products = store_instance.get_all_products()
            if not active_products:
                print("\nNo products available for ordering.")
                continue

            show_all_products(active_products)
            shopping_list: List[Tuple[products.Product, int]] = []

            print("When you want to finish order, enter empty text.")

            while True:
                product_choice = input("Which product # do you want? ")
                if not product_choice.strip():
                    break

                quantity_choice = input("What amount do you want? ")
                if not quantity_choice.strip():
                    break

                try:
                    product_index = int(product_choice) - 1
                    quantity = int(quantity_choice)

                    if 0 <= product_index < len(active_products) and quantity > 0:
                        selected_product = active_products[product_index]
                        shopping_list.append((selected_product, quantity))
                        print("Product added to list!")
                    else:
                        print("Error adding product!")

                except ValueError:
                    print("Error adding product!")

            # Process the order
            if shopping_list:
                try:
                    total_price = store_instance.order(shopping_list)
                    print(f"********")
                    print(f"Order made! Total payment: ${total_price:.2f}")
                    print(f"********")
                except Exception as e:
                    print(f"Error while making order! {e}")
            else:
                print("No items selected for order.")

        elif choice == 4:
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice! Please choose 1-4.")


def main() -> None:
    # Setup initial stock of inventory as specified
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    # Start the user interface
    try:
        start(best_buy)
    except KeyboardInterrupt:
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()