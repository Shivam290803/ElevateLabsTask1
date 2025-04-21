import pandas as pd

def clean_data():
    df = pd.read_csv('dataset.csv', sep='|')

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    print("Info:")
    print(df.info())
    print("\nHead:")
    print(df.head())
    print("\nDescription:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    df = df.dropna()
    df = df.drop_duplicates()

    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.lower().str.strip()
        df['gender'] = df['gender'].replace({'f': 'female', 'm': 'male'})

    if 'date_joined' in df.columns:
        df['date_joined'] = df['date_joined'].astype(str).str.strip()
        df['date_joined'] = pd.to_datetime(df['date_joined'], format='%d-%m-%Y', errors='coerce')

    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

    df = df.dropna()

    df.to_csv('cleaned_mall_customer_data.csv', index=False)
    print("\nCleaned data saved to 'cleaned_mall_customer_data.csv'.")

if __name__ == "__main__":
    clean_data()
