import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # loads .env locally

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY is not set")

client = genai.Client(api_key=api_key)

# async def summarize_text(text: str) -> str:
#     # Get the list and convert to a list of names immediately
#     response = await client.aio.models.list()
#     # Extract only the names to avoid any weird formatting issues
#     available_names = [m.name for m in response]
    
#     return f"Your available models are: {', '.join(available_names)}"

async def summarize_text(text: str) -> str:
    # Use the exact string from your successful list command
    # model_id = "gemini-2.0-flash"
    # model_id = "gemini-1.5-flash"  # Try without the 'models/' prefix again
    # OR if that fails, use the one from your list that is stable:
    model_id = "gemini-flash-latest" 
    
    try:
        response = await client.aio.models.generate_content(
            model=model_id,
            contents=f"Summarize this text professionally: {text}"
        )
        return response.text
    except Exception as e:
        return f"Error with {model_id}: {str(e)}"
