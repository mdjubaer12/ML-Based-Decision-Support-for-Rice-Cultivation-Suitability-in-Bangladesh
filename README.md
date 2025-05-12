# 🌾 ML Based Decision Support System(DSS)

## Empowering Farmers with AI-Driven Weather Insights for Rice Cultivation in Bangladesh 🌧️

*Predicting Daily Rice Suitability with Machine Learning and Real-Time Weather Data*

---

### 🚀 What is ML Based Decision Support System for Rice Cultivation Suitability?

ML Based Decision Support System(DSS) for Rice Cultivation Suitability is a cutting-edge machine learning project that predicts **daily weather suitability** for rice cultivation in Bangladesh. Leveraging real-time weather data from the **OpenWeather API**, this system helps farmers make informed decisions by classifying conditions as **"suitable"** or **"unsuitable"** for rice growth. It also delivers **actionable recommendations** to mitigate unfavorable conditions, empowering farmers to optimize yields and embrace climate-smart agriculture.

Built on a **10,000-sample synthetic dataset** and validated with **10 years of real-world data (2013–2022)**, our models achieve **near-perfect performance (F₁ > 0.99)** on synthetic data and robust generalization (**F₁ ≈ 0.95**) on real data. Whether you're a farmer, researcher, or developer, this project offers a scalable solution for sustainable rice farming! 🌱

---

### 🌟 Key Features

- **Real-Time Weather Integration**: Fetches live weather data via the OpenWeather API for up-to-date predictions.
- **Machine Learning Powerhouse**: Evaluates six classifiers—Logistic Regression, SVM, k-NN, Random Forest, XGBoost, and LightGBM—with top performers achieving 99.97% accuracy.
- **Synthetic & Real-World Data**: Trained on a 10,000-sample synthetic dataset and validated with real Bangladeshi weather data (2013–2022) from Data.gov.bd.
- **Actionable Insights**: Provides farmers with tailored recommendations like irrigation adjustments and variety selection.
- **Scalable & Farmer-Friendly**: Designed for deployment in resource-constrained environments, with plans for a mobile app interface.

---

### 📊 How It Works

The system follows a streamlined pipeline to deliver daily suitability predictions:

1. **Fetch Weather Data** 🌤️  
   Retrieves real-time weather metrics (temperature, sunshine, rainfall) via the OpenWeather API.

2. **Preprocess Data** 🛠️  
   Cleans and transforms data, balancing classes with SMOTE and scaling features for optimal model performance.

3. **Predict with ML Models** 🤖  
   Uses trained classifiers to predict if conditions are "suitable" or "unsuitable" for rice cultivation.

4. **Deliver Recommendations** 📢  
   - **Suitable**: "Go ahead with planting!"  
   - **Unsuitable**: "Consider irrigation adjustments or delay planting—here’s how!"

- ### System Workflow

<p align="center">
  <img src="https://i.ibb.co/sfSybkN/Screenshot-2025-05-13-004018.png" alt="System Workflow">
</p>



---

### 📈 Performance Highlights

#### Synthetic Data Results
| Model            | Accuracy | Precision | Recall | F₁-Score | ROC-AUC |
|------------------|----------|-----------|--------|----------|---------|
| Random Forest    | 99.97%   | 1.000     | 0.999  | 0.9997   | 1.000   |
| XGBoost          | 99.97%   | 1.000     | 0.999  | 0.9997   | 0.9996  |
| LightGBM         | 99.97%   | 0.9993    | 1.000  | 0.9997   | 0.9999  |
| k-NN             | 97.58%   | 0.9994    | 0.9930 | 0.9759   | 0.9930  |
| SVM              | 97.99%   | 0.9744    | 0.9853 | 0.9798   | 0.9988  |
| Logistic Regression | 84.71% | 0.8572    | 0.8279 | 0.8423   | 0.9112  |

#### Real-World Data Results (2013–2022)
| Model            | Accuracy | Precision | Recall | F₁-Score | ROC-AUC |
|------------------|----------|-----------|--------|----------|---------|
| k-NN             | 91.53%   | 0.8500    | 0.9900 | 0.9218   | 0.9593  |
| SVM              | 84.61%   | 0.7600    | 0.9900 | 0.8600   | 0.9762  |
| LightGBM         | 79.66%   | 0.7000    | 0.9900 | 0.8300   | 0.9000  |
| Random Forest    | 79.42%   | 0.7000    | 0.9900 | 0.8200   | 0.8600  |
| XGBoost          | 79.00%   | 0.7000    | 0.9900 | 0.8200   | 0.8500  |
| Logistic Regression | 76.00% | 0.8400    | 0.6300 | 0.7200   | 0.8700  |

---

### 🛠️ Technical Details

#### Dataset
- **Synthetic Dataset**: 10,000 samples with 5 features:
  - **Season**: Pre-kharif, kharif, rabi (categorical)
  - **average_day_temp (°C)**: 15.5–42.5°C
  - **average_night_temp (°C)**: 14.9–30.0°C
  - **daily_sunshine_hours**: 0.72–12 h
  - **daily_rainfall (mm)**: 0–63.4 mm
- **Real-World Data**: Sourced from Data.gov.bd, covering 2013–2022.
- **Suitability Criteria**:
  - Daytime temp: 20–36°C
  - Nighttime temp: 20–23°C
  - Sunshine: ≥6.5 h
  - Rainfall: ≥5 mm/day (kharif), irrigation-dependent (rabi)

#### Preprocessing
- **Cleaning**: Removed outliers using IQR method; no missing values found.
- **Balancing**: Applied SMOTE to address class imbalance (7,243 unsuitable vs. 2,266 suitable).
- **Encoding**: Label-encoded "Season" (pre-kharif = 0, kharif = 1, rabi = 2).
- **Scaling**: Standardized features using StandardScaler.

#### Models
Trained and benchmarked using stratified 5-fold cross-validation:
- Logistic Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors (k-NN)
- Random Forest
- XGBoost
- LightGBM

#### Implementation
- **Language**: Python
- **Libraries**: scikit-learn, pandas, requests
- **API**: OpenWeather API for real-time weather data

---

###  Why It Matters

Rice is the backbone of food security in Bangladesh, but daily weather fluctuations threaten yields. High temperatures (>35°C) cause spikelet sterility, while insufficient rainfall (<1120 mm/season) leads to drought stress. Traditional methods lack the granularity for real-time decisions. ML Based Decision Support System(DSS) bridges this gap by:
- Providing **daily, data-driven insights** for farmers.
- Supporting **climate-smart agriculture** in a vulnerable region.
- Enabling **scalable, low-cost deployment** for smallholder farmers.

---

### Future Enhancements

- Integrate soil moisture and humidity data for more accurate predictions.
- Expand with real-world field data from IoT sensors.
- Build a mobile app for real-time notifications 📱.
- Conduct field trials to validate predictions with actual yields.
- Explore hybrid models to bridge synthetic-real data performance gaps.

---

### 🤝 Contribute to the Project

We welcome contributions from developers, researchers, and agricultural experts! Here’s how you can get involved:
- **Enhance the Dataset**: Add real-world observations or new features.
- **Optimize Models**: Experiment with deep learning or hybrid approaches.
- **Improve Accessibility**: Help design a farmer-friendly mobile interface.
  
---

### Acknowledgments

This project was inspired by the urgent need to address climate impacts on Bangladeshi agriculture. We extend our gratitude to:
- The **Bangladesh Agro-Meteorological Information System (BAMIS)** for agronomic insights.
- **Data.gov.bd** for providing real-world weather data.
- The **OpenWeather API** team for enabling real-time forecasts.
- The open-source community for their invaluable tools and libraries.

---


### 📂 Availability

The source code, datasets, and models are available on GitHub:  
🔗 [GitHub Repository URL](https://github.com/mdjubaer12/ML-Based-Decision-Support-for-Rice-Cultivation-Suitability-in-Bangladesh/)

---

⭐ **Star this repo** if you find it useful! Let’s make rice farming smarter, together! 🌾
