from google import genai
from config import gemini_api_key

client = genai.Client(api_key=gemini_api_key)
chat = client.chats.create(
    model="gemini-2.5-flash",
     config=genai.types.GenerateContentConfig(
            system_instruction="You are a bot"
     ),
    )


def get_response(question):
    response = chat.send_message(question)
    return response.text  

# while True:
#     question = input("Enter your question: ")
#     if question == "quit":
#         break
#     print(f"Answer: {get_response(question)}")  
