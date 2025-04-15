import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 10000

# Initialize data dictionary
data = {
    'temperature_c': np.random.normal(loc=28, scale=5, size=n_samples).clip(10, 45),
    'rainfall_cm_year': np.random.lognormal(mean=np.log(200), sigma=0.5, size=n_samples).clip(50, 500),
    'irrigation_available': np.random.binomial(1, 0.5, size=n_samples),
    'soil_type': np.random.choice(['Clay', 'Loam', 'Silt Clay', 'Sandy Loam', 'Alluvial', 'Sandy', 'Rocky'], 
                                  size=n_samples, p=[0.35, 0.25, 0.15, 0.1, 0.05, 0.05, 0.05]),
    'soil_ph': np.random.normal(loc=6.0, scale=1.0, size=n_samples).clip(3.5, 10.0),
    'soil_water_retention': np.random.normal(loc=40, scale=12, size=n_samples).clip(10, 60),
    'topography': np.random.choice(['Flat', 'Terraced', 'Gently Sloping', 'Steep'], 
                                   size=n_samples, p=[0.4, 0.3, 0.2, 0.1]),
    'sunlight_hours_day': np.random.normal(loc=8, scale=2, size=n_samples).clip(3, 12),
    'humidity_percent': np.random.normal(loc=80, scale=15, size=n_samples).clip(40, 100),
    'altitude_m': np.random.exponential(scale=400, size=n_samples).clip(0, 4000),
    'flooding_duration_days': np.random.normal(loc=80, scale=25, size=n_samples).clip(10, 150),
    'soil_nutrient_level': np.random.choice(['Low', 'Medium', 'High'], 
                                           size=n_samples, p=[0.3, 0.4, 0.3]),
    'drainage_capacity': np.random.choice(['Poor', 'Moderate', 'Good'], 
                                         size=n_samples, p=[0.3, 0.4, 0.3]),
    'temp_variation_c': np.random.normal(loc=5, scale=2.5, size=n_samples).clip(2, 15),
    'extreme_weather_events': np.random.poisson(lam=0.8, size=n_samples).clip(0, 5),
    'growing_season_days': np.random.normal(loc=120, scale=20, size=n_samples).clip(60, 200),
    'proximity_water_km': np.random.exponential(scale=15, size=n_samples).clip(0, 100),
    'wind_speed_ms': np.random.normal(loc=2, scale=1.2, size=n_samples).clip(0.5, 8),
    'pest_pressure': np.random.choice(['Low', 'Moderate', 'High'], 
                                     size=n_samples, p=[0.4, 0.4, 0.2]),
    'latitude_deg': np.random.normal(loc=20, scale=12, size=n_samples).clip(0, 50),
    'harsh_condition_type': np.random.choice(['None', 'Drought', 'Extreme Heat', 'Severe Flood', 'Storm', 'Poor Soil', 'Steep Terrain'], 
                                            size=n_samples, p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05])
}

# Create DataFrame
df = pd.DataFrame(data)

# Apply harsh conditions
for idx, harsh_type in enumerate(df['harsh_condition_type']):
    if harsh_type == 'Drought':
        df.loc[idx, 'rainfall_cm_year'] = np.random.uniform(50, 80)
        df.loc[idx, 'humidity_percent'] = np.random.uniform(40, 60)
    elif harsh_type == 'Extreme Heat':
        df.loc[idx, 'temperature_c'] = np.random.uniform(40, 45)
        df.loc[idx, 'temp_variation_c'] = np.random.uniform(8, 12)
    elif harsh_type == 'Severe Flood':
        df.loc[idx, 'rainfall_cm_year'] = np.random.uniform(400, 500)
        df.loc[idx, 'flooding_duration_days'] = np.random.uniform(120, 150)
    elif harsh_type == 'Storm':
        df.loc[idx, 'extreme_weather_events'] = np.random.randint(2, 5)
        df.loc[idx, 'wind_speed_ms'] = np.random.uniform(5, 8)
    elif harsh_type == 'Poor Soil':
        df.loc[idx, 'soil_ph'] = np.random.choice([np.random.uniform(3.5, 4.5), np.random.uniform(9, 10)])
        df.loc[idx, 'soil_water_retention'] = np.random.uniform(10, 20)
        df.loc[idx, 'soil_nutrient_level'] = 'Low'
    elif harsh_type == 'Steep Terrain':
        df.loc[idx, 'topography'] = 'Steep'

# Add noise to numeric columns
noise_levels = {
    'temperature_c': 0.5,
    'rainfall_cm_year': 5,
    'soil_ph': 0.1,
    'soil_water_retention': 2,
    'sunlight_hours_day': 0.2,
    'humidity_percent': 3,
    'altitude_m': 50,
    'flooding_duration_days': 5,
    'temp_variation_c': 0.3,
    'growing_season_days': 5,
    'proximity_water_km': 2,
    'wind_speed_ms': 0.2,
    'latitude_deg': 1
}

for col, noise_std in noise_levels.items():
    df[col] += np.random.normal(loc=0, scale=noise_std, size=n_samples)
    # Re-apply clipping to ensure values stay within realistic bounds
    if col == 'temperature_c':
        df[col] = df[col].clip(10, 45)
    elif col == 'rainfall_cm_year':
        df[col] = df[col].clip(50, 500)
    elif col == 'soil_ph':
        df[col] = df[col].clip(3.5, 10.0)
    elif col == 'soil_water_retention':
        df[col] = df[col].clip(10, 60)
    elif col == 'sunlight_hours_day':
        df[col] = df[col].clip(3, 12)
    elif col == 'humidity_percent':
        df[col] = df[col].clip(40, 100)
    elif col == 'altitude_m':
        df[col] = df[col].clip(0, 4000)
    elif col == 'flooding_duration_days':
        df[col] = df[col].clip(10, 150)
    elif col == 'temp_variation_c':
        df[col] = df[col].clip(2, 15)
    elif col == 'growing_season_days':
        df[col] = df[col].clip(60, 200)
    elif col == 'proximity_water_km':
        df[col] = df[col].clip(0, 100)
    elif col == 'wind_speed_ms':
        df[col] = df[col].clip(0.5, 8)
    elif col == 'latitude_deg':
        df[col] = df[col].clip(0, 50)

# Add noise to extreme_weather_events (random flip with 5% chance)
for idx in range(n_samples):
    if np.random.random() < 0.05:
        df.loc[idx, 'extreme_weather_events'] = np.random.randint(0, 5)

# Generate general suitability label with corrected operator precedence
df['suitability'] = (
    (df['temperature_c'].between(20, 37)) &
    (((df['rainfall_cm_year'] >= 100) | (df['irrigation_available'] == 1))) &
    (df['soil_ph'].between(5, 8)) &
    (df['sunlight_hours_day'] >= 6) &
    (df['topography'].isin(['Flat', 'Terraced'])) &
    (df['flooding_duration_days'].between(50, 120)) &
    (df['soil_nutrient_level'] != 'Low') &
    (df['drainage_capacity'] != 'Poor') &
    (df['extreme_weather_events'] <= 1)
).astype(int)

# Set suitability to 0 for harsh conditions
df.loc[df['harsh_condition_type'] != 'None', 'suitability'] = 0

# Generate 'is_perfect_weather' label
df['is_perfect_weather'] = (
    (df['temperature_c'].between(25, 33)) &
    (df['rainfall_cm_year'].between(175, 300)) &
    (df['humidity_percent'].between(75, 90)) &
    (df['sunlight_hours_day'].between(8, 10)) &
    (df['temp_variation_c'].between(3, 6)) &
    (df['extreme_weather_events'] == 0) &
    (df['wind_speed_ms'].between(1, 3))
).astype(int)

# Save to CSV
df.to_csv('data/rice_synthetic_data.csv', index=False)

# Print dataset summary
print("Dataset Summary:")
print(df.describe())

# Print dataset info
print("\nDataset Info:")
print(df.info())

# Print first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Preview distributions
print(df.head())
print("\nSuitability Distribution:")
print(df['suitability'].value_counts())
print("\nPerfect Weather Distribution:")
print(df['is_perfect_weather'].value_counts())
print("\nHarsh Condition Distribution:")
print(df['harsh_condition_type'].value_counts())