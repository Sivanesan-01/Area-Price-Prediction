import streamlit as st
import pickle

# Load the model from the pickle file
with open('area_price_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Function to predict price based on area input
def predict_price(area):
    area = [[area]]  # Convert to 2D array
    return loaded_model.predict(area)[0]

# Streamlit App Interface
def main():
    st.title("Area Price Prediction")

    # User input
    area = st.number_input("Enter the area in square feet", min_value=0)

    # Predict button
    if st.button("Predict"):
        try:
            predicted_price = predict_price(area)
            st.success(f'Predicted price for {area} sqft: ${predicted_price:.2f}')
        except ValueError:
            st.error("Please enter a valid numeric value for area.")

if __name__ == '__main__':
    main()
