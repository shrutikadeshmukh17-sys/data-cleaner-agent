# 🧹 Data Cleaner Agent

## About the Project
Data Cleaner Agent is a Python-based web application that helps users clean CSV and Excel datasets automatically. It is built using Streamlit and Pandas.

## Features
- Upload CSV and Excel files
- Detect missing values
- Identify duplicate rows
- Fill missing numeric values using the median
- Fill missing text values using the most frequent value
- Remove duplicate records
- Preview original and cleaned datasets
- Download cleaned data in Excel and CSV formats
- View data quality summaries

## Technologies Used
- Python
- Streamlit
- Pandas
- OpenPyXL

## Installation and Setup

1. Install Python on your computer.
2. Clone or download this repository.
3. Open a terminal inside the project folder.
4. Install the required libraries:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python -m streamlit run app.py
```

6. Open the local URL displayed in the terminal.

## How to Use
1. Upload a CSV or Excel dataset.
2. Review the original data and its quality summary.
3. Click **Clean Dataset**.
4. Review the cleaned data.
5. Download the cleaned dataset in Excel or CSV format.

## Project Goal
The goal of this project is to simplify data preprocessing and demonstrate practical skills in Python programming, data cleaning, and data analytics.

## Author
Shrutika Deshmukh
