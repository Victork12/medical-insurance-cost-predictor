# Medical Insurance Cost Predictor

A Python application that predicts medical insurance charges using linear regression, with a Tkinter graphical interface for easy user input.

## Overview

This project trains a linear regression model on a real-world medical insurance dataset to predict insurance charges based on personal attributes. It includes a simple desktop GUI built with Tkinter so users can enter their information and get an instant cost estimate.

## Features

- Data preprocessing with `LabelEncoder` to convert categorical features (sex, smoker, region) into numerical values
- Linear regression model trained with scikit-learn
- Train/test split for model evaluation (R² score reported on the test set)
- Optional data visualization code (age distribution, sex/children/smoker/region counts, and a correlation heatmap) included but commented out
- Interactive Tkinter GUI for entering age, sex, BMI, children, smoker status, and region to get a real-time charge estimate

## Dataset

The model uses `Medical_insurance.csv`, which contains the following columns:

| Column     | Description                                  |
|------------|-----------------------------------------------|
| `age`      | Age of the primary beneficiary                |
| `sex`      | Gender (`male` / `female`)                    |
| `bmi`      | Body mass index                               |
| `children` | Number of dependents covered                  |
| `smoker`   | Smoking status (`yes` / `no`)                 |
| `region`   | Residential region in the US                  |
| `charges`  | Individual medical costs billed by insurance  |

Dataset source: [Kaggle - Medical Insurance Dataset](https://www.kaggle.com/datasets).

## Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- tkinter (included with most standard Python installations)

Install dependencies with:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

> **Note:** Tkinter usually ships with Python by default. On Linux, if it's missing, install it via your package manager, e.g. `sudo apt-get install python3-tk`.

## Usage

1. Make sure `Medical_insurance.csv` is in the same directory as the script.
2. Run the script:

   ```bash
   python medical_insurance_predictor.py
   ```

3. The script will print the model's R² score to the console.
4. A GUI window will open. Enter the following:
   - **Age** — numeric (e.g., `29`)
   - **Sex** — `Male` or `Female`
   - **BMI** — numeric (e.g., `27.99`)
   - **Number of Children** — numeric (e.g., `2`)
   - **Smoker** — `Yes` or `No`
   - **Region** — `Northeast`, `Northwest`, `Southeast`, or `Southwest`
5. Click **Calculate** to see the estimated insurance cost.

## How It Works

1. The dataset is loaded and categorical columns (`sex`, `smoker`, `region`) are label-encoded into numeric values.
2. Charges are rounded to the nearest 100 to assist with correlation analysis (used only for the optional heatmap visualization).
3. Features (age, BMI, children, encoded sex/smoker/region) are split into training (50%) and test (50%) sets.
4. A linear regression model is trained on the training set and evaluated on the test set using R².
5. The same trained model is used to predict charges from values entered in the GUI.

## Project Structure

```
medical-insurance-cost-predictor/
├── medical_insurance_predictor.py   # Main script: data processing, model training, and GUI
├── Medical_insurance.csv            # Dataset used for training/testing
└── README.md                        # Project documentation
```

## Possible Improvements

- Use a larger training split (e.g., 80/20) for potentially better model accuracy
- Add input validation in the GUI to catch invalid entries before prediction
- Try other regression models (Ridge, Random Forest, etc.) and compare performance
- Add unit tests for data preprocessing and prediction logic

## Author

Victor Kumar

## License

This project is for educational purposes (CS 470 Term Project).
