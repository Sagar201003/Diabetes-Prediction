from django.shortcuts import render,HttpResponse,redirect
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from dia_2.models import Peopleinfo

def view(request):
    return render(request, 'index.html')
def get_user_input(request):
# Load and preprocess the diabetes dataset
    data2 = pd.read_csv('PIMA workbook Maths.csv')
# preprocess the dataset as needed
    columns_drop = ['Outcome', 'SkinThickness']
    x = np.array(data2.drop(columns_drop, axis=1))
    y = np.array(data2.Outcome)
# Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a logistic regression model
    LR = LogisticRegression()
    logreg=BaggingClassifier(estimator=LR,n_estimators=100,max_samples=0.8,oob_score=True,random_state=0)
    logreg.fit(x_train, y_train)

# Define a function to take user input

    if request.method == "POST":
        name = request.POST.get('name')
        preg = float(request.POST.get('preg', 0))
        glu = float(request.POST.get('glu', 0))
        if glu == 0:
            glu = float(data2['Glucose'].mean())
        bp = float(request.POST.get('bp', 0))
        if bp == 0:
            bp = float(data2['BloodPressure'].mean())
        insulin = float(request.POST.get('insulin', 0))
        if insulin == 0:
            insulin = float(data2['Insulin'].mean())
        height =(request.POST.get('height', '0'))
        weight = (request.POST.get('weight', '0'))

        dpf = float(request.POST.get('dpf', 0))
        if dpf == 0:
            dpf =float (data2['DiabetesPedigreeFunction'].mean())
        age = float(request.POST.get('age', 0))
        gender = float(request.POST.get('Gender', 0))
        
    height=float(height)
    weight=float(weight)
    # Return None if the request method is not POST
    bmi = weight / (height * height)
# Call your input function to get user input
    user_input =  np.array([[preg, glu, bp, insulin, bmi, dpf, gender, age]])
    prediction = logreg.predict(user_input)
    my_user=Peopleinfo(name=name,preg=preg,glu=glu,bp=bp,insulin=insulin,height=height,weight=weight,dpf=dpf,age=age,gender=gender)
    my_user.save()
    if prediction == [0]:
        # return HttpResponse("The predicted outcome : you don't have diabetes")
        return render(request, 'diapredPositive.html')
    else:
        # return HttpResponse("The predicted outcome : you have diabetes") 
        return render(request, 'diapredNegative.html')
    
    
    

    



# Create your views here.
