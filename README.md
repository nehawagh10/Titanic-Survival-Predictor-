# 🚢 Titanic Survival Prediction — Logistic Regression

This project predicts whether a Titanic passenger would have survived using Logistic Regression and displays results in a Streamlit web app.

## 📂 Project Files
- **Logistic Regression -Titanic_train.ipynb** — Model training notebook
- **Logistic Regression-Titanic test.ipynb** — Model testing notebook
- **Titanic_train.csv** — Training dataset
- **Titanic_test.csv** — Test dataset
- **app.py** — Streamlit app for predictions
- **logistic_model.pkl** — Saved trained model

## ⚙️ How to Run (Anaconda Prompt)

1️⃣ **Open Anaconda Prompt**  
From your Start menu, search and open **Anaconda Prompt**.

2️⃣ **Navigate to your project folder**  
Example (if your folder is in `Documents`):
```
cd Documents\Titanic-Logistic-Regression
```

3️⃣ **Create a virtual environment** (optional but recommended):
```
conda create --name titanic_env python=3.9
```

4️⃣ **Activate the environment**:
```
conda activate titanic_env
```

5️⃣ **Install dependencies**:
```
pip install pandas numpy scikit-learn streamlit
```

6️⃣ **Run the Streamlit app**:
```
streamlit run app.py
```

7️⃣ The app will open in your default browser at:
```
http://localhost:8501
```

---

## 🧠 Model Details
- Algorithm: Logistic Regression
- Features used: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
- Preprocessing: Label encoding for categorical features


## 📬 Author
**Neha Wagh**
