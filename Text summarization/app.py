print("========================================")
print("          TEXT SUMMARIZER")
print("========================================")

text = input("\nEnter a paragraph:\n")

sentences = text.split(".")

words = text.lower().split()

stop_words = [
    "the", "is", "a", "an", "and", "or",
    "of", "to", "in", "on", "for", "with",
    "this", "that", "are", "was", "were"
]

word_frequency = {}

for word in words:
    word = word.strip(".,!?")
    
    if word not in stop_words and len(word) > 2:
        word_frequency[word] = word_frequency.get(word, 0) + 1

sentence_scores = {}

for sentence in sentences:
    score = 0
    
    for word in sentence.lower().split():
        word = word.strip(".,!?")
        
        if word in word_frequency:
            score += word_frequency[word]
    
    sentence_scores[sentence] = score

top_sentences = sorted(
    sentence_scores,
    key=sentence_scores.get,
    reverse=True
)

print("\n----------------------------------------")
print("SUMMARY:")
print("----------------------------------------")

count = 0

for sentence in top_sentences:
    if sentence.strip():
        print(sentence.strip() + ".")
        count += 1
        
        if count == 2:
            break

print("----------------------------------------")