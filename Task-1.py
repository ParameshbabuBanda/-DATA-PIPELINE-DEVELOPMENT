######DATA PIPELINE DEVELOPMENT

import os  # For file path operations
import pandas as pd  # For data manipulation and analysis
from sklearn.preprocessing import StandardScaler, LabelEncoder  # For encoding and scaling
from sklearn.model_selection import train_test_split  # For splitting dataset

i="Loan_data.csv"
file_dir=os.path.join(os.getcwd(),r'C:\Users\param\OneDrive\Documents\NareshIT\DataFiles') # <-- Update this path to your directory
file_path=file_dir+'\\'+i

# Load loan dataset (Extract step)
df = pd.read_csv(file_path)  # <-- make sure 'loan_dataset.csv' is available

# Example: encode target column (assuming 'Loan_Status' is the target)
le = LabelEncoder()
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

# Standardize feature columns (excluding the target)
scaler = StandardScaler()
# Dropping non-numeric columns before scaling (optional: depends on your dataset)
X = df.drop('Loan_Status', axis=1).select_dtypes(include=['float64', 'int64'])
scaled_features = scaler.fit_transform(X)

# Split the data into training and test sets (Load step)
X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, df['Loan_Status'], test_size=0.2, random_state=42
)

print("ETL Process for Loan Dataset Completed")
