import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter1d

# Set random seed for reproducibility
np.random.seed(42)

def add_weather_persistence(data, correlation_strength=0.7):
    """Add temporal correlation to weather data"""
    smooth_data = gaussian_filter1d(data, sigma=2)
    noise = np.random.normal(0, 1, len(data))
    return smooth_data * correlation_strength + data * (1 - correlation_strength)

def generate_extreme_events(data, base_probability=0.05, season=None):
    """Generate clustered extreme events with seasonal variation"""
    season_multipliers = {
        'pre-kharif': 1.2,  # More extreme events in pre-monsoon
        'kharif': 0.8,      # Fewer extremes during monsoon
        'rabi': 1.0         # Base probability in winter
    }
    
    probability = base_probability * season_multipliers.get(season, 1.0)
    extreme_mask = np.random.random(len(data)) < probability
    
    # Create clusters of extreme events
    for i in range(1, len(extreme_mask)-1):
        if extreme_mask[i-1]:
            extreme_mask[i] = np.random.random() < 0.3
    
    return extreme_mask

def add_variable_correlations(day_temp, night_temp, sunshine_hours, rainfall):
    """Add realistic correlations between weather variables"""
    # Temperature difference affects rainfall
    temp_diff = day_temp - night_temp
    rainfall_modifier = 1 - (temp_diff - np.min(temp_diff)) / (np.max(temp_diff) - np.min(temp_diff))
    rainfall *= rainfall_modifier * 0.7 + 0.3  # Preserve some randomness
    
    # Rainfall affects sunshine hours
    sunshine_modifier = 1 - (rainfall / np.max(rainfall)) * 0.6
    sunshine_hours *= sunshine_modifier
    
    # Ensure night temp stays below day temp
    night_temp = np.minimum(night_temp, day_temp - 2)
    
    return day_temp, night_temp, sunshine_hours, rainfall

# Define the number of samples (days)
num_samples = 100000

# Define seasons and their probabilities
seasons = ['pre-kharif', 'kharif', 'rabi']
season_probs = [0.3, 0.4, 0.3]

# Enhanced season-specific parameters
season_params = {
    'pre-kharif': {
        'day_temp_mean': 30, 'day_temp_std': 3,
        'night_temp_mean': 22, 'night_temp_std': 1.5,
        'sunshine_hours_mean': 8, 'sunshine_hours_std': 2,
        'rainfall_prob': 0.4, 'rainfall_mean': 10, 'rainfall_std': 5,
        'extreme_temp_range': (-6, 6),
        'extreme_rain_multiplier': (0.3, 2.5)
    },
    'kharif': {
        'day_temp_mean': 28, 'day_temp_std': 2,
        'night_temp_mean': 21.5, 'night_temp_std': 1,
        'sunshine_hours_mean': 7, 'sunshine_hours_std': 1.5,
        'rainfall_prob': 0.6, 'rainfall_mean': 15, 'rainfall_std': 7,
        'extreme_temp_range': (-4, 4),
        'extreme_rain_multiplier': (0.4, 2.2)
    },
    'rabi': {
        'day_temp_mean': 25, 'day_temp_std': 2.5,
        'night_temp_mean': 20, 'night_temp_std': 1.2,
        'sunshine_hours_mean': 9, 'sunshine_hours_std': 2,
        'rainfall_prob': 0.3, 'rainfall_mean': 5, 'rainfall_std': 3,
        'extreme_temp_range': (-5, 5),
        'extreme_rain_multiplier': (0.2, 1.8)
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
    
    # Generate base weather patterns
    day_temp[season_mask] = np.random.normal(
        params['day_temp_mean'], 
        params['day_temp_std'], 
        sum(season_mask)
    )
    night_temp[season_mask] = np.random.normal(
        params['night_temp_mean'], 
        params['night_temp_std'], 
        sum(season_mask)
    )
    sunshine_hours[season_mask] = np.random.normal(
        params['sunshine_hours_mean'], 
        params['sunshine_hours_std'], 
        sum(season_mask)
    )
    
    # Enhanced rainfall generation
    rain_days = np.random.binomial(1, params['rainfall_prob'], sum(season_mask))
    rainfall_amount = np.random.normal(
        params['rainfall_mean'], 
        params['rainfall_std'], 
        sum(season_mask)
    )
    rainfall[season_mask] = rain_days * rainfall_amount
    
    # Add weather persistence
    day_temp[season_mask] = add_weather_persistence(day_temp[season_mask])
    night_temp[season_mask] = add_weather_persistence(night_temp[season_mask])
    rainfall[season_mask] = add_weather_persistence(rainfall[season_mask])
    
    # Generate and apply extreme events
    extreme_mask = generate_extreme_events(
        day_temp[season_mask], 
        base_probability=0.05, 
        season=season
    )
    
    # Apply extreme events with season-specific ranges
    day_temp[season_mask][extreme_mask] += np.random.uniform(
        params['extreme_temp_range'][0],
        params['extreme_temp_range'][1],
        sum(extreme_mask)
    )
    night_temp[season_mask][extreme_mask] += np.random.uniform(
        params['extreme_temp_range'][0]*0.6,
        params['extreme_temp_range'][1]*0.6,
        sum(extreme_mask)
    )
    rainfall[season_mask][extreme_mask] *= np.random.uniform(
        params['extreme_rain_multiplier'][0],
        params['extreme_rain_multiplier'][1],
        sum(extreme_mask)
    )
    
    # Apply correlations between variables
    day_temp[season_mask], night_temp[season_mask], \
    sunshine_hours[season_mask], rainfall[season_mask] = \
        add_variable_correlations(
            day_temp[season_mask],
            night_temp[season_mask],
            sunshine_hours[season_mask],
            rainfall[season_mask]
        )

# Final cleanup and constraints
day_temp = np.round(day_temp, 1)
night_temp = np.round(night_temp, 1)
sunshine_hours = np.clip(sunshine_hours, 0, 12)
rainfall = np.clip(rainfall, 0, None)

# Validate physical constraints
assert np.all(night_temp <= day_temp), "Night temperatures exceed day temperatures"
assert np.all(sunshine_hours >= 0) and np.all(sunshine_hours <= 12), "Invalid sunshine hours"
assert np.all(rainfall >= 0), "Negative rainfall values"

# Define suitability conditions with more granular thresholds
day_temp_condition = (day_temp >= 20) & (day_temp <= 36)
night_temp_condition = (night_temp >= 20) & (night_temp <= 23)
sunshine_condition = sunshine_hours >= 6
rainfall_condition = (rainfall >= 2) & (rainfall <= 30)

# Determine suitability
suitable = day_temp_condition & night_temp_condition & sunshine_condition & rainfall_condition
suitability = np.where(suitable, "suitable", "unsuitable")

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
print("Enhanced daily dataset generated and saved as 'data/rice_cultivation_daily_dataset.csv'.")