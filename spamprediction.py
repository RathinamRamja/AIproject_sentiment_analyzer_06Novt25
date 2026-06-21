from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample Data
emails = [
    "win free lottery money now",      # Input 1 - spam
    "meeting tomorrow at office",      # Input 2 - not spam  
    "buy now limited offer",           # Input 3 - spam
    "project deadline next week",      # Input 4 - not spam
    "free cash prize claim"            # Input 5 - spam
]
labels = [1, 0, 1, 0, 1]  # OUTPUT: 1=Spam, 0=Not Spam

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)  # INPUT: email texts

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save both model and vectorizer
joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Prediction - NEW INPUT
new_email = ["congratulations you won prize"]  # INPUT
new_email_vector = vectorizer.transform(new_email)
prediction = model.predict(new_email_vector)  # OUTPUT

print(f"Spam Prediction: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
# Output: Spam Prediction: Spam
# /////////////////////

new_email = [" deadline next week you won prize project"]

new_email_vector = vectorizer.transform(new_email)
print("new_email_vector",new_email_vector)
prediction = model.predict(new_email_vector)
print("prediction",prediction)

print("Spam" if prediction[0] == 1 else "Not Spam")

