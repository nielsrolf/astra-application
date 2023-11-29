import pytest
from main import Agent
import os
    
    
@pytest.mark.asyncio
async def test_get_openai_response_stream():
    agent = Agent()
    await agent.reply("Create a file joke.txt, then create a file done.txt")
    assert os.path.exists("joke.txt")
    assert os.path.exists("done.txt")
    await agent.reply("Haha nice joke! Now delete the files again please")
    assert not os.path.exists("joke.txt")
    assert not os.path.exists("done.txt")
