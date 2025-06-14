import pandas as pd
from sklearn.impute import KNNImputer
from supabase import create_client, Client
import dotenv
import os

dotenv.load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase_client: Client = create_client(supabase_url, supabase_key)

df = pd.read_csv("dev/ML/data/delhi.csv")

def basic_preprocessing(df):
    # columns to impute : StarRating (KNN), Nearest Landmark (Constant)
    # columns to drop : Distance to landmark, Tax
    imputer = KNNImputer(n_neighbors=5)
    df['Star Rating'] = imputer.fit_transform(df[['Star Rating']])
    df['Nearest Landmark'] = df['Nearest Landmark'].fillna('Unknown')  # Fill with constant value
    df.drop(columns=["Distance to Landmark", 'Tax'], inplace=True)

    # Changing the datatype of the Price column to int
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0).astype(int)

    return df

def data_push_to_supabase(data):
    try:
        data_processed = basic_preprocessing(data)
        data_processed = data_processed.to_dict(orient='records')
        response = supabase_client.table("hotels_delhi").insert(data_processed).execute()

        return response
    except Exception as exception:
        return exception

if __name__ == "__main__":
    response = data_push_to_supabase(df)
    print(response)
