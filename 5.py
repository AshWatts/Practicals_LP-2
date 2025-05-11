def food_chatbot():
    print("🍽️ Welcome to FoodBot! Ask me anything about our menu or services.")
    print("Type 'exit' to leave the chat.\n")

    responses = {
        'menu': "We offer pizzas, burgers, pasta, and salads. What would you like to try?",
        'pizza': "Our bestsellers: Margherita, Pepperoni, and Veggie Delight.",
        'burger': "Try our Cheesy Crunch or Spicy Paneer Burger!",
        'pasta': "We serve creamy Alfredo and tangy Arrabiata pastas.",
        'salad': "Fresh garden salad and Caesar salad are available.",
        'order': "You can place an order at www.foodbot.com/order or via our app.",
        'price': "Prices start at ₹99. Which item are you interested in?",
        'hours': "We are open from 10 AM to 11 PM, every day.",
        'hello': "Hi there! What can I get for you today?",
        'hi': "Hello! Craving something tasty?",
        'thanks': "You're welcome! Let me know if you're hungry again. 😊",
    }

    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("FoodBot: Goodbye! Enjoy your meal! 🍕")
            break

        response = responses.get(user_input, "I'm sorry, I didn't understand that. Can you ask something else?")
        print(f"FoodBot: {response}\n")
        