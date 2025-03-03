Car Price Prediction API

Project Overview

This project involves building a car price prediction model and deploying it as an API using FastAPI. The API takes car features as input and returns the predicted price.

Technologies Used

Python

FastAPI

Scikit-learn

Pandas

NumPy

GitHub

Project Structure

Car_price/
│── model_car_besk.pkl        # Contains trained ML model
├── main.py                   # FastAPI application
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
│── .gitignore                # Ignore unnecessary files

Setup and Installation

Clone the repository:

git clone <repo_url>
cd car-price-prediction

Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the FastAPI application:

uvicorn src.main:app --reload

API Endpoints

POST /predict

Description: Predicts the price of a car based on input features.

Request Body:

![image](https://github.com/user-attachments/assets/6d81a1d2-648b-4dc6-b292-42fb94c5ecb9)

Response:

![image](https://github.com/user-attachments/assets/2f653ba8-afdd-4556-b291-91cbd9efc79c)


Deployment using Render
![image](https://github.com/user-attachments/assets/c5a9b4d1-4fd8-400a-8eef-10f51d31ed0e)





