# 🧠 Animal Species Classification using XGBoost

A machine learning project that classifies animals into biological classes based on physical and behavioral traits like “milk,” “legs,” and “feathers” — using only binary inputs and the powerful XGBoost algorithm.

---

## 📌 Table of Contents
- [🔍 Project Overview](#-project-overview)  
- [🎯 Problem Statement](#-problem-statement)  
- [📊 Dataset Details](#-dataset-details)  
- [⚙️ Project Workflow](#️-project-workflow)  
- [🤖 Model Selection](#-model-selection)  
- [🧪 Evaluation Metrics](#-evaluation-metrics)  
- [🚀 Deployment](#-deployment)  
- [🐾 Example Predictions](#-example-predictions)  
- [🔮 Future Scope](#-future-scope)  
- [✅ Conclusion](#-conclusion)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📚 References](#-references)

---

## 🔍 Project Overview

This project focuses on predicting the biological class of animals using only **binary physical and behavioral traits**.  
It avoids using species names or textual descriptions and instead classifies based on traits like **feathers, milk, aquatic**, and **legs**.  
The model of choice — **XGBoost** — provided an impressive **100% accuracy**, making it the best candidate for final deployment.  
The final model is deployed using a **Streamlit web app** for real-time, user-friendly predictions.

---

## 🎯 Problem Statement

Can we classify animals without knowing their name or species?  
Yes — by analyzing just **16 binary features**, we can categorize animals into one of **seven biological classes** like Mammals, Birds, and Reptiles.  
The project frames this as a **multi-class classification** problem, focusing on developing a fast, accurate, and lightweight ML model.  
This system can simplify classification for educational, scientific, and research-based platforms.

---

## 📊 Dataset Details

- **Dataset:** [Zoo Dataset – UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Zoo)  
- **Instances:** 101 animals  
- **Features:** 16 binary traits (e.g., hair, feathers, milk, eggs, legs)  
- **Target Variable:** `class_type` — values from 1 to 7

### 🔎 Example Features
| Feature        | Description                          |
|----------------|--------------------------------------|
| `hair`         | Has hair or not (1/0)                |
| `feathers`     | Has feathers or not (1/0)            |
| `milk`         | Produces milk or not (1/0)           |
| `aquatic`      | Lives in water or not (1/0)          |
| `legs`         | Number of legs (0–8)                 |
| `class_type`   | Animal class (Mammal, Bird, etc.)    |

---

## ⚙️ Project Workflow

1. **Data Cleaning:** Dropped irrelevant column (`animal_name`), verified no missing values.  
2. **EDA:** Explored features and class distribution via bar plots and pairplots.  
3. **Preprocessing:** Minimal work required — all features are already binary.  
4. **Model Comparison:** Tested several models including Decision Tree, Random Forest, SVM, etc.  
5. **Model Training:** Selected XGBoost due to top-tier performance and robustness.  
6. **Evaluation:** Performed cross-validation, confusion matrix, and ROC AUC scoring.  
7. **Deployment:** Built a real-time prediction interface using Streamlit.

---

## 🤖 Model Selection

### 🧪 Models Tested:
| Model                 | Accuracy |
|----------------------|----------|
| Decision Tree         | 100%     |
| Random Forest         | 97%      |
| Logistic Regression   | 97%      |
| SVM                   | 94%      |
| KNN                   | 91%      |
| ✅ **XGBoost**         | **100%** |

**Why XGBoost?**  
XGBoost outperformed all other models and provided perfect accuracy even on unseen data.  
Its ability to avoid overfitting through **built-in regularization** made it ideal for this small and clean dataset.

---

## 🧪 Evaluation Metrics

To ensure robustness, we validated the XGBoost model using multiple metrics:

- **Training & Test Accuracy:** 100%  
- **Cross-Validation:** 5-Fold and Stratified CV showed stable results  
- **Confusion Matrix:** Zero misclassifications across all 7 classes  
- **ROC-AUC Score:** Close to 1.0 for each class — very strong confidence  
- **Overfitting Check:** Model generalizes well due to tree boosting and regularization

---

## 🚀 Deployment

The trained model is deployed using **Streamlit**, providing a browser-based UI for end-users.  
Users can interactively select features (via checkboxes and dropdowns) and get instant animal class predictions.

### ▶ How to Run Locally:
```bash
git clone https://github.com/your-username/animal-xgboost-classifier
cd animal-xgboost-classifier
pip install -r requirements.txt
streamlit run app.py
