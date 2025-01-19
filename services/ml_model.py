import joblib
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "models/word_classifier.joblib"

def train_model():
  words = ["apple", "car", "laptop", "dog", "banana", "phone", "python"]
  labels = [1 if len(word) >= 5 else 0 for word in words ]

  X = [[len(word)] for word in words]
  y = labels

  classifier = RandomForestClassifier(random_state=42)
  classifier.fit(X, y)

  joblib.dump(classifier, MODEL_PATH)
  return classifier

def load_model():
  try:
    return joblib.load(MODEL_PATH)
  except FileNotFoundError:
    return train_model()
  
def classify_word(word: str) -> str:
  classifier = load_model()
  prediction = classifier.predict([[len(word)]])[0]
  return "long" if prediction == 1 else "short"