# server.py
from mcp.server.fastmcp import FastMCP
import pandas as pd
from supabase import create_client, Client
import dotenv
import os
from functools import lru_cache

dotenv.load_dotenv()

# Create an MCP server
mcp = FastMCP("Demo")
df = pd.read_csv("D:\\project\\travel-site\\dev\\ML\\data\\delhi.csv")

@lru_cache(maxsize=1) # For lazy loading of the supabase client
def get_supabase_client() -> Client:
    """Get cached Supabase client"""
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    
    if not supabase_url or not supabase_key:
        raise ValueError("Missing Supabase credentials")
    
    return create_client(supabase_url, supabase_key)

@mcp.tool()
def fetch_hotels_near_landmark_from_db(landmark:str) -> str:
    """ Return a string of hotels in Delhi fetching from the database """
    client = get_supabase_client()
    response = client.table("hotels_delhi").select("*").eq("Nearest Landmark", landmark).execute()
    hotels = response.data

    if not hotels:
        return f"No hotels found near {landmark}"
    hotels_data = ""
    for hotel in hotels:
        hotels_data += f"Hotel Name: {hotel['Hotel Name']} ----- Rating: {hotel['Star Rating']}\t"

    return hotels_data


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

