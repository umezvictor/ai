import json
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5-20251001"

#maintain message history
#add user message
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


#add assistant message
def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }

    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text

messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
#to prevent claude from genrating extra characters, use an assistant message and a stop sequence
add_assistant_message(messages, "```json")
#you can use any character for message prefilling, not just back ticks
result = chat(messages, stop_sequences=["```"])
print(json.loads(result.strip()))