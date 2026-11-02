# Homiq: House Price Prediction Website

A complete local website using Flask + HTML/CSS/JavaScript and a trained Scikit-learn model.

## Run on your computer
1. Install Python 3.10 or newer.
2. Extract this ZIP and open the extracted folder in VS Code.
3. Open Terminal in that folder.
4. (Recommended) Create a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Start the website: `python app.py`
7. Open `http://127.0.0.1:5000` in your browser.

## Included
- Responsive landing page and property estimator form
- Flask prediction endpoint (`POST /predict`)
- Pre-trained Random Forest model
- Synthetic sample training dataset
- `train_model.py` to retrain the model after replacing the CSV

## Important model/data limitation
The supplied CSV is synthetic demonstration data. The website and model pipeline work, but predicted values are not actual property market valuations. Replace the CSV with a documented, verified dataset before making real-world claims. The sample model is intended for a college demonstration.
