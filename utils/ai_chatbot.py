def get_chatbot_response(user_query):
    responses = {
        "What is malaria?": "Malaria is a disease caused by a parasite, transmitted through mosquito bites.",
        "How can I order medication?": "Log in to the app, search for the medication, and click 'Order Now'."
    }
    return responses.get(user_query, "Sorry, I do not understand your question.")

