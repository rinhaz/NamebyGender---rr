import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = None

dataname = input("enter the data name: ")
df = pd.read_csv("name_gender.csv")


features = df[["Name", "Count", "Probability"]]
target= df["Gender"]


features_train,features_test,target_train, target_test = train_test_split(
   features, target, test_size= 0.2, random_state=42
)


while True:
   print("Choose one of the following: ")
   print("1. Show a dataset info")
   print("2. Train a model")
   print("3. Evaluate model")
   print("4. Predict new name")
   print("5. Exit")
 
 
   userchoice = input("choose: ")
 
   if userchoice == "1":
       print("\n First 10 rows of the dataset")
       print(df.head(10))
       print("\nDataset Information:")
       print(df.describe())
     
     
   elif userchoice == "2":
     
       features = df[["Name", "Count", "Probability"]]
       target= df["Gender"]
     
       cate_features = ["Name"]
       num_features = ["Count","Probability"]
     
       prep = ColumnTransformer(
            transformers= [
                ("num", MinMaxScaler(),num_features ),
                ("cat", OneHotEncoder(handle_unknown="ignore"), cate_features), ])
     
     
       features_train,features_test,target_train, target_test = train_test_split(
           features, target, test_size= 0.2, random_state=42)


print("\nChoose a model to train:")
       print("1. K-Nearest Neighbors (KNN)")
       print("2. Decision Tree Classifier")
       choice = input("Enter 1 or 2: ")
       
       
       if choice == '1':
          model = KNeighborsClassifier(n_neighbors=3)
          print("Using KNN Classifier...")
       elif choice == '2':
          model = DecisionTreeClassifier(random_state=10)
          print("Using Decision Tree Classifier...")
          prep_features_train = prep.fit_transform(features_train)
          model.fit(prep_features_train, target_train)
          print("\n model trained")
       else:
           print("Invalid choice, choose one or two")
           continue
       prep_features_train = prep.fit_transform(features_train)
       model.fit(prep_features_train, target_train)
       print("\nModel trained successfully!")
           

         
   elif userchoice == '3':
       if model is None or prep is None:
           print("You need to train a model first (option 2).")
       else:
           prep_features_test = prep.transform(features_test)
           predictions = model.predict(prep_features_test)
           acc = accuracy_score(target_test, predictions)
           cm = confusion_matrix(target_test, predictions)
           cr = classification_report(target_test, predictions)
           
           print("\nEvaluation Results:")
           print("Accuracy:", round(acc, 4))
           print("Confusion Matrix:\n", cm)
           print("\nClassification Report:\n", cr)



           if input("\nSave results to a file? (y/n): ").lower() == 'y':
               filename = input("Enter filename (e.g., results.txt): ")
               with open(filename, 'w') as f:
                   f.write(f"Accuracy: {acc}\nConfusion Matrix:\n{cm}\nClassification Report:\n{cr}\n")
               print("Results saved!")
                     
                        
   elif userchoice == '4':
    if model is None or prep is None:
        print("You need to train a model first (option 2).")
        continue


 
    new_name = input("Enter a name: ").strip()
    if not new_name.isalpha():
        print("Name must contain only letters (A–Z).")
        continue


   
    try:
        new_count = float(input("Enter count (a number): "))
        new_prob = float(input("Enter probability (0–1): "))


        if not 0 <= new_prob <= 1:
            print("Probability must be between 0 and 1.")
            continue
    except ValueError:
        print("Please enter valid numbers for count and probability.")
        continue


    # Make prediction
    new_df = pd.DataFrame([[new_name, new_count, new_prob]],
                          columns=["Name", "Count", "Probability"])


    new_vec = prep.transform(new_df)
    prediction = model.predict(new_vec)[0]
    print(f"Predicted Gender for '{new_name}': {prediction}")


       




   elif userchoice == '5':
      print("Exiting the program. Thanks for today!!!")
      break
 
   else:
      print(" Invalid choice:( Please choose a number between 1 and 5:-)")

 


