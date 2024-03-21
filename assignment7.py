# Task 1: 
words = ["good", "excellent", "bad", "poor", "average"]

reviews = ["This product is really good. I'm impressed with its quality.", 
            "The performance of this product is excellent. Highly recommended!",
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.",
            "The product was average. Nothing extraordinary about it."]

 
for i in range(len(reviews)):
    lower_list = [i.lower() for i in reviews]
    modified_review = lower_list[i].replace(words[i], words[i].upper())
    print(modified_review)



    

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
def counter():
    count_positive=0
    count_negative=0
    raca = []
    for l in lower_list:
        racan = [x.strip() for x in l.split(".")]
        raca.append(racan)

    flat = [r for ra in raca for r in ra]

    for i in range(len(flat)):
        for world in range(len(positive_words)):
            count_positive+= flat[i].count(positive_words[world])
        for world2 in range(len(positive_words)):
            count_negative+= flat[i].count(negative_words[world2])
        
    print(count_positive)
    print(count_negative)

counter()