# import anthropic
from groq import Groq
from mcp import ClientSession, StdioServerParameters
from mcp.server.fastmcp.exceptions import FastMCPError, ToolError
from mcp.client.stdio import stdio_client
import asyncio
import os
import dotenv

# loading the environment variables
dotenv.load_dotenv()

async def fetch_hotels_via_mcp() -> str:
    server_params = StdioServerParameters(
        command="uv", 
        args=[
            "run",
            "--with",
            "supabase",
            "--with",
            "mcp[cli]",
            "mcp",
            "run",
            "D:\\project\\travel-site\\dev\\recommender\\mcp-server\\main.py"
        ]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # tools = await session.list_tools()
            result = await session.call_tool(
                "fetch_hotels_near_landmark_from_db",
                {"landmark": "Delhi city centre"}
            )
            return result.content


async def get_recommendations() -> str:
    # fetching the response from the MCP server
    response_mcp = await fetch_hotels_via_mcp()
    print(response_mcp)

    # Setting the system prompt
    system_prompt = """
        You are a JSON extraction engine not a code generating engine. Your task is to process a string containing hotel names along with their ratings and description, and return a structured JSON array where each item represents one hotel.

        Each hotel entry in the output must include:
        - **name**: The name of the hotel (string)
        - **rating**: The rating value associated with the hotel (float or string)
        - **description**: The one liner description of the hotel (string) Add this section on your own.

        RULES & CONSTRAINTS:
        1. Input Format:
        - The input string may contain multiple hotel names and their corresponding ratings, often written together in formats like:
            - `"Hotel Grand Palace - 4.5 stars, Royal Stay Inn: 4.2, Metro Luxury Hotel (4.8)"`, etc.
        - Expect separators such as commas, colons, hyphens, parentheses, or textual phrases like “stars”.

        2. Output Format:
        - Only output a valid JSON array.
        - No natural language explanations outside the JSON.
        - Each entry must have `name`, `rating` and `description` fields.
        - Maintain the hotel name in clean form (remove extra punctuation or suffixes like "stars").
        - Parse ratings into floats if possible (e.g., "4.5 stars" → `4.5`).

        3. Robustness:
        - If a rating is not clearly attached to a hotel, omit that hotel from the JSON.
        - Clean any excessive whitespace or symbols.

        EXAMPLE INPUT:
        "Hotel Name: Country Inn and Suites by Radisson, Sahibabad ----- Rating: 5Hotel Name: Radisson Blu Kaushambi Delhi NCR ----- Rating: 5Hotel Name: Golden Tulip Vasundhara Hotel & Suites, Delhi NCR ----- Rating: 4Hotel Name: Lemon Tree Hotel East Delhi Mall Kaushambi ----- Rating: 4"

        EXPECTED OUTPUT:
        [
        {
            "name": "Country Inn and Suites by Radisson",
            "rating": 5.0,
            "description":"A premium Radisson property offering excellent service and amenities."
        },
        {
            "name": "Radisson Blu Kaushambi",
            "rating": 5.0,
            "description":"Another top-tier Radisson hotel with luxury accommodations"
        },
        {
            "name": "Golden Tulip Vasundhara",
            "rating": 4.0,
            "description":"A well-regarded international chain hotel with good facilities"
        },
        {
            "name": "Lemon Tree Hotel Kaushambi",
            "rating": 4.0,
            "description":"A popular business hotel with modern amenities and convenient location near a shopping mall"
        }
        ]

        Important thing to keep in mind is that you have to generate the description on your own and then add this in the description section of the json.

    """

    client = Groq(api_key=os.getenv("GROQ_KEY"))
    response_client = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        max_tokens=1000,
        messages = [
            {
            "role": "system",
            "content": system_prompt
            },
            {
            "role": "user",
            "content": str(response_mcp)
            }
        ]
    )

    return response_client.choices[0].message.content
    

async def mainFunction():
    response = await get_recommendations()
    print(response)

if __name__ == "__main__":
    asyncio.run(mainFunction())
