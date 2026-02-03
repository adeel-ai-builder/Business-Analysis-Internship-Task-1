import pandas as pd
# load the datasete 
df=pd.read_csv("Telco_Customer_Churn_Dataset  (3).csv")

# show first 10 row
print("First 10 rows of the dataset:")
print(df.head(10))

# show the shape of dataset
print("\nDataset shape (rows, columns):")
print(df.shape)

# show the columns name
print("\nColumn names:")
print(df.columns)

# show the data types of each columns
print("\nData types of each column:")
print(df.dtypes)

# check missing values in dataset
print("\nMissing values in each column:")
print(df.isnull().sum())

# show the dataset summary
print("\nDataset info:")
print(df.info())