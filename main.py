# A simple mock database for order statuses
order_status = {
    "12345": {"status": "delayed", "estimated_time": "15 minutes"},
    "67890": {"status": "on the way", "estimated_time": "5 minutes"},
    "11223": {"status": "delivered", "estimated_time": None},
}

def check_order_status(order_number):
    # Check if the order number exists in the mock database
    if order_number in order_status:
        order_info = order_status[order_number]
        if order_info["status"] == "delayed":
            return f"Your order is delayed. It should arrive in about {order_info['estimated_time']}."
        elif order_info["status"] == "on the way":
            return f"Your order is on the way and should arrive in {order_info['estimated_time']}."
        elif order_info["status"] == "delivered":
            return "Your order has been delivered. If you haven't received it, please let us know."
    else:
        return "Sorry, I couldn't find an order with that number. Could you try again?"

def chatbot():
    print("Hello! I'm your food delivery assistant.")
    print("Please type 'exit' anytime to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        
        if user_input.lower() in ["hi", "hello"]:
            print("Bot: Hello! Please provide your order number so I can check the status.")
        else:
            response = check_order_status(user_input)
            print(f"Bot: {response}")

# Start the chatbot
chatbot()

    app.run(debug=True)
