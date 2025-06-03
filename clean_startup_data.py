import pandas as pd

# Load the dataset
df = pd.read_csv("startup_funding.csv", encoding='latin1')

print("Original Data Preview:")
print(df.head())
print("\nData Shape:", df.shape)

# Check missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Check data types
print("\n Data Types:")
print(df.dtypes)

# Remove duplicates
df_before = df.shape[0]
df.drop_duplicates(inplace=True)
df_after = df.shape[0]
print(f"\n Duplicates Removed: {df_before - df_after}")

# Strip whitespaces from column names and lowercase
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Fix inconsistent formatting (basic example)
if 'citylocation' in df.columns:
    df['citylocation'] = df['citylocation'].str.title().str.strip()

if 'startupname' in df.columns:
    df['startupname'] = df['startupname'].str.title().str.strip()

# Convert 'date' column to datetime format
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Handle missing values - for demo, we fill them with 'Unknown'
df.fillna("Unknown", inplace=True)

# Recheck missing values
print("\n Missing Values After Cleaning:")
print(df.isnull().sum())

# Final data types
print("\n Final Data Types:")
print(df.dtypes)

# Save the cleaned data
df.to_csv("Cleaned_Startup_Funding.csv", index=False)
print("\n Cleaned file saved as 'Cleaned_Startup_Funding.csv'")
