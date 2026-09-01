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

def chat(messages, system =None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 500,
        "messages": messages,
        "temperature": temperature
    }

    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text

messages = []

add_user_message(messages, "Write a 1 sentence of a fake darabase")
#used streaming here - useful for chat applications
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        #print(text, end="")
        pass

print(stream.get_final_message())