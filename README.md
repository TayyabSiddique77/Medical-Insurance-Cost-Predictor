# Medical Insurance Cost Predictor

This project provides a simple web application to predict medical insurance costs based on various personal and health-related factors. It utilizes a pre-trained machine learning model and a scaler to offer interactive predictions through a Streamlit interface.

## Project Purpose

The primary goal of this application is to offer an intuitive tool for users to estimate their potential medical insurance expenses by inputting key demographic and health information.

## Features

-   **Interactive Web Interface:** Built with Streamlit for a user-friendly experience.
-   **Insurance Cost Prediction:** Predicts medical insurance costs based on user inputs.
-   **Input Parameters:** Accepts age, gender, BMI, number of children, smoker status, and region.
-   **Machine Learning Powered:** Uses a pre-trained model and data scaler for predictions.

## Tech Stack

The application is built using the following technologies:

-   **Python:** The core programming language.
-   **Streamlit:** For creating the interactive web user interface.
-   **Pandas:** Used for data manipulation and structuring input data.
-   **NumPy:** For numerical operations, often a dependency for ML libraries.
-   **Scikit-learn (Implied):** The machine learning model and scaler (`model.pkl`, `my_scalar.pkl`) are typically serialized from scikit-learn objects.

## Model Information

The application uses a pre-trained machine learning model (`model.pkl`) along with a fitted feature scaler (`my_scalar.pkl`) to generate insurance cost predictions. These artifacts are loaded at runtime by the Streamlit application. 

## Setup

To get this project up and running on your local machine, follow these steps:

### Prerequisites

-   Python 3.x installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Medical-Insurance-Cost-Predictor
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Model and Scaler Files:** Ensure that `model.pkl` (the trained machine learning model) and `my_scalar.pkl` (the trained data scaler) are present in the project's root directory (alongside `app.py`). These files are crucial for the application's functionality and are expected to be pre-trained.

## Usage

To run the Streamlit application, navigate to the project's root directory in your terminal and execute the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser. You can then enter the required details into the input fields and click the "Predict" button to see the estimated medical insurance cost.

## Project Structure

```
Medical-Insurance-Cost-Predictor/
├── app.py                  # The main Streamlit application script
├── model.pkl               # Pre-trained machine learning model
├── my_scalar.pkl           # Pre-trained data scaler
├── README.md               # Project README file
└── requirements.txt        # Python dependencies
```
## Future Improvements

- Support additional machine learning models for comparison.
- Improve feature engineering and model accuracy.
- Add model evaluation metrics and visualizations.
- Deploy the application to Streamlit Community Cloud or another cloud platform.
- Containerize the application using Docker.