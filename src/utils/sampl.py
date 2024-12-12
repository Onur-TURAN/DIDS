from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Apply K-Fold Cross Validation
scores = cross_val_score(model, X_train, y_train, cv=10)
print("K-Fold Cross Validation Results:", scores)
print("Average Accuracy:", scores.mean())