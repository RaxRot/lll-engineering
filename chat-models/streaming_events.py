from langchain_openai import ChatOpenAI
import asyncio

from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-6-luna")

async def stream_response_events():
    prompt="Describe the NBA"

    async for event_chunk in model.astream_events(prompt,version="v2"):
        print(event_chunk)

asyncio.run(stream_response_events())