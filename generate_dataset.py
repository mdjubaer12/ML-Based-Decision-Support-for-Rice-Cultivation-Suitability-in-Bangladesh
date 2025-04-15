import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define the number of samples (days)
num_samples = 10000

# Define seasons and their probabilities
seasons = ['pre-kharif', 'kharif', 'rabi']
season_probs = [0.3, 0.4, 0.3]

# Season-specific parameters for daily data
season_params = {
    'pre-kharif': {
        'day_temp_mean': 30, 'day_temp_std': 3,       # Daily avg day temp (°C)
        'night_temp_mean': 22, 'night_temp_std': 1.5, # Daily avg night temp (°C)
        'sunshine_hours_mean': 8, 'sunshine_hours_std': 2,  # Daily sunshine (hours)
        'rainfall_prob': 0.4, 'rainfall_mean': 10, 'rainfall_std': 5  # Daily rainfall (mm)
    },
    'kharif': {
        'day_temp_mean': 28, 'day_temp_std': 2,
        'night_temp_mean': 21.5, 'night_temp_std': 1,
        'sunshine_hours_mean': 7, 'sunshine_hours_std': 1.5,
        'rainfall_prob': 0.6, 'rainfall_mean': 15, 'rainfall_std': 7
    },
    'rabi': {
        'day_temp_mean': 25, 'day_temp_std': 2.5,
        'night_temp_mean': 20, 'night_temp_std': 1.2,
        'sunshine_hours_mean': 9, 'sunshine_hours_std': 2,
        'rainfall_prob': 0.3, 'rainfall_mean': 5, 'rainfall_std': 3
    }
}

# Generate season for each sample
season_data = np.random.choice(seasons, size=num_samples, p=season_probs)

# Initialize arrays
day_temp = np.zeros(num_samples)
night_temp = np.zeros(num_samples)
sunshine_hours = np.zeros(num_samples)
rainfall = np.zeros(num_samples)

# Generate daily data based on season
for season in seasons:
    season_mask = season_data == season
    params = season_params[season]
    
    # Daily temperatures with normal distribution
    day_temp[season_mask] = np.random.normal(params['day_temp_mean'], params['day_temp_std'], sum(season_mask))
    night_temp[season_mask] = np.random.normal(params['night_temp_mean'], params['night_temp_std'], sum(season_mask))
    
    # Daily sunshine hours with normal distribution
    sunshine_hours[season_mask] = np.random.normal(params['sunshine_hours_mean'], params['sunshine_hours_std'], sum(season_mask))
    
    # Daily rainfall: Bernoulli for rain/no-rain, then normal for amount on rainy days
    rain_days = np.random.binomial(1, params['rainfall_prob'], sum(season_mask))
    rainfall_amount = np.random.normal(params['rainfall_mean'], params['rainfall_std'], sum(season_mask))
    rainfall[season_mask] = rain_days * rainfall_amount

# Add measurement noise to temperatures
day_temp += np.random.normal(0, 0.5, num_samples)
night_temp += np.random.normal(0, 0.5, num_samples)

# Introduce extreme events (5% of samples)
extreme_indices = np.random.choice(num_samples, size=int(0.05 * num_samples), replace=False)
for idx in extreme_indices:
    if np.random.rand() < 0.5:
        # Extreme temperature
        day_temp[idx] += np.random.choice([-5, 5])
        night_temp[idx] += np.random.choice([-3, 3])
    else:
        # Extreme rainfall
        rainfall[idx] *= np.random.choice([0.5, 2])  # Halve or double rainfall

# Round temperatures to one decimal place
day_temp = np.round(day_temp, 1)
night_temp = np.round(night_temp, 1)

# Ensure sunshine hours are between 0 and 12, rainfall is non-negative
sunshine_hours = np.clip(sunshine_hours, 0, 12)
rainfall = np.clip(rainfall, 0, None)

# Define daily suitability conditions
day_temp_condition = (day_temp >= 20) & (day_temp <= 36)
night_temp_condition = (night_temp >= 20) & (night_temp <= 23)
sunshine_condition = sunshine_hours >= 6
rainfall_condition = (rainfall >= 2) & (rainfall <= 30)

# Determine labels
suitable = day_temp_condition & night_temp_condition & sunshine_condition & rainfall_condition
suitability = np.where(suitable, "suitable", "not suitable")

# Create DataFrame
df = pd.DataFrame({
    "season": season_data,
    "average_day_temp": day_temp,
    "average_night_temp": night_temp,
    "daily_sunshine_hours": sunshine_hours,
    "daily_rainfall": rainfall,
    "suitability": suitability
})

# Save to CSV
df.to_csv("data/rice_cultivation_daily_dataset.csv", index=False)

print("Daily dataset generated and saved as 'data/rice_cultivation_daily_dataset.csv'.")