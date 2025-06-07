
def greet():
    print("👋 Hey there! I’m *CryptoBuddy*, your friendly crypto advisor.")
    print("Ask me about trending cryptos or the most eco-friendly coins!")
    print("Type 'exit' anytime to leave the chat.")
    print("Let's dive into the world of cryptocurrencies! 🚀\n")


# Predefined Crypto Data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Chatbot Logic
def handle_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These cryptos are trending up: {', '.join(trending_coins)}"

    elif "should i buy" in user_query or "best for long-term" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"🚀 {name} is trending up and has a top-tier sustainability score!"
        return "🤔 None of the cryptos fit both growth and sustainability right now."

    elif "energy" in user_query:
        eco_friendly = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"⚡ These coins use low energy: {', '.join(eco_friendly)}"

    elif "help" in user_query:
        return "Try asking: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'"

    else:
        return "❓ I didn’t catch that. Try asking about trends, sustainability, or long-term advice."

# Advice Rules
#Profitability Rule: price_trend = "rising" and market_cap = "high"
#Sustainability Rule: energy_use = "low" and sustainability_score > 7/10

# Run the Chatbot
def run_bot():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("CryptoBuddy: 🚪 Goodbye! Remember: crypto is risky — always do your own research!")
            break
        response = handle_query(user_input)
        print(f"CryptoBuddy: {response}")

if __name__ == "__main__":
    run_bot()
