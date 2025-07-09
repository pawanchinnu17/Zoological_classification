🧠 Animal Classification Using XGBoost
A machine learning project that classifies animals into biological classes based on their physical and behavioral traits using the Zoo dataset. This project uses the XGBoost algorithm to achieve 100% accuracy, with an interactive Streamlit app for real-time predictions.

📌 Table of Contents
📌 Table of Contents

📂 Project Overview

🔍 Problem Statement

📊 Dataset Description

⚙️ Project Pipeline

📈 Model Selection

🧪 Model Evaluation

🚀 Deployment

📸 Sample Predictions

📚 Future Scope

✅ Conclusion

🛠️ Tech Stack

📎 References

📂 Project Overview
This project focuses on predicting the biological class of an animal using only its physical and behavioral features, such as hair, feathers, milk, aquatic, and legs. By using the Zoo dataset, we explore how even simple, binary features can be powerful enough to distinguish among 7 animal classes using machine learning.

🔍 Problem Statement
To classify animals into their correct class types (e.g., Mammal, Bird, Reptile, Fish) using only 16 binary attributes — without any species names or textual descriptions. The main goal is to automate classification in educational and biological research domains using an interpretable, highly accurate model.

📊 Dataset Description
Source: UCI Machine Learning Repository

Records: 101 animals

Features: 16 binary features (e.g., milk, eggs, backbone, aquatic, legs)

Target: class_type (1–7 representing 7 biological classes)

Note: The dataset is clean with no missing values or outliers

🧾 Sample Features
Feature	Description
hair	Whether the animal has hair
feathers	Whether the animal has feathers
eggs	Whether the animal lays eggs
milk	Whether the animal produces milk
aquatic	Aquatic (1) or Terrestrial (0)
legs	Number of legs
class_type	Target class label (1–7 categories)

⚙️ Project Pipeline
Data Cleaning: Dropped animal_name, no missing values

EDA: Feature analysis and class distribution visualized

Preprocessing: No encoding or scaling needed

Model Selection: Tried DT, RF, SVM, KNN, LR

Model Training: Trained XGBoost with hyperparameters

Evaluation: Used Accuracy, Confusion Matrix, CV, ROC

Deployment: Streamlit app for prediction

📈 Model Selection
We experimented with multiple models:

Model	Accuracy
Decision Tree	100%
Random Forest	97%
Logistic Regression	97%
SVM	94%
KNN	91%
✅ XGBoost	100%

XGBoost was chosen for its:

High accuracy

Regularization to avoid overfitting

Speed and efficiency on small data

Robust handling of multiclass classification

🧪 Model Evaluation
Train/Test Accuracy: 100% on both

Confusion Matrix: Perfect classification (no errors)

Cross Validation: 5-Fold and Stratified CV confirmed stability

ROC Curve: AUC score ~1 for all classes

Interpretability: Clear decision boundaries from simple binary input

🚀 Deployment
The model is deployed using Streamlit, providing a user-friendly UI.

Features:
Users select animal features (checkboxes)

Real-time prediction of animal class

Instant, web-accessible interface

Run Locally:
bash
Copy
Edit
pip install -r requirements.txt
streamlit run app.py
📸 Sample Predictions
Example input:

ini
Copy
Edit
Milk = Yes
Feathers = No
Aquatic = No
Legs = 4
✅ Output: Mammal (Class 1)

📚 Future Scope
Add new features: habitat, diet, behavior

Use image-based classification with CNNs

Apply SHAP and LIME for explainable ML

Develop an educational app or quiz interface

Expand dataset with more real-world animals

Integrate voice-based input for accessibility

✅ Conclusion
XGBoost emerged as the best model, giving 100% accuracy and excellent generalization even on a small dataset. The use of only binary traits demonstrates that even simple features can yield powerful predictions. The model was thoroughly evaluated and successfully deployed as a live web app. This project highlights how ML can enhance biological classification and has great potential for educational and scientific use.

🛠️ Tech Stack
Python

Pandas, NumPy

XGBoost, Scikit-learn

Matplotlib, Seaborn

Streamlit

Git/GitHub

📎 References
Zoo Dataset – UCI Repository

XGBoost Documentation

Streamlit Documentation
