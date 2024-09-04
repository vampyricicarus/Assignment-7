# task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

reviews = str(reviews)
reviews =(reviews.replace("good","GOOD").replace("bad","BAD").replace("poor", "POOR").replace("excellent", "EXCELLENT").replace("average", "AVERAGE").replace("Poor", "POOR"))
reviews = ''.join(reviews)
print(reviews)

# task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
 
def wordCount():
    print(len(positive_words) + len(negative_words))
    return
wordCount()

# task 3

def summary():
    review1 = "This product was very useful to me as I cleaned my kitchen."
    print(review1[slice(0, 30)] + "...")
    return
summary()