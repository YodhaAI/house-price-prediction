🏡 House Price Prediction

A Machine Learning project for predicting house prices using regression models (Random Forest, Decision Tree).
This project includes data preprocessing, feature engineering, model training, hyperparameter tuning, and a Flask web app for deployment.

📌 Features

Data preprocessing and cleaning

Feature engineering and selection

Model training (Random Forest, Decision Tree)

Hyperparameter tuning for better performance

Flask API for deployment

HTML frontend for user interaction

🚀 Tech Stack

Python 3

Flask (API & Web deployment)

Scikit-learn (ML models)

Pandas & NumPy (data preprocessing)

HTML/CSS (frontend)

📂 Project Structure
house-price-prediction/
│── app.py                  # Flask app for deployment
│── houseprice.ipynb        # Jupyter Notebook with ML workflow
│── index.html              # Frontend HTML file
│── best_random_forest_model.pkl   # Trained model
│── rf_tuned_model.pkl      # Tuned Random Forest model
│── model_features.pkl      # Feature set
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation
│── LICENSE                 # MIT License

⚙️ Installation & Usage

1️⃣ Clone this repository:

git clone https://github.com/YodhaAI/house-price-prediction.git
cd house-price-prediction


2️⃣ Install dependencies:

pip install -r requirements.txt


3️⃣ Run the Flask app:

python app.py


4️⃣ Open in browser:

http://127.0.0.1:5000

📊 Dataset

The model was trained on a housing dataset (e.g., Kaggle Ames Housing Dataset).
You can replace it with your own dataset for customization.

📸 Demo

👉 (<img width="406" height="424" alt="Screenshot 2025-09-02 120554" src="https://github.com/user-attachments/assets/9635f388-335f-446c-9cf7-7cbb2f603a5e" />)

🔮 Future Improvements

Deploy app on Heroku/Render/Streamlit

Add more ML models (XGBoost, LightGBM)

Improve UI with Bootstrap or React

Create an API endpoint for external apps

📜 License

This project is licensed under the MIT License – feel free to use and modify.

⚡ Created with ❤️ by Aryan Singh Rajput
