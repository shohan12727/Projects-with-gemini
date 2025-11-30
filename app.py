# from google import genai
# from config import gemini_api_key

# client = genai.Client(api_key=gemini_api_key)

# def get_response(question):
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         config=genai.types.GenerateContentConfig(
#             system_instruction="You are a cat. Your name is Neko."
#         ),
#         contents=question,
#     )
#     return response.text    

# while True:
#     question = input("Enter your question: ")
#     if question == "quit":
#         break
#     print(f"Answer: {get_response(question)}")



# from flask import Flask, render_template
# from ai import get_response

# app = Flask(__name__)

# @app.route('/', method=['POST'])
# def chat():
#     message = request.form['message']
#     response = get_response(message)
#     return {"response": response}


# def home():
#     return render_template('index.html')

# @app.route('/chat', )
# def chat():
#      question = input("Enter your question: ")
 
# app.run(); 



from flask import Flask, render_template, request
from ai import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    response = get_response(message)
    return {"response": response}

app.run()
 