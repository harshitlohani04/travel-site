from supabase import create_client, Client
import dotenv
import os

dotenv.load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase_client: Client = create_client(supabase_url, supabase_key)

