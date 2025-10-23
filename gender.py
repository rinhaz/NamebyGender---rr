import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer

dataset_name = input("Enter the following dataset name: ")
data = pd.read_csv("gender_by_name.csv")
print(" Dataset loaded successfully!")


print("Choose one of the following:")
print("1. Show dataset info")
print("2. Train a model")
print("3. Evaluate model")
print("4. Predict new name")
print("5. Exit")

userchoice = input("Choose: ")

if userchoice == '1':
  print(data.head(10))
  print("/N Basic statistics:", data.describe())

if  userchice == '2':
    X = data['Name']
    y = data['Gender']
    vectorizer = CountVectorizer(analyzer='char')
    X = vectorizer.fit_transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test size = 0.2, randome_state = 10) 

    print ("\n Choose a model to train:")
    print("1: K-Nearest Neighbors (KNN)")
    print("2. Decision Tree Classifier")
  choice = input("Enter 1 or 2: ")
    if choice == '1':
        model = KNeighborsClassifier(n_neighbors=3)
        print("Using KNN Classifier...")
    else:
        model = DecisionTreeClassifier(random_state=10)
        print("Using Decision Tree Classifier...")
    model.fix(X_train, Y_train)
    print("\n Model trained")

if userchoice == '3':
    use_file = input("Do you want to load another CSV file ? ")
    if use_file.lower() == 'y':
        test_file = input("Enter test dataset name: ")
        test_data = pd.read_csv(test_file)
        X_eval = vectorizer.transform(test_data['Name'])
        Y_eval = test_data['Gender']
    else:
        X_eval = X_test
        Y_eval = Y_test

Y_pred = model.predicted(X_eval)

acc = accuracy_score(Y_eval, Y_pred)
cm = confusion_matrix(Y_eval, Y_pred)
cr = classification_report(Y_eval, Y_pred, zero_division =0)

print("Evaluation Results:")
print("Accuracy:", round(acc, 4))
print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", cr)

    if input("\nSave results to a file? (y/n): ").lower() == 'y':
        with open(input("Enter filename (e.g. results.txt): "), 'w') as f:
            f.write(f"Accuracy: {acc}\nConfusion Matrix:\n{cm}\nClassification Report:\n{cr}\n")
        print(" Results saved!")

if userchoice == '4':
    simulate = input("\nDo you want to predict a new name? (y/n): ")
    if simulate.lower() == 'y':





Y_pred = model.predict(X_test) 
print(\n "Accuracy:", accuracy_sore(Y_test, Y_pred))
print("Confuson Matrix:\n", confusion_matrix(Y_test, Y_pred))

new_name = input("\n Type a name to predict gender: ")
new_vec = vectorizer.transform([new_name])
print("Predicted Gender:", model.predict(new_vec)[0])















