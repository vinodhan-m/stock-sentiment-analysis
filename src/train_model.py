import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data_path):
    # Load data
    df = pd.read_csv(data_path)
    X = df[['sentiment']]  # Features
    y = df['target']  # Target variable

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

train_model('../data/twitter_data.csv')
