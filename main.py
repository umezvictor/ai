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

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=500,
        messages=messages
    )
    return message.content[0].text


#make a starting list of messages

messages = []

#add initial question
add_user_message(messages, "Define biology in one sentence")

#pass the list of messages into chat function
answer = chat(messages)

#take the answer add it asn an assistant message into the list
add_assistant_message(messages, answer)

#add in the user's follow up question
add_user_message(messages, "What are the classes of living things")

#call chat function again with the list of messages to get a final answer
answer = chat(messages)

print(answer)