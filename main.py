from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import pickle

# Load the trained model (ensure this file exists)
with open("model_car_best.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI
app = FastAPI()

# Define the input data schema
class CarFeatures(BaseModel):
    Manufacturer: int
    Model: int
    Prod_year: int
    Category: int
    Leather_interior: int
    Engine_volume: float
    Mileage: int
    Cylinders: float
    Doors: int
    Wheel: int
    Color: int
    Airbags: int
    Drive_4x4: bool
    Drive_Front: bool
    Drive_Rear: bool
    Gear_Automatic: bool
    Gear_Manual: bool
    Gear_Tiptronic: bool
    Gear_Variator: bool
    Fuel_CNG: bool
    Fuel_Diesel: bool
    Fuel_Hybrid: bool
    Fuel_Hydrogen: bool
    Fuel_LPG: bool
    Fuel_Petrol: bool
    Fuel_Plug_in_Hybrid: bool

# Prediction endpoint
@app.post("/predict/")
def predict_price(car: CarFeatures):
    # Convert input into a numpy array
    input_data = np.array([[
        car.Manufacturer, car.Model, car.Prod_year, car.Category,
        car.Leather_interior, car.Engine_volume, car.Mileage, 
        car.Cylinders, car.Doors, car.Wheel, car.Color, car.Airbags,
        car.Drive_4x4, car.Drive_Front, car.Drive_Rear,
        car.Gear_Automatic, car.Gear_Manual, car.Gear_Tiptronic, car.Gear_Variator,
        car.Fuel_CNG, car.Fuel_Diesel, car.Fuel_Hybrid, car.Fuel_Hydrogen,
        car.Fuel_LPG, car.Fuel_Petrol, car.Fuel_Plug_in_Hybrid
    ]])

    # Make a prediction
    predicted_log_price = float(model.predict(input_data)[0])
    predicted_price=np.expm1(predicted_log_price)

    # Return the predicted price
    return {"Predicted Price": predicted_price}
