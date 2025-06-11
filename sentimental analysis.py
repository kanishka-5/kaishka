from textblob import TextBlob

# Sample product reviews
reviews = [
    "This product is amazing! Highly recommended.",
    "Terrible experience. The product broke after one day.",
    "It's okay, not great but not terrible either.",
    "Excellent quality for the price!",
    "Waste of money. I'm very disappointed."
]

# Analyze sentiment
for i, review in enumerate(reviews, start=1):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity  # Ranges from -1 to 1
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    
    print(f"Review {i}: {review}")
    print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})\n")
from textblob import TextBlob

# Sample product reviews
reviews = [
    "This product is amazing! Highly recommended.",
    "Terrible experience. The product broke after one day.",
    "It's okay, not great but not terrible either.",
    "Excellent quality for the price!",
    "Waste of money. I'm very disappointed."
]

# Analyze sentiment
for i, review in enumerate(reviews, start=1):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity  # Ranges from -1 to 1
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    
    print(f"Review {i}: {review}")
    print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})\n")
