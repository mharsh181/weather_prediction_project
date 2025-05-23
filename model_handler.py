import joblib
import pandas as pd
import numpy as np

class WeatherPredictor:
    def __init__(self):
        self.temp_model = joblib.load('temperature_model.pkl')
        self.et0_model = joblib.load('et0_model.pkl')
        self.feature_order = [
            'month', 'temp_lag1', 'temp_lag2', 'precipitation_sum',
            'season_Winter', 'season_Spring', 'season_Summer', 'season_Fall'
        ]
        
    def preprocess_input(self, new_data):
        """Prepare input data for prediction"""
        new_data['time'] = pd.to_datetime(new_data['time'])
        new_data['month'] = new_data['time'].dt.month
        
        # Generate lag features
        new_data['temp_lag1'] = new_data['temperature_2m_mean'].shift(1)
        new_data['temp_lag2'] = new_data['temperature_2m_mean'].shift(2)
        
        # Generate seasonal dummies
        new_data = pd.get_dummies(new_data, columns=['season'])
        
        # Ensure all required columns exist
        for col in self.feature_order:
            if col not in new_data.columns:
                new_data[col] = 0
                
        return new_data[self.feature_order].iloc[-1:].fillna(0)

    def predict_temperature(self, input_data):
        processed_data = self.preprocess_input(input_data)
        return self.temp_model.predict(processed_data)[0]
    
    def predict_et0(self, input_data):
        required_features = ['temperature_2m_mean', 
                           'shortwave_radiation_sum',
                           'windspeed_10m_max',
                           'month']
        input_data['month'] = pd.to_datetime(input_data['time']).dt.month
        return self.et0_model.predict(input_data[required_features])[0]