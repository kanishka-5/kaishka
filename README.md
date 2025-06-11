from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

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
    result = classifier(review)[0]
    print(f"Review {i}: {review}")
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

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
    result = classifier(review)[0]
    print(f"Review {i}: {review}")
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

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
    result = classifier(review)[0]
    print(f"Review {i}: {review}")
    print(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})\n")
