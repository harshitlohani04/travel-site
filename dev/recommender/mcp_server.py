from mcp.server.fastmcp import FastMCP
# from models.db import supabase_client
import dotenv
import os
from supabase import create_client, Client

# MCP server initialization
mcp = FastMCP("tripmate-mcp")

# supabase
dotenv.load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase_client: Client = create_client(supabase_url, supabase_key) 

# MCP resource creation
# @mcp.resource

# MCP tools creation
@mcp.tool()
def get_recommendations(location: str) -> list:
    """
    Get recommendations for a user based on their ID and location.
    
    Args:
        location (str): The location to get recommendations for.
    
    Returns:
        list: A list of recommended items.
    """
    # Fetch recommendations from the database
    response = supabase_client.table("hotels_delhi").select("*").eq("Nearest Landmark", location).execute()
    
    if response.error:
        raise Exception(f"Error fetching recommendations: {response.error.message}")
    
    return f"Sugest the best hotel among the following options : {response.data}"

# MCP router configuration


