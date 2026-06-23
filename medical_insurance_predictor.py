######################################################
#Name: Victor Kumar
#Class: CS 470
#Assignment: Term Project
#Description: Medical Insurance Predictor program. Uses Medical_Insurance.csv dataset from Kaggle
#             to train and test using linear regression and uses a Tkinter library to create a
#             graphical interface for user input to predict the charges more user-friendly.
#Due: 11/13/23
######################################################
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import sklearn.metrics as sm
import tkinter as tk
from tkinter import *

# Read data from csv file containing Insurance Dataset
data = pd.read_csv('Medical_insurance.csv')

# Check missing data in Medical_Insurance.csv
# data.isnull()

# Display charts based on data file
'''
# Display counts of different ages
plt.figure(figsize=(10, 5))  
data['age'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Different Ages')
plt.show()

# Display counts of male or female
plt.figure(figsize=(4, 4))  # Optional: Adjust the figure size
data['sex'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Count of Male and Female')
plt.show()

# Display counts of childern
plt.figure(figsize=(4, 4))  # Optional: Adjust the figure size
data['children'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Children')
plt.ylabel('Count')
plt.title('Count of Childern')
plt.show()

#Display smoker or nonsmoker count
plt.figure(figsize=(4, 4))  # Optional: Adjust the figure size
data['smoker'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Smoker')
plt.ylabel('Count')
plt.title('Count of Smoker and Non-Smokers')
plt.show()

# Display region counts
plt.figure(figsize=(4, 4))  # Optional: Adjust the figure size
data['region'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Count of Different Regions')
plt.show()
'''

encoder = LabelEncoder()
# Encode data from csv file
data['EncodedSex'] = encoder.fit_transform(data['sex'])
data['EncodedSmoker'] = encoder.fit_transform(data['smoker'])
data['EncodedRegion'] = encoder.fit_transform(data['region'])

# Round charges to nearest 100 for better correlation
data['RoundedCharges'] = (data['charges'] / 100).round() * 100
temp = data.iloc[:,[0,7,2,3,8,9,10]]  # temp hold all encoded from data

#Seaborn heatmap Correlation
'''
plt.figure(figsize = (10,10))
sns.heatmap(temp.corr(), annot = False, cmap = 'coolwarm')
plt.show()
'''

# Load in all features from csv file into X and y 
X = data.iloc[:,:-1]
#y = data.iloc[:, 6]
y = data['charges']

# Dropping features because not numrical 
X = X.drop('sex', axis = 1)
X = X.drop('smoker', axis = 1)
X = X.drop('region', axis = 1)
X = X.drop('charges', axis = 1)


# Train and test split
num_training = int(0.5 * len(X)) # Use 50% of data for training
num_test = len(X) - num_training # Use the rest of thr data for testing

# Training data /   Set first 50% of data to X_train and y_train
X_train, y_train = X[:num_training], y[:num_training] 

# Test Data  /   Set the rest of the data to X_test and y_test
X_test, y_test = X[num_training:], y[num_training:]

# Create a Linear Regression Object
linear_regressor = linear_model.LinearRegression()

# Train the model using the training sets
linear_regressor.fit(X_train, y_train)

# Predict the output
y_test_pred = linear_regressor.predict(X_test)

# Compute performance score
print("R2 Score =", round(sm.r2_score(y_test, y_test_pred), 2))


# Creating GUI
window = tk.Tk()
window.title("Medical Insurance Predictor")

window.geometry("700x700")  # Window size

# function for estimate button
def estimate():
    if age_entry.get() and sex_entry.get() and bmi_entry.get() and children_entry.get() and smoker_entry.get() and region_entry.get():  # if all boxes are filled
        user_age = int(age_entry.get())
        
        user_sex_str = sex_entry.get()
        # Convert string to 0 or 1
        if user_sex_str.lower() == "female":
            user_sex = 0
        elif user_sex_str.lower() == "male":
            user_sex = 1
        else:
            estimate_label.config(text="Enter a valid sex (Male or Female)")
            
        user_bmi = float(bmi_entry.get())
        user_children = int(children_entry.get())
        
        user_smoker_str = smoker_entry.get()
        # Convert smoker yes or no to 0 or 1
        if user_smoker_str.lower() == "no":
            user_smoker = 0
        elif user_smoker_str.lower() == "yes":
            user_smoker = 1
        else:
            estimate_label.config(text="Enter Yes or No in Smoker")
   
        user_region_str = region_entry.get()
        # Convert region area to 0,1,2,3
        if user_region_str.lower() == "northeast":
            user_region = 0
        elif user_region_str.lower() == "northwest":
            user_region = 1
        elif user_region_str.lower() == "southeast":
            user_region = 2
        elif user_region_str.lower() == "southwest":
            user_region = 3
        else:
            estimate_label.config(text="Enter a valid region")

        input_data = pd.DataFrame(data=[[user_age, user_bmi, user_children, user_sex, user_smoker, user_region]],
                                  columns=['age', 'bmi', 'children', 'EncodedSex', 'EncodedSmoker', 'EncodedRegion']
                                  ).to_numpy()
        # Predict using user inputs
        user_prediction = linear_regressor.predict(input_data)

        estimate_label.config(text=f"Estimated Insurance: ${user_prediction[0]:.2f}")
        
    else:  # if any box is left empty
        estimate_label.config(text="Fill all boxes")

label_frame = LabelFrame(window, text= 'Medical Insurance Predictor')
label_frame.pack()

frame = Frame(label_frame)
frame.pack(pady = 20, padx= 20)

# Creating labels and entry boxes for user input
age_label = Label(frame, text = "Age")
age_entry = Entry(frame, font=("Arial", 18))

sex_label = Label(frame, text = "Sex (Male or Female)")
sex_entry = Entry(frame, font=("Arial", 18))

bmi_label = Label(frame, text = "BMI (Ex: 27.99)")
bmi_entry = Entry(frame, font=("Arial", 18))

children_label = Label(frame, text = "Number of Childern")
children_entry = Entry(frame, font=("Arial", 18))

smoker_label = Label(frame, text = "Smoker (Yes or No)")
smoker_entry = Entry(frame, font=("Arial", 18))

region_label = Label(frame, text = "Region (Northwest, Northeast, Southwest, Southeast)")
region_entry = Entry(frame, font=("Arial", 18))

# Display the boxes in window
age_label.grid(row = 0, column = 0)
age_entry.grid(row = 0, column = 1)
                  
sex_label.grid(row = 1, column = 0)
sex_entry.grid(row = 1, column = 1, pady = 20)

bmi_label.grid(row = 2, column = 0)
bmi_entry.grid(row = 2, column = 1)

children_label.grid(row = 3, column = 0)
children_entry.grid(row = 3, column = 1, pady = 20)

smoker_label.grid(row = 4, column = 0)
smoker_entry.grid(row = 4, column = 1)

region_label.grid(row = 5, column = 0)
region_entry.grid(row = 5, column = 1, pady = 20)

button = Button(label_frame, text= "Calculate", command=estimate)
button.pack(pady=20)

# prints label at bottom if any box is blank
estimate_label = Label(window, text= '' , font = ("Arial", 18))
estimate_label.pack(pady = 20)

window.mainloop()



#Creating a Predictor based on User inputs
'''
user_age = int(input('Enter you Age: '))
user_sex = int(input('Enter 1 for Male and 0 for Female: '))
user_bmi = float(input('Enter BMI: '))
user_children = int(input('Enter number of childern: '))
user_smoker = int(input('Smoker 1 or Non-smoker 0: '))
user_region = int(input('Enter region: '))

input_data = pd.DataFrame(
    data=[[user_age, user_bmi, user_children, user_sex, user_smoker, user_region]],
    columns=['age', 'bmi', 'children', 'EncodedSex', 'EncodedSmoker', 'EncodedRegion']
).to_numpy()

user_prediction = linear_regressor.predict(input_data)

print(user_prediction[0])
'''
