import joblib
import numpy as np

# Load the trained model
model = joblib.load('attrition_model.pkl')

def predict(input_data):
    input_data = np.array(input_data).reshape(1, -1)
    
    prediction = model.predict(input_data)
    return prediction[0]


example_input_from_dataset = [0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0] 

result = predict(example_input_from_dataset)
print(f"Predicted Attrition (Untuk label sesungguhnya no): {'Yes' if result == 1 else 'No'}")
