# Import necessary libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Step 1: Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Step 2: Sample Text
text = "The cats are running faster than the mice who were hiding in the boxes."

# Step 3: Tokenize the text
words = word_tokenize(text)

# Step 4: Lemmatize each word
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Step 5: Display Results
print("Original Words:")
print(words)
print("\nLemmatized Words:")
print(lemmatized_words)
