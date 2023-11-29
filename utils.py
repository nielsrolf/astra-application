import asyncio
from retry import retry
from typing import List, Dict, Callable

import openai


@retry(tries=10, delay=2, backoff=2, jitter=(1, 3))
async def get_openai_response_stream(
    messages: List[Dict], stream: Callable, model: str="gpt-4-0613",
) -> str:
    response = {
        'role': 'assistant',
        'content': ''
    }
    try:
        openai_response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            temperature=0.1,
            stream=True,
            stop=['</bash>']
        )
        # iterate through the stream of events
        async for chunk in openai_response:
            chunk = chunk["choices"][0]["delta"].to_dict_recursive()
            if 'content' not in chunk:
                continue
            chunk = chunk['content']
            response['content'] += chunk
            await stream(chunk)
    except openai.error.RateLimitError as e:
        import time
        print("We got rate limited, chilling for a minute...")
        await asyncio.sleep(60)
        raise e
    
    return response