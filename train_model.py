import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).parent
data = pd.read_csv(ROOT / "house_prices_sample.csv")
features = ["location", "area_sqft", "bhk", "bathrooms", "property_age_years", "floor", "parking"]
target = "price_lakhs"
categorical = ["location"]
numeric = [c for c in features if c not in categorical]

preprocessor = ColumnTransformer([
    ("categorical", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical),
    ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median"))]), numeric)
])
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=220, random_state=42, min_samples_leaf=2))
])

X_train, X_test, y_train, y_test = train_test_split(
    data[features], data[target], test_size=0.2, random_state=42
)
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
print(f"Mean Absolute Error: ₹{mean_absolute_error(y_test, predictions):.2f} lakh")
print(f"R² score: {r2_score(y_test, predictions):.3f}")
joblib.dump(pipeline, ROOT / "house_price_model.joblib")
print("Saved house_price_model.joblib")
