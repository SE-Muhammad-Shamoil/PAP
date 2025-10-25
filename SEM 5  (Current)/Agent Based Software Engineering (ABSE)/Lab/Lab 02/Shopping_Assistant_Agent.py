def shopping_assistant_agent(budget, items):

    print(f"Shopping Assistant activated. Budget: ${budget:.2f}\n")
    
    # Calculate the effective price and utility-to-price ratio for each item
    for item in items:
        item['effective_price'] = item['price'] * (1 - item['discount_percent'] / 100)
        item['value_ratio'] = item['utility'] / item['effective_price']

    # Sort items by their value ratio in descending order (greedy approach)
    sorted_items = sorted(items, key=lambda x: x['value_ratio'], reverse=True)

    shopping_cart = []
    total_cost = 0
    total_utility = 0

    print("Evaluating items based on value (Utility/Price ratio):")
    for item in sorted_items:
        print(f" - Considering '{item['name']}' (Price: ${item['effective_price']:.2f}, Utility: {item['utility']}, Value Ratio: {item['value_ratio']:.2f})")
        if total_cost + item['effective_price'] <= budget:
            shopping_cart.append(item)
            total_cost += item['effective_price']
            total_utility += item['utility']
            print(f"   -> ADDED to cart.")
        else:
            print(f"   -> SKIPPED. Not enough budget.")

    print("\n--- Purchase Summary ---")
    print(f"Items in Cart: {[item['name'] for item in shopping_cart]}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Total Utility Maximized: {total_utility}")

# --- Example Usage ---
print("\n--- Shopping Assistant Agent Demo ---")
available_items = [
    {'name': 'Headphones', 'price': 150, 'utility': 90, 'discount_percent': 10}, # eff_price: 135, ratio: 0.67
    {'name': 'Smartwatch', 'price': 250, 'utility': 95, 'discount_percent': 0},  # eff_price: 250, ratio: 0.38
    {'name': 'Keyboard', 'price': 80, 'utility': 70, 'discount_percent': 0},   # eff_price: 80, ratio: 0.88
    {'name': 'Mouse', 'price': 40, 'utility': 50, 'discount_percent': 20}      # eff_price: 32, ratio: 1.56
]
shopping_budget = 200

shopping_assistant_agent(shopping_budget, available_items)