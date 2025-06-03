# 🚀 Task 1 – Data Cleaning & Preprocessing (Python-Based)

### • Tool Used: Python (Pandas)  
### • Dataset: [Startup Funding Dataset – Kaggle]

---

## 🎯 Objective  
Clean a real-world dataset using **Python (Pandas)** by identifying and fixing:

- ❌ Missing values  
- 📄 Duplicate records  
- 🧩 Inconsistent text formatting  
- 📅 Irregular date formats  
- 🧮 Incorrect data types  
- 🧹 Messy column names  

**Goal:** Transform raw data into a clean, structured format suitable for analysis.

---

## 📂 Dataset Overview  

| Metric             | Raw Data  | Cleaned Data  |
|--------------------|-----------|---------------|
| Rows               | 3046      | 3010          |
| Columns            | 13        | 13            |
| Null Values        | ✅ Yes   | ❌ No         |
| Duplicate Rows     | ✅ Yes   | ❌ No         |
| Column Format      | Messy     | Cleaned       |
| Date Consistency   | No        | Yes           |

---

## 🛠 Python Cleaning Steps
1️⃣ Missing Values  
- Used `.isnull().sum()` to identify missing data.  
- Applied `fillna("Unknown")` to handle non-critical missing values.
- 
2️⃣ Duplicate Removal  
- Used `df.drop_duplicates()` to remove **36 duplicate rows**.
- 
3️⃣ Standardized Text Formatting  
- Cleaned `startupname` and `citylocation` using `.str.title().str.strip()`  
- Removed inconsistent casing and extra whitespace.
- 
4️⃣ Column Header Formatting  
- Renamed columns using:
  ```python
  df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
  
5️⃣ Date Format Fix
Converted the date column using:
pd.to_datetime(df['date'], errors='coerce')
Ensured uniform datetime64 format across rows.

6️⃣ Data Type Validation
Verified date as datetime64
Ensured categorical fields are strings, and missing values are handled as "Unknown".


✅ Results After Cleaning

Cleaned dataset with no nulls or duplicate rows.

Column names are uniform and lowercase.

All text fields are consistent in casing.

Dates are correctly parsed and standardized.

The dataset is ready for analysis, visualization, or model building.


📁 Files Included in this Repo

| File Name                     | Description                         |
| ----------------------------- | ----------------------------------- |
| `startup_funding.csv`         | Original raw dataset                |
| `Cleaned_Startup_Funding.csv` | Cleaned dataset after preprocessing |
| `README.md`                   | Task explanation and cleaning steps |
| `clean_startup_data.py`       | Python code used for data cleaning  |


🧠 What I Learned

How to identify and treat missing values and duplicates in real-world data

Standardizing text and dates to improve dataset usability

Importance of data types, formatting, and clean column names

Using Pandas functions effectively for data cleaning

Writing clean, modular, and reproducible data scripts


📝 Notes

Always keep a backup of the original dataset

Document every cleaning step — transparency matters

Python + Pandas is a powerful combo for fast and flexible data wrangling


🔚 Conclusion

This task gave me hands-on experience with real-world data cleaning using Python.

I feel confident dealing with raw, messy datasets and prepping them for meaningful analysis or visualization. ✅


👨‍💻 Author

[Himanshu Dholasiya]
