import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer


data = pd.read_csv("gender_by_name.csv")
print(data.head(10))

X = data['Name']
y = data['Gender']

vectorizer = CountVectorizer
X = vectorizer.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test size = 0.2, randome_state = 10) 

model = KNeighborsClassifier(n_neighbors=3) 
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test) 
print(\n "Accuracy:", accuracy_sore(Y_test, Y_pred))
print("Confuson Matrix:\n", confusion_matrix(Y_test, Y_pred))

new_name = input()
new_vec = vectorizer.transform([new_name])
print("Predicted Gender:", model.predict())







