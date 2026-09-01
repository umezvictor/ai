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
#initial list of messages
messages = []

#use  while loop to run chat forever
while True:
    user_input = input("> ")
    print(">", user_input)

    #add user input to list of messages
    add_user_message(messages, user_input)
    #call claude with chat function
    answer = chat(messages)
    #add generated text to the list of messages
    add_assistant_message(messages, answer)
    #print generated tect
    print("----------------")
    print(answer)
    print("-------------------")