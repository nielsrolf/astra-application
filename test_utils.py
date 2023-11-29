import pytest
from utils import get_openai_response_stream


async def async_print(x):
    print(x, end="")
    
@pytest.mark.asyncio
async def test_get_openai_response_stream():
    # Prepare test data
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]

    # Call the function
    response = await get_openai_response_stream(messages, stream=async_print)
    # Assertions
    assert 'role' in response
    assert 'content' in response
    assert isinstance(response['content'], str)
    assert len(response['content']) > 0  # Ensure some content is returned
