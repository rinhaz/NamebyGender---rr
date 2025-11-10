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
 
