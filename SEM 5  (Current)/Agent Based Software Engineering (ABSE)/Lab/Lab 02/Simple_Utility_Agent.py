class SimpleUtilityShopper:

    def __init__(self, utility_scores):
        self.utility_scores = utility_scores
        print(f"Agent initialized with utility scores: {self.utility_scores}")

    def decide_to_buy(self, item_category, utility_threshold=50):

        utility = self.utility_scores.get(item_category, 0)
        
        if utility >= utility_threshold:
            decision = f"Buy '{item_category}'. (Utility: {utility} >= Threshold: {utility_threshold})"
        else:
            decision = f"Don't buy '{item_category}'. (Utility: {utility} < Threshold: {utility_threshold})"
        
        print(decision)
        return decision

# --- Example Usage ---
print("\n--- Simple Utility-Based Agent Demo ---")
scores = {'electronics': 90, 'food': 70, 'clothes': 45}
shopper = SimpleUtilityShopper(scores)

shopper.decide_to_buy('electronics')
shopper.decide_to_buy('food')
shopper.decide_to_buy('clothes')
